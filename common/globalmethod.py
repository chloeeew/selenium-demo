# -*- coding:utf-8 -*-
# @Time    :2021/3/21 13:18
# @Author  :ChloeeeeWang
# @Email   :403505960@qq.com
# @File    :.py
# @Software:PyCharm

import random
import time
import datetime
# from common.logger_handler import logger


def generate_name():
    """
    生成并返回随机名称：10位随机字母+int时间戳
    """
    random_name_list = []
    for i in range(10):
        int_c = random.randint(97, 122)  # a-z的ascii码
        alpha = chr(int_c)
        random_name_list.append(alpha)
    time_str = f"{int(time.time())}"
    random_name_list.append(time_str)
    random_name = ''.join(random_name_list)
    # logger.info(f"生成的随机名称为：{random_name}")
    return random_name


def get_current_time():
    """
    获取当前时间
    """
    current_time = datetime.datetime.now()
    # logger.info(f"获取当前时间为：{current_time}")
    return current_time


def get_current_time_range_list(now):
    """根据当前时间获得区间范围值，前后一分钟共3分钟的范围值，并以hh24：mm格式列表输出
    传入的时间时13：16那么返回的时间返回list时13：15 13:16 13:17
    """
    time_list = []
    before = now + datetime.timedelta(minutes=-1)
    after = now + datetime.timedelta(minutes=1)

    now_time = now.strftime('%H:%M')
    before_time = before.strftime("%H:%M")
    after_time = after.strftime("%H:%M")
    time_list.extend([before_time, now_time, after_time])
    return time_list

def get_current_time_str_time():
    """
    按照指定格式输出时间
    """
    now_time = datetime.datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
    return now_time


