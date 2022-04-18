from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from account.models import CustomUser, Teachers, Classes, Subjects, Students, Academic_years, Sequences, Results
from blog.models import Admission
#from .forms import AddStudentForm, EditStudentForm


@login_required()
def activate_admission(request):
    new_admission = Admission.objects.get(pk=1)
    new_admission.open = True
    new_admission.save()
    classs=Classes.objects.all()
    subjects=Subjects.objects.all()
    teachers=Teachers.objects.all()
    students = Students.objects.all()

    context={
    'classs':classs,
    'subjects':subjects,
    'teachers':teachers,
    'students':students,
    }
    return render(request, 'principal/home.html', context)

@login_required()
def deactivate_admission(request):
    new_admission = Admission.objects.get(pk=1)
    new_admission.open = False
    new_admission.save()
    classs=Classes.objects.all()
    subjects=Subjects.objects.all()
    teachers=Teachers.objects.all()
    students = Students.objects.all()

    context={
    'classs':classs,
    'subjects':subjects,
    'teachers':teachers,
    'students':students,
    }
    return render(request, 'principal/home.html', context)

@login_required()
def principal(request):
    classs=Classes.objects.all()
    subjects=Subjects.objects.all()
    teachers=Teachers.objects.all()
    students = Students.objects.all()

    context={
    'classs':classs,
    'subjects':subjects,
    'teachers':teachers,
    'students':students,
    }
    return render(request, 'principal/home.html', context)

@login_required()
def results(request):
    subjects = Subjects.objects.all()
    classes=Classes.objects.all()
    sequences = Sequences.objects.all()
    students = Students.objects.all()
    results = Results.objects.all()

    context={
    'classes':classes,
    'sequences':sequences,
    'subjects':subjects,
    'students':students,
    'results':results,
    }
    return render(request, 'principal/results.html', context)

@login_required()
def staffs(request):
    teachers = Teachers.objects.all()
    context = {
    'teachers':teachers
    }
    return render(request, 'principal/staffs.html', context)

@login_required()
def students(request):
    students = Students.objects.all()
    context ={
    'students':students
    }
    return render(request, 'principal/students.html', context)

@login_required()
def classes(request):
    classes = Classes.objects.all()
    teachers = Teachers.objects.all()
    context = {
    'classes':classes,
    'teachers':teachers,
    }
    return render(request, 'principal/classes.html', context)

@login_required()
def subjects(request):
    subjects = Subjects.objects.all()
    teachers = Teachers.objects.all()
    context = {
    'subjects':subjects,
    'teachers':teachers,
    }
    return render(request, 'principal/subjects.html', context)

@login_required()
def academicYear(request):
    academic_years = Academic_years.objects.all()
    context = {
    'academic_years':academic_years
    }
    return render(request, 'principal/academicYear.html', context)


@login_required()
def add_staff(request):
    classes = Classes.objects.all()
    subjects = Subjects.objects.all()
    context = {
    'classes': classes,
    'subjects': subjects
    }
    return render(request, 'principal/add_staff.html', context)


@login_required()
def add_student(request):
    classes = Classes.objects.all()
    academic_years = Academic_years.objects.all()
    context = {
    'classes': classes,
    'academic_years': academic_years
    }
    return render(request, 'principal/add_student.html', context)

@login_required()
def add_class(request):
    return render(request, 'principal/add_class.html')

@login_required()
def add_subject(request):
    classes = Classes.objects.all()
    context = {
    'classes': classes,
    }
    return render(request, 'principal/add_subject.html', context)

@login_required()
def add_academicYear(request):
    return render(request, 'principal/add_academicYear.html')


@login_required()
def save_staff(request):
    classesDs = Classes.objects.all()
    subjectsDs = Subjects.objects.all()
    if request.method != 'POST':
        messages.error(request, "Invalid Method ")
        return redirect('add_staff')
    else:
        myfiles=request.FILES['myfiles']
        fs = FileSystemStorage()
        filename = fs.save(myfiles.name, myfiles)
        url =fs.url(filename)
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        phone1 = request.POST.get('phone1')
        phone2 = request.POST.get('phone2')
        address = request.POST.get('address')
        subjects = request.POST.getlist('subject')
        classes = request.POST.getlist('classes')
        health = request.POST.get('health')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            new_user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=lastname, first_name=firstname, user_type=2 )
            new_teacher = Teachers()
            new_teacher.phone1 = phone1
            new_teacher.profile_pic = url
            new_teacher.admin = new_user
            new_teacher.phone2 = phone2
            new_teacher.address = address
            new_teacher.health = health
            new_teacher.gender = gender
            new_teacher.save()

            for subject in subjects:
                compare_value = int(subject)
                print(compare_value)
                for subjectsD in subjectsDs:
                    if subjectsD.id == compare_value:
                        here = Subjects.objects.get(pk = subjectsD.id)
                        new_teacher.Subjects.add(here)

            for classe in classes:
                compare_value = int(classe)
                print(compare_value)
                for classesD in classesDs:
                    if classesD.id == compare_value:
                        here = Classes.objects.get(pk = classesD.id)
                        new_teacher.Classes.add(here)
            messages.success(request, "Teacher Added Successfully!")
            return redirect('add_staff')
        except:
            messages.error(request, "Failed to Add Teacher! Enter Correct Credentials or Enter different names")
            return redirect('add_staff')

