from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

DEFAULT_RESULT_CLASS = 1
DEFAULT_RESULT_YEAR = 1

class Academic_years(models.Model):
    id = models.AutoField(primary_key=True)
    start_year = models.DateField()
    end_year = models.DateField()
    objects = models.Manager()

    def __str__(self):
        return str(self.start_year) + '    to    ' + str(self.end_year)


# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_data = ((1, "Principal"), (2, "Teacher"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)





class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Subjects(models.Model):
    id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    classes = models.ManyToManyField(Classes, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    coef = models.CharField(blank=True, max_length=10)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Principal(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()




class Teachers(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    phone1 = models.CharField(blank=True, max_length=100)
    phone2 = models.CharField(blank=True, max_length=100)
    gender = models.CharField(blank=True, max_length=100)
    address = models.TextField()
    profile_pic = models.URLField(blank=True)
    health = models.TextField(blank=True)
    Subjects = models.ManyToManyField(Subjects, blank=True)
    Classes = models.ManyToManyField(Classes, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.admin.username



class Sequences(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(blank=True, max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name





class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    gender = models.CharField(max_length=50)
    profile_pic = models.URLField(blank=True)
    address = models.TextField()
    classs = models.ForeignKey(Classes, on_delete=models.DO_NOTHING, default=1)
    academic_year = models.ForeignKey(Academic_years, on_delete=models.CASCADE)
    health = models.CharField(blank=True, max_length=100)
    phone1 = models.CharField(blank=True, max_length=100)
    phone2 = models.CharField(blank=True, max_length=100)
    parent_name = models.CharField(blank=True, max_length=100)
    previous_school = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.admin.username



class Results(models.Model):
    id = models.AutoField(primary_key = True)
    sequence = models.ForeignKey(Sequences, on_delete = models.CASCADE)
    student = models.ForeignKey(Students, default = 1, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete = models.CASCADE)
    classs = models.ForeignKey(Classes,default = DEFAULT_RESULT_CLASS, on_delete = models.CASCADE)
    mark = models.CharField(blank=True, max_length=100)
    academic_year = models.ForeignKey(Academic_years,default=DEFAULT_RESULT_YEAR, on_delete = models.CASCADE)
    objects = models.Manager()
    def __str__(self):
        return self.mark











# class Attendance(models.Model):
#     # Subject Attendance
#     id = models.AutoField(primary_key=True)
#     subject_id = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)
#     attendance_date = models.DateField()
#     session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()
#
#
# class AttendanceReport(models.Model):
#     # Individual Student Attendance
#     id = models.AutoField(primary_key=True)
#     student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
#     attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
#     status = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()
#
#
# class LeaveReportStudent(models.Model):
#     id = models.AutoField(primary_key=True)
#     student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
#     leave_date = models.CharField(max_length=255)
#     leave_message = models.TextField()
#     leave_status = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()
#
#
# class LeaveReportStaff(models.Model):
#     id = models.AutoField(primary_key=True)
#     staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
#     leave_date = models.CharField(max_length=255)
#     leave_message = models.TextField()
#     leave_status = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()
#
#
# class FeedBackStudent(models.Model):
#     id = models.AutoField(primary_key=True)
#     student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
#     feedback = models.TextField()
#     feedback_reply = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()
#
#
# class FeedBackStaffs(models.Model):
#     id = models.AutoField(primary_key=True)
#     staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
#     feedback = models.TextField()
#     feedback_reply = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()
#
#
#
# class NotificationStudent(models.Model):
#     id = models.AutoField(primary_key=True)
#     student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()
#
#
# class NotificationStaffs(models.Model):
#     id = models.AutoField(primary_key=True)
#     stafff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()
#
#
# class StudentResult(models.Model):
#     id = models.AutoField(primary_key=True)
#     student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
#     subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
#     subject_exam_marks = models.FloatField(default=0)
#     subject_assignment_marks = models.FloatField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()
#
#
# #Creating Django Signals
#
# # It's like trigger in database. It will run only when Data is Added in CustomUser model
#
# @receiver(post_save, sender=CustomUser)
# # Now Creating a Function which will automatically insert data in HOD, Staff or Student
# def create_user_profile(sender, instance, created, **kwargs):
#     # if Created is true (Means Data Inserted)
#     if created:
#         # Check the user_type and insert the data in respective tables
#         if instance.user_type == 1:
#             AdminHOD.objects.create(admin=instance)
#         if instance.user_type == 2:
#             Staffs.objects.create(admin=instance)
#         if instance.user_type == 3:
#             Students.objects.create(admin=instance, course_id=Courses.objects.get(id=1), session_year_id=SessionYearModel.objects.get(id=1), address="", profile_pic="", gender="")
#
#
# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.user_type == 1:
#         instance.adminhod.save()
#     if instance.user_type == 2:
#         instance.staffs.save()
#     if instance.user_type == 3:
#         instance.students.save()
