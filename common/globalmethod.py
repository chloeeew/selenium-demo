# -*- coding:utf-8 -*-
# @Time    :2021/3/21 13:18
# @Author  :ChloeeeeWang
# @Email   :403505960@qq.com
# @File    :.py
# @Software:PyCharm

import random
import time
import datetime


def generate_name():
    class_name_list = []
    for i in range(10):
        int_c = random.randint(97, 122)  # a-z的ascii码
        alpha = chr(int_c)
        class_name_list.append(alpha)
    time_str = f"{int(time.time())}"
    class_name_list.append(time_str)
    class_name = ''.join(class_name_list)
    return class_name


def get_current_time():
    return datetime.datetime.now()


def get_current_time_range_list(now):
    """根据当前时间获得区间范围值，并以hh24：mm格式列表输出"""
    time_list = []
    before = now + datetime.timedelta(minutes=-1)
    after = now + datetime.timedelta(minutes=1)

    now_time = now.strftime('%H:%M')
    before_time = before.strftime("%H:%M")
    after_time = after.strftime("%H:%M")
    time_list.extend([before_time, now_time, after_time])
    return time_list

def get_current_time_str_time():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H_%M_%S")