@login_required()
def save_student(request):
    if request.method != 'POST':
        messages.error(request, "Invalid Method ")
        return redirect('add_student')

    else:
        myfile=request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url =fs.url(filename)
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        parent_name = request.POST.get('parent_name')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        phone1 = request.POST.get('phone1')
        phone2 = request.POST.get('phone2')
        address = request.POST.get('address')
        classes = request.POST.get('class')
        year = request.POST.get('academic_year')
        health = request.POST.get('health')
        email = request.POST.get('email')
        password = request.POST.get('password')
        previous_school = request.POST.get('previous_school')
        print(year)
        print("year")
        print(classes)
        print("class")
        try:
            new_user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=lastname, first_name=firstname, user_type=3 )
            new_student = Students()
            new_student.phone1 = phone1
            new_student.profile_pic = url
            new_student.admin = new_user
            new_student.phone2 = phone2
            new_student.address = address
            new_student.health = health
            new_student.gender = gender
            new_student.previous_school = previous_school
            new_student.parent_name = parent_name
            classhere = Classes.objects.get(pk=classes)
            yearhere = Academic_years.objects.get(pk=year)
            new_student.classs = classhere
            new_student.academic_year = yearhere
            new_student.save()
            messages.success(request, "Student Added Successfully!")
            return redirect('add_student')
        except:
            messages.error(request, "Failed to Add Student! Enter Correct Credentials or Enter different user name")
            return redirect('add_student')

@login_required()
def save_academic_year(request):
    if request.method != 'POST':
        messages.error(request, "Invalid Method ")
        return redirect('add_academicYear')
    else:
        new_yearS = request.POST.get('start')
        new_yearE = request.POST.get('end')
        try:
            create_year = Academic_years()
            create_year.start_year = new_yearS
            create_year.end_year = new_yearE
            create_year.save()
            messages.success(request, "Academic Year Added Successfully!")
            return redirect('add_academicYear')
        except:
            messages.error(request, "Failed to Add Academic Year! Enter Correct Credentials or Enter different Year")
            return redirect('add_academicYear')

    return render(request, 'principal/add_academicYear.html')

@login_required()
def save_result(request):
    return render(request, 'principal/edit_result.html')


@login_required()
def save_class(request):
    if request.method != 'POST':
        messages.error(request, "Invalid Method ")
        return redirect('add_class')
    else:
        new_class = request.POST.get('class_name')
        try:
            create_hall = Classes()
            create_hall.name = new_class
            create_hall.save()
            messages.success(request, "Class Added Successfully!")
            return redirect('add_class')
        except:
            messages.error(request, "Failed to Add Class! Enter Correct Credentials or Enter different class")
            return redirect('add_class')

@login_required()
def save_subject(request):
    classes = Classes.objects.all()
    if request.method != 'POST':
        messages.error(request, "Invalid Method ")
        return redirect('add_subject')
    else:
        name = request.POST.get('subject_name')
        classees = request.POST.getlist('subject_class')
        coef = request.POST.get('coefficient')
        try:
            create_subject = Subjects()
            create_subject.name = name
            create_subject.coef = coef
            create_subject.save()
            for classee in classees:
                compare_value = int(classee)
                print(compare_value)
                for classe in classes:
                    if classe.id == compare_value:
                        here = Classes.objects.get(pk = classe.id)
                        create_subject.classes.add(here)
            messages.success(request, "Subject Added Successfully!")
            return redirect('add_subject')
        except:
            messages.error(request, "Failed to Add Subject! Enter Correct Credentials or Enter different Subject")
            return redirect('add_subject')



@login_required()
def edit_year(request, year_id):
    year = Academic_years.objects.get(id=year_id)
    return render(request,'principal/edit_year.html', {'year':year})

@login_required()
def edit_result(request):
    return render(request, 'principal/edit_result.html')

@login_required()
def edit_subject(request, subject_id):
    subjects = Subjects.objects.get(id=subject_id)
    teachers = Teachers.objects.all()
    classes = Classes.objects.all()
    context = {
    'subjects': subjects,
    'teachers': teachers,
    'classes': classes,
    }
    return render(request,'principal/edit_subject.html', context)

