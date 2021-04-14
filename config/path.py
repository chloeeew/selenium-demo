"""
==================
Author:Chloeee
Time:2021/3/18 22:38
Contact:403505960@qq.com
==================
"""

import os

# 当前目录
current_abs_path = os.path.abspath(__file__)

# 当前文件夹即config文件夹
config_dir = os.path.dirname(current_abs_path)

# 顶级文件夹
top_dir = os.path.dirname(config_dir)

# data文件夹 不存在则创建
data_dir = os.path.join(top_dir,"data")
if not os.path.exists(data_dir):
    os.mkdir(data_dir)

# config.yaml文件
config_yaml_path = os.path.join(config_dir,"config.yaml")

# logs文件夹
logs_dir = os.path.join(top_dir, "logs")

# img 文件夹
img_dir = os.path.join(top_dir,"img")

def join_dir_file(dir_name, filename):
    return os.path.join(dir_name,filename)


