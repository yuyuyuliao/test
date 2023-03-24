from urllib import parse
from urllib.parse import parse_qs, urlparse
from w3lib.url import (
    add_or_replace_parameter,
    add_or_replace_parameters,
    canonicalize_url,
)


def url_fix(response_url: str, detail_url: str) -> str:
    """
    根据请求url拼接不完整的url

    :param response_url: 请求url
    :param detail_url: 需要拼接的url
    :return: 拼接完成的url
    """
    url1 = parse.urljoin(response_url, detail_url)

    return url1


def url_encode(string, safe_word="/"):
    """
    字符串 url编码

    :param safe_word:
    :param string: '你好'
    :return: '%E4%BD%A0%E5%A5%BD'
    """
    return parse.quote(string, safe=safe_word)


def url_unencode(string):
    """
    字符串 url解码

    :param string: '%E4%BD%A0%E5%A5%BD'
    :return: '你好'
    """
    return parse.unquote(string)


def url_query_encode(query: dict):
    """
    对params 的字典 进行url编码

    :param query: {'wd': 'Python3标准库'}
    :return: 'wd=Python3%E6%A0%87%E5%87%86%E5%BA%93'
    """

    return parse.urlencode(query)


def url_query_to_dict(url: str):
    """
    将url后的参数提取出来生成字典

    :param query: https/www.xxxx.com?a=2&c=3
    :return: {'a':'2','c':'3'}
    """
    ret_dict = {}
    querys = parse.urlparse(url).query
    if querys:
        for query in querys.split("&"):
            key, value = query.split("=")
            ret_dict[key] = value
    return ret_dict


def clean_url(url_string):
    """
    对 正则匹配后的 a标签的href 进行清洗

    :param url_string: ' "http://xxxxx.xxxxx.xxxx"  target=_blank'
    :return:  'http://xxxxx.xxxxx.xxxx'
    """
    return url_string.replace('"', "").replace(" ", "").replace("target=_blank", "")


def add_or_replace_param(url: str, param_key: str, param_value: str) -> str:
    """
    新增或替换url中的单个参数

    :param url: http://www.example.com/index.php
    :param param_key: arg
    :param param_value: v
    :return: http://www.example.com/index.php?arg=v
    """
    return add_or_replace_parameter(url, param_key, param_value)


def add_or_replace_params(url: str, params: dict) -> str:
    """
    新增或替换url中的多个参数

    :param url: http://www.example.com/index.php
    :param params: {"arg", "v"}
    :return: http://www.example.com/index.php?arg=v
    """
    return add_or_replace_parameters(url, params)


def format_url(url: str):
    """
    格式化URL
    url编码, 使URL安全
    对查询参数进行排序，先按键，后按值
    将所有空格（在查询参数中）'+'（加号）规范化
    将百分比编码的大小写规范化（%2f->%2F）。
    删除有空白值的查询参数

    :param url: http://www.example.com/r\u00e9sum\u00e9
    :return: http://www.example.com/r%C3%A9sum%C3%A9
    """
    return canonicalize_url(url)


def parse_params(url: str):
    """
    解析出url的后缀生成字典

    :param url: 'http://xxx?a=1&b=2'
    :return: {"a": ['1'], "b": ['2']}
    """
    return parse_qs(urlparse(url).query)
