"""
==================
Author:Chloeee
Time:2021/3/27 17:43
Contact:403505960@qq.com
==================
"""

from pages.home import HomePageTeacher,HomePageStudent
from pages.course import CoursePageTeacher, CoursePageStudent
from common.yaml_handler import yaml_config
from common.globalmethod import get_current_time,get_current_time_range_list



def test_student_sign_in(login_teacher,login_student):
    """ 学生签到 """
    class_num = yaml_config["class_info"]["class_num"]
    driver_student = login_student
    driver_teacher = login_teacher

    home_page_teacher = HomePageTeacher(driver_teacher)
    home_page_teacher.click_into_class_by_num(class_num)
    # 老师发起签到
    course_page_teacher = CoursePageTeacher(driver_teacher)
    sign_num = course_page_teacher.raise_attendance()   # 获得签到码
    # 学生根据签到码签到
    home_page_student = HomePageStudent(driver_student)
    home_page_student.click_into_class_by_num(class_num)

    course_page_student = CoursePageStudent(driver_student)
    course_page_student.to_sign_in(sign_num)
    now_time = get_current_time()
    time_validate_range_list = get_current_time_range_list(now_time)


    get_date,get_time = course_page_student.get_sign_in_time()
    state = course_page_student.get_sign_in_state()
    member_count = course_page_teacher.get_sign_in_member_count()
    assert state == "出勤" and 1 == member_count and get_time in time_validate_range_list