@login_required()
def edit_class(request, class_id):
    classes = Classes.objects.get(id=class_id)
    context = {
    'classes': classes,
    }
    return render(request,'principal/edit_class.html', context)

@login_required()
def edit_teacher(request, teacher_id):
    subjects = Subjects.objects.all()
    teacher = Teachers.objects.get(id=teacher_id)
    classes = Classes.objects.all()
    context = {
    'subjects': subjects,
    'teacher': teacher,
    'classes': classes,
    }
    return render(request,'principal/edit_teacher.html', context)

@login_required()
def edit_student(request, student_id):
    subjects = Subjects.objects.all()
    student = Students.objects.get(id=student_id)
    classes = Classes.objects.all()
    academicYears = Academic_years.objects.all()
    context = {
    'subjects': subjects,
    'student': student,
    'classes': classes,
    'academicYears': academicYears
    }
    return render(request,'principal/edit_student.html', context)


@login_required()
def edit_subject_save(request):
    classes = Classes.objects.all()
    if request.method != 'POST':
        messages.error(request, "Invalid Method ")
        return redirect('edit_year')
    else:
        subject_name = request.POST.get('subject_name')
        coefficient = request.POST.get('coefficient')
        subject_id = request.POST.get('subject_id')
        classees = request.POST.getlist('classe')
        print(subject_name)
        print(subject_id)
        subject = Subjects.objects.get(id=subject_id)
        try:
            subject.classes.clear()
            subject.name = subject_name
            subject.coef = coefficient
            for classee in classees:
                compare_value = int(classee)
                print(compare_value)
                for classe in classes:
                    if classe.id == compare_value:
                        here = Classes.objects.get(pk = classe.id)
                        subject.classes.add(here)
            subject.save()
            messages.success(request, " Subject Edited Successfully!")
            return redirect('subjects')

        except:
            messages.error(request, "Failed to edit  subjects!")
            return redirect('subjects')
@login_required()
def edit_class_save(request):
    if request.method != 'POST':
        messages.error(request, "Invalid Method ")
        return redirect('classes')
    else:
        class_name = request.POST.get('class_name')
        class_id = request.POST.get('class_id')
        classs = Classes.objects.get(id=class_id)
        try:
            classs.name = class_name
            classs.save()
            messages.success(request, " Class Edited Successfully!")
            return redirect('classes')

        except:
            messages.error(request, "Failed to edit  Class!")
            return redirect('classes')

@login_required()
def edit_year_save(request):
    if request.method != 'POST':
        messages.error(request, "Invalid Method ")
        return redirect('edit_year')
    else:
        start = request.POST.get('start')
        end = request.POST.get('end')
        year_id = request.POST.get('year_id')
        year = Academic_years.objects.get(id=year_id)
        try:
            year.start_year = start
            year.end_year = end
            year.save()
            messages.success(request, "Academic Year Edited Successfully!")
            return redirect('academicYear')

        except:
            messages.error(request, "Failed to edit academic year! Try to Enter different year")
            return redirect('academicYear')


@login_required()
def edit_teacher_save(request):
    classes = Classes.objects.all()
    Subs = Subjects.objects.all()
    if request.method != 'POST':
        messages.error(request, "Invalid Method ")
        return redirect('edit_teacher')
    else:
        tmyfiles=request.FILES['myfiles']
        fs = FileSystemStorage()
        filename = fs.save(tmyfiles.name, tmyfiles)
        url =fs.url(filename)
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        phone1 = request.POST.get('phone1')
        phone2 = request.POST.get('phone2')
        address = request.POST.get('address')
        subjects = request.POST.getlist('subject')
        classees = request.POST.getlist('classes')
        health = request.POST.get('health')
        email = request.POST.get('email')
        teacher_id = request.POST.get('teacher_id')
        teacher = Teachers.objects.get(id=teacher_id)
        try:
            adminT = teacher.admin.username
            user = CustomUser.objects.get(username=adminT)
            user.first_name = firstname
            user.last_name = lastname
            user.username = username
            user.email = email
            user.save()
            teacher.phone1 = phone1
            teacher.profile_pic = url
            teacher.phone2 = phone2
            teacher.address = address
            teacher.health = health
            teacher.gender = gender
            teacher.Classes.clear()
            teacher.Subjects.clear()
            for classee in classees:
                compare_value = int(classee)
                print(compare_value)
                for classe in classes:
                    if classe.id == compare_value:
                        here = Classes.objects.get(pk = classe.id)
                        teacher.Classes.add(here)
            for subject in subjects:
                compare_value = int(subject)
                print(compare_value)
                for Sub in Subs:
                    if Sub.id == compare_value:
                        here = Subjects.objects.get(pk = Sub.id)
                        teacher.Subjects.add(here)
            teacher.save()
            messages.success(request, " Teacher Edited Successfully!")
            return redirect('staff')

        except:
            messages.error(request, "Failed to edit  Teacher!")
            return redirect('staff')


