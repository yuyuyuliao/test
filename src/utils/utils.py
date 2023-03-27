import re
from asyncio import iscoroutinefunction
from functools import wraps, partial
from typing import Callable


from utils.constants import EXT_TYPES
from utils.exceptions import TooManyTriesError

jinja2_template_funcs = {}


def register_for_jinja2(func: Callable = None, name: str = None):
    """
    将函数注册到jinja2_template_funcs之中
    注册后的函数可以在jinja2模版中进行调用

    :param name: jinja2模版中调用使用的名字，默认为func name
    :param func: 函数对象
    :return: 函数
    """

    if func is None:
        return partial(register_for_jinja2, name=name)
    name = name or func.__name__
    jinja2_template_funcs[name] = func
    return func


def form_data_to_json(data: str) -> dict:
    """
    将form表单字符串转为json

    :param data: provinceJT=JT&docTitle=&docCode=
    :return: {'provinceJT': 'JT', 'docTitle': '', 'docCode': ''}
    """
    return {item.split("=")[0]: item.split("=")[1] for item in data.split("&")}


def retry(times: int):
    """
    简单的重试装饰器

    :param times: 重试次数
    :return:
    """

    def func_wrapper(func):
        @wraps(func)
        async def wrapped(*args, **kwargs):
            for _ in range(times):
                try:
                    if iscoroutinefunction(func):
                        return await func(*args, **kwargs)
                    else:
                        return func(*args, **kwargs)
                except Exception as exc:
                    pass
            raise TooManyTriesError(f"{func.__name__} too many retries")

        return wrapped

    return func_wrapper


def retry_no_async(times: int):
    """
    简单的重试装饰器

    :param times: 重试次数
    :return:
    """

    def func_wrapper(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    pass
            raise TooManyTriesError(f"{func.__name__} too many retries")

        return wrapped

    return func_wrapper


@register_for_jinja2
def false_to_str(false) -> str:
    """
    将python中被认为是false类型的数据转为空字符串

    :param false: None / [] / {} / false
    :return:
    """
    return false if false else ""


def file_add_ext_type(file_url, file_title):
    """
    输入文件url，文件名，判断是否有后缀，如果文件名没后缀，加url内的

    :param file_url: 文件url
    :param file_title: 文件名
    :return: 原始文件名，新文件名
    """
    origin_file_title = file_title
    file_title = file_title.strip()
    for ext_type in EXT_TYPES:
        ext_type = ext_type.upper()
        up_file_title = file_title.upper()
        up_file_url = file_url.upper()
        if up_file_title.endswith(ext_type):
            new_file_title = file_title
            return origin_file_title, new_file_title
        else:
            if up_file_url.endswith(ext_type):
                new_file_title = file_title + f".{ext_type}"
                return origin_file_title, new_file_title
    else:
        new_file_title = ""
        return origin_file_title, new_file_title


def get_filename_by_headers(headers):
    """
    输入提取后的response.headers内容
    形如 response.headers["Content-Disposition"]
    b'attachment;filename="NMG00014000000479-%E6%BB%A1%E6%B4%B2%E9%87%8C%E5%B8%82%E7%A7%83%E5%B0%BE%E5%B1%B1%E5%8E%86%E5%8F%B2%E9%81%97%E7%95%99%E5%9C%B0%E8%B4%A8%E7%8E%AF%E5%A2%83%E5%92%8C%E8%8D%89%E5%8E%9F%E6%A4%8D%E8%A2%AB%E7%94%9F%E6%80%81%E4%BF%AE%E5%A4%8D%E5%B7%A5%E7%A8%8B%EF%BC%88%E4%BA%8C%E6%AC%A1%EF%BC%89.pdf"'
    key为=号前的内容 用于正则

    :param headers: 响应头
    :return: 文件名
    """
    file_content = headers.get("Content-Disposition", "")
    file_key_list = ["filename"]
    for file_key in file_key_list:
        try:
            info = re.findall(f'{file_key}="(.*?)"', file_content.decode())
        except UnicodeDecodeError:
            info = re.findall(f'{file_key}="(.*?)"', file_content.decode("GBK"))
        if info:
            return info[0]
        else:
            try:
                info = re.findall(f"{file_key}=(.*?)$", file_content.decode())
            except UnicodeDecodeError:
                info = re.findall(f'{file_key}="(.*?)$"', file_content.decode("GBK"))
            if info:
                return info[0]
    else:
        return ""
