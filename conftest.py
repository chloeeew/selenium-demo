"""
==================
Author:Chloeee
Time:2021/3/16 21:54
Contact:403505960@qq.com
==================
"""
from selenium import webdriver
from pages.login import LoginPage
from common.yaml_handler import yaml_config
import time
import pytest


@pytest.fixture()
def get_driver():
    """
    打开网页
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    time.sleep(3)
    driver.quit()


@pytest.fixture()
def login_teacher(get_driver):
    """
    登录老师账号
    """
    login_page = LoginPage(get_driver).get_into_login_url()
    login_page.set_usr_and_password(yaml_config["teacher_info"]["usr"], yaml_config["teacher_info"]["pwd"]).\
        click_login_confirm()
    time.sleep(2)
    yield get_driver



@pytest.fixture()
def login_student():
    """
    登录学生账号
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    login_page = LoginPage(driver).get_into_login_url()
    login_page.set_usr_and_password(yaml_config["student_info"]['usr'], yaml_config["student_info"]['pwd']).\
        click_login_confirm()
    time.sleep(2)
    yield driver
    time.sleep(3)
    driver.quit()


