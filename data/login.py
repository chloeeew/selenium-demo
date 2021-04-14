"""
==================
Author:Chloeee
Time:2021/3/18 21:37
Contact:403505960@qq.com
==================
"""


"""
登录的数据格式为：(username,pwd,expected)
"""

data_list_success = [
    ("looker53@sina.com","admin123456","yuze")
]


data_list_wrong = [
    ("","admin123456",["账号不能为空"]),
    ("looker53@sina.com","",["密码不能为空"]),
    ("nousername","admin123456",["用户不存在"]),
    ("looker53@sina.com","12345",["密码有效长度是6到30个字符"]),
    ("looker53@sina.com","1234567890123456789012345678901",["密码有效长度是6到30个字符"])
]


