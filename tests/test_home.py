# -*- coding:utf-8 -*-
# @Time    :2021/3/20 19:16
# @Author  :ChloeeeeWang
# @Email   :403505960@qq.com
# @File    :.py
# @Software:PyCharm


from pages.home import HomePageTeacher,HomePageStudent
from pages.course import CoursePageTeacher
from common.globalmethod import generate_name
from common.yaml_handler import yaml_config


def test_add_class(login_teacher):
    """以老师的形式，创建课程"""
    driver = login_teacher
    home_page = HomePageTeacher(driver)
    class_name = generate_name()
    home_page.create_class(class_name)
    # 断言：是否存在该课程名称的课
    assert home_page.check_class_by_name(class_name)


def test_add_class_num_without_teacher_add_class(login_student, login_teacher):
    """以学生的形式，加入课程"""
    student_usr = yaml_config["student_info"]["usr"]
    student_pwd = yaml_config["student_info"]["pwd"]
    class_num = yaml_config["class_info"]["class_num"]
    driver = login_student
    driver_teacher = login_teacher

    home_page_student = HomePageStudent(driver)
    # WHEN ALREADY EXIST COURSE
    if home_page_student.check_class_by_num(class_num):
        class_name = home_page_student.get_class_name_by_num(class_num)
        home_page_student.quit_class_by_name(class_name, student_pwd)
    home_page_student.add_class(class_num)
    # assert the existence of the course in student-homepage
    assert home_page_student.check_class_by_num(class_num)

    home_page_teacher = HomePageTeacher(driver_teacher)
    # assert the existence of the student in course-member-page
    home_page_teacher.click_into_class_by_num(class_num)
    course_page_teacher = CoursePageTeacher(driver_teacher)
    assert course_page_teacher.check_student_in_class_member(student_usr)


def test_student_quit_class(login_student,login_teacher):
    """ 学生退课 （保证老师允许退课）"""
    pass




