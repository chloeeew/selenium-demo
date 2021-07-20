"""
==================
Author:Chloeee
Time:2021/3/28 12:44
Contact:403505960@qq.com
==================
"""

import logging
from common.globalmethod import get_current_time_str_time
from logging import Logger
from common.yaml_handler import yaml_config
from config.path import logs_dir, join_dir_file

class MyLogger(Logger):
    # 获取配置文件的内容
    conf = yaml_config['log_conf']
    name = conf["name"]
    level = conf["level"]
    fmt_str = conf["formatter"]

    def __init__(self):
        # 动态生成log文件名称
        now_time_str = get_current_time_str_time()
        file_name = f"auto_test_log_{now_time_str}.log"
        file = join_dir_file(logs_dir, file_name)
        # 设置日志器名称和日志级别
        super().__init__(self.name,self.level)

        # 设置处理器
        handle1 = logging.StreamHandler()

        # 设置日志输出格式
        fmt = logging.Formatter(self.fmt_str)
        handle1.setFormatter(fmt)

        # 将处理器和日志器绑定
        self.addHandler(handle1)

        # 添加文件处理器，并与日志器绑定
        if file:
            handle2 = logging.FileHandler(file,mode='a',encoding='utf-8')
            handle2.setFormatter(fmt)
            self.addHandler(handle2)


logger = MyLogger()


if __name__ == "__main__":
    logger.info("22")

