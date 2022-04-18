from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from account import views
from blog import views as Blogviews
from account import principalViews, teacherViews, studentViews

urlpatterns = [
    path('accounts/principal', principalViews.principal, name='principal'),
    path('accounts/login/',views.loging, name ='loging'),
    path('accounts/loging', views.loging, name = 'loging'),
    path('accounts/doLogin', views.doLogin, name = 'doLogin'),
    path('accounts/get_user_details', views.get_user_details, name = 'get_user_details'),
    path('accounts/logout_user', views.logout_user, name = 'logout_user'),

    path('accounts/results', principalViews.results, name='results'),
    path('accounts/academicYear', principalViews.academicYear, name='academicYear'),
    path('accounts/subjects', principalViews.subjects, name='subjects'),
    path('accounts/classes', principalViews.classes, name='classes'),
    path('accounts/students', principalViews.students, name='students'),
    path('accounts/activate_admission', principalViews.activate_admission, name='activate_admission'),
    path('accounts/deactivate_admission', principalViews.deactivate_admission, name='deactivate_admission'),
    path('accounts/staff', principalViews.staffs, name='staff'),
    path('accounts/posts', Blogviews.posts, name='posts'),

    path('accounts/add_staff', principalViews.add_staff, name='add_staff'),
    path('accounts/add_student', principalViews.add_student, name='add_student'),
    path('accounts/add_class', principalViews.add_class, name='add_class'),
    path('accounts/add_subject', principalViews.add_subject, name='add_subject'),
    path('accounts/edit_result', principalViews.edit_result, name='edit_result'),
    path('accounts/add_academicYear', principalViews.add_academicYear, name='add_academicYear'),

    path('accounts/save_staff', principalViews.save_staff, name='save_staff'),
    path('accounts/save_student', principalViews.save_student, name='save_student'),
    path('accounts/save_class', principalViews.save_class, name='save_class'),
    path('accounts/save_subject', principalViews.save_subject, name='save_subject'),
    path('accounts/save_academic_year', principalViews.save_academic_year, name='save_academic_year'),
    path('accounts/save_result', principalViews.save_result, name='save_result'),

    path('accounts/view_teacher/<int:teacher_id>', principalViews.view_teacher, name='view_teacher'),
    path('accounts/view_student/<int:student_id>', principalViews.view_student, name='view_student'),

    path('accounts/edit_year/<int:year_id>', principalViews.edit_year, name='edit_year'),
    path('accounts/edit_subject/<int:subject_id>', principalViews.edit_subject, name='edit_subject'),
    path('accounts/edit_class/<int:class_id>', principalViews.edit_class, name='edit_class'),
    path('accounts/edit_teacher/<int:teacher_id>', principalViews.edit_teacher, name='edit_teacher'),
    path('accounts/edit_student/<int:student_id>', principalViews.edit_student, name='edit_student'),


    path('accounts/edit_year/edit_year_save', principalViews.edit_year_save, name='edit_year_save'),
    path('accounts/edit_subject/edit_subject_save', principalViews.edit_subject_save, name='edit_subject_save'),
    path('accounts/edit_class/edit_class_save', principalViews.edit_class_save, name='edit_class_save'),
    path('accounts/edit_teacher/edit_teacher_save', principalViews.edit_teacher_save, name='edit_teacher_save'),
    path('accounts/edit_student/edit_student_save', principalViews.edit_student_save, name='edit_student_save'),

    path('accounts/delete_year/<int:year_id>', principalViews.delete_year, name='delete_year'),
    path('accounts/delete_subject/<int:subject_id>', principalViews.delete_subject, name='delete_subject'),
    path('accounts/delete_class/<int:class_id>', principalViews.delete_class, name='delete_class'),
    path('accounts/delete_student/<int:student_id>', principalViews.delete_student, name='delete_student'),

    path('accounts/view_teacher/delete_teacher/<int:teacher_id>', principalViews.delete_teacher, name='delete_teacher'),
    path('accounts/view_student/delete_student/<int:student_id>', principalViews.delete_student, name='delete_student'),

    path('accounts/delete_teacher/<int:teacher_id>', principalViews.delete_teacher, name='delete_teacher'),
    path('accounts/activate_teacher/<int:teacher_id>', principalViews.activate_teacher, name='activate_teacher'),
    path('accounts/activate_student/<int:student_id>', principalViews.activate_student, name='activate_student'),




    path('accounts/teacher', teacherViews.teacher, name='teacher'),



    path('accounts/student', studentViews.student, name='student'),


    # path('getStudents', principalViews.getStudents, name='getStudents'),
]
