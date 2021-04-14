"""
==================
Author:Chloeee
Time:2021/3/18 22:50
Contact:403505960@qq.com
==================
"""
from config import path
import yaml


def read_yaml(fpath):
    """
    :param fpath: yaml路径
    :return: yaml里的数据
    """
    with open(fpath, encoding="utf-8") as f:
        data = yaml.load(f, yaml.FullLoader)
        return data


# 获取yaml配置项
yaml_config = read_yaml(path.config_yaml_path)
