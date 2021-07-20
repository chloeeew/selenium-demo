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

# 获取用例yaml
yaml_testcase = read_yaml(path.testcase_yaml_path)



if __name__ == '__main__':
    print(yaml_testcase.get('data_list_success'))
