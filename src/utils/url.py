from urllib import parse
from urllib.parse import parse_qs, urlparse

from utils.constants import EXT_TYPES


def is_attachment_href(href) -> bool:
    """判断链接是否含有附件

    :param: href (str): 字符串链接 <a href='xxxx'>name.pdf</a>
    :return: bool: True or False
    """
    if not href:
        return False
    for ext in EXT_TYPES:
        if ext in href:
            return True
    return False


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


def parse_params(url: str):
    """
    解析出url的后缀生成字典

    :param url: 'http://xxx?a=1&b=2'
    :return: {"a": ['1'], "b": ['2']}
    """
    return parse_qs(urlparse(url).query)
