import time
from datetime import datetime, timedelta, date
import arrow
import dateparser


def date_ago(target_date):
    """
    计算指定时间距离今天多少天
    diff_date - current_date

    :param target_date: 目标日期
    :return: 天数差
    """
    return (datetime.today() - dateparser.parse(str(target_date))).days


def time_transformation(timestamp):
    """
    jinja2 时间戳转换日期

    :param timestamp: 时间戳 10位
    :return: 日期  年-月-日
    """
    time_array = time.localtime(int(str(timestamp)[0:10]))
    date_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return date_time


def timestamp_to_date(timestamp):
    """
    时间戳 转换成日期

    :param timestamp: 时间戳 10位
    :return: 日期  年-月-日
    """
    return arrow.get(timestamp).format("YYYY-MM-DD")


def time_zone_conversion(date_time, time_zone):
    """
    将日期转换为设置时区的年月日

    :param date_time: 如 2023-03-29T15:00:00.000+00:00 的str格式
    :param time_zone: 时区 int格式
    :return: 日期
    """
    datetime_n = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S.%f+00:00") + timedelta(
        hours=time_zone
    )
    datetime_n = datetime_n.strftime("%Y-%m-%d")
    return datetime_n


def javascript_timestamp():
    """
    同 js代码  Date.parse(dt)
    得到 13 位当前时间的时间戳 如1562255999000，后三位固定为 000

    :return: 时间戳
    """
    return int(str(int(arrow.now().timestamp())) + "000")


def now_timestamp():
    """
    返回13位当前时间的时间戳  后三位是有数字的！！！！！！

    :return: 时间戳
    """
    return str(round(time.time() * 1000))


def date_parse(date_str: str) -> "datetime":
    """
    输入任意字符串返回datetime类型

    :param date_str: '1991-05-17' / 'In two months' / 1484823450
    :return: datetime.datetime(2017, 1, 19, 10, 57, 30)
    """
    return dateparser.parse(date_str)


def previous_date(day_nums: int, date_model="%Y-%m-%d") -> str:
    """
    输入数字返回距离当天第x天的日期 年-月-日 日期为该天00:00:00
    date_model 可以设置日期格式 默认为年-月-日  如 2001-01-31

    :param date_model: 日期格式 （默认'%Y-%m-%d'）
    :param day_nums: 相隔天数
    :return: 目标日期
    """
    today = date.today()
    previous_day = today - timedelta(days=day_nums)
    previous_day = previous_day.strftime(date_model)
    return previous_day


def greater_than_oneday(day_nums: int, target_date: str):
    """
    输入距今天数  和  某天日期，
    比较是否 距今天数的日期  <=  某天

    :param day_nums: 距今天数
    :param target_date: 目标日期
    :return: 是否小于等于
    """
    today = date.today()
    previous_day = today + timedelta(days=day_nums)
    info_date = dateparser.parse(str(target_date)).date()
    return previous_day <= info_date
