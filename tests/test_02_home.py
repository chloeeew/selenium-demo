# -*- coding:utf-8 -*-
# @Time    :2021/3/20 19:16
# @Author  :ChloeeeeWang
# @Email   :403505960@qq.com
# @File    :.py
# @Software:PyCharm

import time
import allure
from pages.home import HomePageTeacher,HomePageStudent
from pages.course import CoursePageTeacher
from common.globalmethod import generate_name
from common.yaml_handler import yaml_config
from common.logger_handler import logger


@allure.feature("个人主页测试")
class TestHome:

    @allure.title("冒烟测试-创建课程")
    def test_add_class(self,login_teacher):
        """以老师的形式，创建课程"""
        home_page = HomePageTeacher(login_teacher)
        class_name = generate_name()    # 生成随机名字
        home_page.create_class(class_name)  # 根据随机名字创建课程

        # 断言：是否存在该课程名称的课
        try:
            assert home_page.check_class_by_name(class_name)
        except AssertionError:
            logger.error(f"断言失败，不存在{class_name}名称的课程，请检查")
            raise AssertionError


    @allure.title("冒烟测试-加入课程")
    def test_add_class_num_without_teacher_add_class(self,login_student, login_teacher):
        """以学生的形式，加入课程"""
        class_num = yaml_config["class_info"]["class_num"]
        driver_student = login_student
        driver_teacher = login_teacher

        home_page_student = HomePageStudent(driver_student)
        # WHEN ALREADY EXIST COURSE QUIT THE CLASS, IF DOSE NOT EXIT THEN ADD CLASS
        home_page_student.add_class(class_num,yaml_config["student_info"]["pwd"])

        # assert the existence of the course in student-homepage
        try:
            assert home_page_student.check_class_by_num(class_num)
        except AssertionError:
            logger.error(f"断言失败，学生主页面不存在课程{class_num},请检查")
            raise AssertionError


        # switch to teacher-homepage , assert the existence of the student in course-member-page
        home_page_teacher = HomePageTeacher(driver_teacher)
        home_page_teacher.click_into_class_by_num(class_num)
        time.sleep(1)
        course_page_teacher = CoursePageTeacher(driver_teacher)
        try:
            assert course_page_teacher.check_student_in_class_member(yaml_config["student_info"]["usr"])
        except AssertionError:
            logger.error(f"断言失败，学生不在老师的{class_num}课堂里，请检查")
            raise AssertionError






