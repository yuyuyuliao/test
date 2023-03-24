import re
from json import JSONDecodeError, loads
from pathlib import Path


def clean_text(string: str) -> str:
    """
    清洗特殊字符

    :param string: 正文内容
    :return: 清洗后的正文内容
    """
    return re.sub(
        '<span .*?>|<!D.*dtd">|\\n|\\t|\\r|\xa0|\\u3000|textarea|&quot;|&lt;',
        "",
        string,
    )


def tailless(string: str) -> str:
    """
    去除字符串末尾的`类型标注`

    Example:
    tailless('/a/b/c.docs') # => '/a/b/c'

    :param string (str): 需要处理的字符串
    :return str: 处理后的字符串

    """
    return str(Path(string).with_suffix(""))


def clear_title(word) -> str:
    r"""
    对标题中的一些特殊字符进行去除 如'\\t\\n\\r nbsp;'等

    :param word: 需要处理的字符串
    :return: 处理后的字符串
    """
    word = re.sub(r"[\t\n\r]", "", word)
    word = re.sub(
        r"[\u003c\u003e\u0001\u2002\u2003\u0001\uf096\u200c\u200f\u202a\u202b\u202c"
        r"\u2028\ue010\ufeff\ue862\ue861\u200d\u200b\u2005\u2006\u2009\ue234\ue0e5"
        r"\ue261\ue306\ue495\ue236\ue0cf\ue0e9\ue00f\ue495\uf0b7\ue00c\ue2e5\ue3ac"
        r"\ue004\ue003\xa0\xad\x96\x7f\u3000]|nbsp;",
        " ",
        word,
    )

    word = word.strip()
    return word


def clear_file_name(file_name: str) -> str:
    r"""
    对文件名中的一些特殊字符进行去除如\\n\\r等

    :param file_name: 待处理文件名
    :return: 清洗后的文件名
    """
    return re.sub(r"\n|\r| .|\t", "", file_name)


def text_to_json(text):
    """
    将text变成json

    :param text: 待处理字符串
    :return: json
    """
    try:
        json = loads(text)
    except JSONDecodeError:
        json = {}
    return json
