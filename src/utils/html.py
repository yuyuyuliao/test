# -- coding: utf-8 --
import re
from xml.sax.saxutils import unescape
from typing import Iterable


def html_unescape(content):
    """
    将content 变成 html 语言
    比如 &nt &gt..... 变成<>

    :param content：待处理文本
    :return: html
    """
    return unescape(content)


def replace_tags(text: str, old_tag, new_tag):
    """
    将文本中的tag类型替换

    :param text: 待处理文本
    :param old_tag: 需要替换的旧标签名
    :param new_tag: 用来替换的新标签名
    :return: 处理后的文本
    """
    content = re.sub(f"<{old_tag}.*?>", f"<{new_tag}>", text)
    content = re.sub(f"</{old_tag}.*?>", f"</{new_tag}>", content)
    return content
