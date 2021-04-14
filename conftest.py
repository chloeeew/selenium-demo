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

student_info = yaml_config["student_info"]
teacher_info = yaml_config["teacher_info"]

@pytest.fixture()
def get_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    time.sleep(3)
    driver.quit()


@pytest.fixture()
def login_teacher():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    login_page = LoginPage(driver).get_into_login_url()
    login_page.set_usr_and_password(teacher_info["usr"], teacher_info["pwd"]).click_login_confirm()
    yield driver
    time.sleep(3)
    driver.quit()


@pytest.fixture()
def login_student():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    login_page = LoginPage(driver).get_into_login_url()
    login_page.set_usr_and_password(student_info['usr'], student_info['pwd']).click_login_confirm()
    yield driver
    time.sleep(3)
    driver.quit()