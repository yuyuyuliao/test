# -- coding: utf-8 --
import re
from xml.sax.saxutils import unescape
from typing import Iterable

from w3lib.html import (
    strip_html5_whitespace,
    remove_tags_with_content,
    remove_tags as html_remove_tags,
    remove_comments as html_remove_comments,
    replace_escape_chars,
)


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


def remove_tags(text: str, which_ones: Iterable[str] = (), keep: Iterable[str] = ()):
    """
    仅删除 HTML 标签。
    which_ones	keep	它能做什么
    不是空的	空的	删除所有which_ones标签
    空的	不是空的	删除所有标签keep之外的标签
    空的	空的	删除所有标签
    不是空的	不是空的	不允许

    :param text: HTML
    :param which_ones: 需要删除的标签
    :param keep: 需要保留的标签
    :return: 处理后的HTML
    """
    return html_remove_tags(text, which_ones, keep)


def remove_tags_content(text: str, which_ones: Iterable[str] = ()):
    """
    删除标签及其内容

    :param text: HTML
    :param which_ones: 要删除哪些标签的元组，包括它们的内容。如果为空，则返回未修改的字符串。
    :return: 处理后的HTML
    """
    return remove_tags_with_content(text, which_ones)


def remove_comments(text: str):
    """
    删除 HTML 注释。

    :param text: HTML
    :return: 处理后的HTML
    """
    return html_remove_comments(text)


def remove_escape_chars(text: str):
    """
    删除转义字符

    :param text: HTML
    :return: 处理后的HTML
    """
    return replace_escape_chars(text)


def remove_html5_whitespace(text: str):
    r"""
    去除所有前后空格字符( \\t\\n\\r\\x0c)

    :param text: HTML
    :return: 处理后的HTML
    """
    return strip_html5_whitespace(text)