@login_required()
def edit_student_save(request):
    if request.method != 'POST':
        messages.error(request, "Invalid Method ")
        return redirect('edit_student')
    else:
        print("trying")
        myfiles=request.FILES['myfile']
        print("ouai")
        fs = FileSystemStorage()
        filename = fs.save(myfiles.name, myfiles)
        url =fs.url(filename)
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        parent_name = request.POST.get('parent_name')
        previous_school = request.POST.get('previous_school')
        gender = request.POST.get('gender')
        phone1 = request.POST.get('phone1')
        phone2 = request.POST.get('phone2')
        address = request.POST.get('address')
        health = request.POST.get('health')
        email = request.POST.get('email')
        academic_year = request.POST.get('academic_year')
        academic_year = Academic_years.objects.get(id=academic_year)
        classe = request.POST.get('class')
        classe = Classes.objects.get(id=classe)
        student_id = request.POST.get('student_id')
        student = Students.objects.get(id=student_id)
        try:
            adminT = student.admin.username
            user = CustomUser.objects.get(username=adminT)
            user.first_name = firstname
            user.last_name = lastname
            user.username = username
            user.email = email
            user.save()
            student.phone1 = phone1
            student.parent_name = parent_name
            student.previous_school = previous_school
            student.academic_year = academic_year
            student.classs = classe
            student.profile_pic = url
            student.phone2 = phone2
            student.address = address
            student.health = health
            student.gender = gender
            student.save()
            messages.success(request, " Student Edited Successfully!")
            return redirect('students')

        except:
            messages.error(request, "Failed to edit  Student!")
            return redirect('students')



@login_required()
def view_teacher(request, teacher_id):
    teacher=Teachers.objects.get(id=teacher_id)
    context={
    'teacher':teacher
    }

    return render(request, 'principal/teacher_stats.html', context)


@login_required()
def view_student(request, student_id):
    student=Students.objects.get(id=student_id)
    context={
    'student':student
    }

    return render(request, 'principal/student_stats.html', context)


@login_required()
def delete_subject(request, subject_id):
    try:
        subject = Subjects.objects.get(id=subject_id)
        subject.delete()
        messages.success(request, "Subject deleted Successfully!")
        return redirect('subjects')
    except:
        messages.error(request, "Failed to delete  subject!")
        return redirect('subjects')


@login_required()
def delete_class(request, class_id):
    try:
        classs = Classes.objects.get(id=class_id)
        classs.delete()
        messages.success(request, "Class deleted Successfully!")
        return redirect('classes')
    except:
        messages.error(request, "Failed to delete  Class!")
        return redirect('classes')


@login_required()
def delete_year(request, year_id):
    try:
        year = Academic_years.objects.get(id=year_id)
        year.delete()
        messages.success(request, "Academic year deleted Successfully!")
        return redirect('academicYear')
    except:
        messages.error(request, "Failed to delete Academic year!")
        return redirect('academicYear')


@login_required()
def delete_teacher(request, teacher_id):
    teacher=Teachers.objects.get(id=teacher_id)
    try:
        adminT = teacher.admin.username
        user = CustomUser.objects.get(username=adminT)
        user.is_active=False
        user.save()
        messages.success(request, " Teacher Deactivated Successfully!")
        return redirect('staff')

    except:
        messages.error(request, "Failed to deactivate  teacher!")
        return redirect('staff')


@login_required()
def delete_student(request, student_id):
    student=Students.objects.get(id=student_id)
    try:
        adminT = student.admin.username
        user = CustomUser.objects.get(username=adminT)
        user.is_active=False
        user.save()
        messages.success(request, " Student Deactivated Successfully!")
        return redirect('students')

    except:
        messages.error(request, "Failed to deactivate  teacher!")
        return redirect('students')


@login_required()
def activate_teacher(request, teacher_id):
    teacher=Teachers.objects.get(id=teacher_id)
    try:
        adminT = teacher.admin.username
        user = CustomUser.objects.get(username=adminT)
        user.is_active=True
        user.save()
        messages.success(request, " Teacher Deactivated Successfully!")
        return redirect('staff')

    except:
        messages.error(request, "Failed to deactivate  teacher!")
        return redirect('staff')


@login_required()
def activate_student(request, student_id):
    student=Students.objects.get(id=student_id)
    try:
        adminT = student.admin.username
        user = CustomUser.objects.get(username=adminT)
        user.is_active= True
        user.save()
        messages.success(request, " Student Deactivated Successfully!")
        return redirect('students')

    except:
        messages.error(request, "Failed to deactivate  teacher!")
        return redirect('students')


# def getStudents(request, class_id):
