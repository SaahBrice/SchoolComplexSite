from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from .validators import validate_file_size
# Create your models here.
SEX_CHOICES = (
        ('M', ' Male'),
        ('F', 'Female'),)
LS_CHOICES = (
        ('LSA', ' Lower Sixth Arts'),
        ('LSS', ' Lower Sixth Science'),
        )
F2_4_CHOICES = (

        ('F4A', 'Form4 Arts'),
        ('F4S', 'Form4 Science'),
        ('F3', 'Form3'),
        ('F2', 'Form2'),
        )

F1_CHOICES = (
        ('F1', 'Form1'),
        )

C2_6_CHOICES = (
        ('C6', 'Class6'),
        ('C5', 'Class5'),
        ('C4', 'Class4'),
        ('C3', 'Class3'),
        ('C2', 'Class2'),
        )

C1_CHOICES = (
        ('C1', 'Class1'),
        )

N_CHOICES = (
        ('PN', 'Pre-nursery'),
        ('N1', 'Nursery1'),
        )
TEACHER_CHOICES = (
        ('S', 'SECONDARY'),
        ('P', 'PRIMARY'),
        ('N', 'NURSERY'),
        )

class article(models.Model):
    title = models.CharField(blank=True, max_length=100)
    description = models.CharField(blank=True, max_length=100)
    card_image = models.ImageField(upload_to ="media/")
    content = RichTextUploadingField(blank = True, null = True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Admission(models.Model):
    open = models.BooleanField(default=False)

class Schoolinfos(models.Model):
    Email1 = models.EmailField( blank=True)
    Email2 = models.EmailField( blank=True)
    Number1 = models.CharField(blank=True, max_length=15)
    Number2 = models.CharField(blank=True, max_length=15)
    Number3 = models.CharField(blank=True, max_length=15)
    Pobox = models.CharField(blank=True, max_length=15)
    Location1 = models.CharField(blank=True, max_length=15)
    Location2 = models.CharField(blank=True, max_length=15)
    Location3 = models.CharField(blank=True, max_length=15)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Email1

class Sitemessages(models.Model):
    name = models.CharField(blank=True, max_length=100)
    message = models.CharField(blank=True, max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Form1_applications(models.Model):
    Full_names = models.CharField(blank=False, max_length=100)
    Date_of_birth = models.DateField(blank=False)
    Gender = models.CharField(blank=False, max_length=100, choices = SEX_CHOICES, default = "M")
    Admission_Class = models.CharField(blank=False, max_length=10, choices = F1_CHOICES, default = "F1")
    Physical_condition = models.TextField(blank=True, default = "None")
    parent_name = models.CharField(blank=False, max_length=100)
    Parent_Contact = models.CharField(blank=False, max_length=15)
    Alternative_contact = models.CharField(blank=True, max_length=15)
    Parent_Email = models.EmailField(blank = False)
    Alternative_email = models.EmailField(blank = True)
    Town_of_Residence = models.CharField(blank=True, max_length=15)
    Previous_school = models.CharField(blank=False, max_length=100)
    Birth_certificate = models.FileField(upload_to="media/Student_applications/f1",validators = [validate_file_size])
    Acceptance_slip = models.FileField(upload_to="media/Student_applications/f1", validators = [validate_file_size])
    Class6_report_card  = models.FileField(upload_to="media/Student_applications/f1", validators = [validate_file_size])
    Approved = models.BooleanField(default=False)
    Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Full_names

class Form2_4_applications(models.Model):
    Full_names = models.CharField(blank=False, max_length=100)
    Date_of_birth = models.DateField(blank=False)
    Gender = models.CharField(blank=False, max_length=100, choices = SEX_CHOICES, default = "M")
    Admission_Class = models.CharField(blank=False, max_length=10, choices = F2_4_CHOICES, default = "F2")
    Physical_condition = models.TextField(blank=True, default = "None")
    parent_name = models.CharField(blank=False, max_length=100)
    Parent_Contact = models.CharField(blank=False, max_length=15)
    Alternative_contact = models.CharField(blank=True, max_length=15)
    Parent_Email = models.EmailField(blank = False)
    Alternative_email = models.EmailField(blank = True)
    Town_of_Residence = models.CharField(blank=True, max_length=15)
    Previous_school = models.CharField(blank=False, max_length=100)
    Birth_certificate = models.FileField(upload_to="media/Student_applications/f2_4", validators = [validate_file_size])
    Previous_class_report_card  = models.FileField(upload_to="media/Student_applications/f2_4", validators = [validate_file_size])
    Approved = models.BooleanField(default=False)
    Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Full_names

class Lowersixth_applications(models.Model):
    Full_names = models.CharField(blank=False, max_length=100)
    Date_of_birth = models.DateField(blank=False)
    Gender = models.CharField(blank=False, max_length=100, choices = SEX_CHOICES, default = "M")
    Admission_Class = models.CharField(blank=False, max_length=10, choices = LS_CHOICES, default = "LSA")
    Physical_condition = models.TextField(blank=True, default = "None")
    parent_name = models.CharField(blank=False, max_length=100)
    Parent_Contact = models.CharField(blank=False, max_length=15)
    Alternative_contact = models.CharField(blank=True, max_length=15)
    Parent_Email = models.EmailField(blank = False)
    Alternative_email = models.EmailField(blank = True)
    Town_of_Residence = models.CharField(blank=True, max_length=15)
    Previous_school = models.CharField(blank=False, max_length=100)
    Birth_certificate = models.FileField(upload_to="media/Student_applications/l6", validators = [validate_file_size])
    GCE_results_slip_or_printed_page_of_results = models.FileField(upload_to="media/Student_applications/l6", validators = [validate_file_size])
    Form5_report_card  = models.FileField(upload_to="media/Student_applications/l6", validators = [validate_file_size])
    Approved = models.BooleanField(default=False)
    Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Full_names

class Class1_applications(models.Model):
    Full_names = models.CharField(blank=False, max_length=100)
    Date_of_birth = models.DateField(blank=False)
    Gender = models.CharField(blank=False, max_length=100, choices = SEX_CHOICES, default = "M")
    Admission_Class = models.CharField(blank=False, max_length=10, choices = C1_CHOICES, default = "C1")
    Physical_condition = models.TextField(blank=True, default = "None")
    parent_name = models.CharField(blank=False, max_length=100)
    Parent_Contact = models.CharField(blank=False, max_length=15)
    Alternative_contact = models.CharField(blank=True, max_length=15)
    Parent_Email = models.EmailField(blank = False)
    Alternative_email = models.EmailField(blank = True)
    Previous_school = models.CharField(blank=False, max_length=100)
    Birth_certificate = models.FileField(upload_to="media/Student_applications/cl1", validators = [validate_file_size])
    Nursery_school_certificate = models.FileField(upload_to="media/Student_applications/cl1", validators = [validate_file_size])
    Clinical_card_showing_vaccination_taken  = models.FileField(upload_to="media/Student_applications/cl1", validators = [validate_file_size])
    Approved = models.BooleanField(default=False)
    Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Full_names

class Class2_6_applications(models.Model):
    Full_names = models.CharField(blank=False, max_length=100)
    Date_of_birth = models.DateField(blank=False)
    Gender = models.CharField(blank=False, max_length=100, choices = SEX_CHOICES, default = "M")
    Admission_Class = models.CharField(blank=False, max_length=10, choices = C2_6_CHOICES, default = "C2")
    Physical_condition = models.TextField(blank=True, default = "None")
    parent_name = models.CharField(blank=False, max_length=100)
    Parent_Contact = models.CharField(blank=False, max_length=15)
    Alternative_contact = models.CharField(blank=True, max_length=15)
    Parent_Email = models.EmailField(blank = False)
    Alternative_email = models.EmailField(blank = True)
    Previous_school = models.CharField(blank=False, max_length=100)

    Birth_certificate = models.FileField(upload_to="media/Student_applications/cl2_6", validators = [validate_file_size])
    Previous_class_report_card = models.FileField(upload_to="media/Student_applications/cl2_6", validators = [validate_file_size])
    Approved = models.BooleanField(default=False)
    Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Full_names


class Nursery_applications(models.Model):
    Full_names = models.CharField(blank=False, max_length=100)
    Date_of_birth = models.DateField(blank=False)
    Gender = models.CharField(blank=False, max_length=100, choices = SEX_CHOICES, default = "M")
    Admission_Class = models.CharField(blank=False, max_length=10, choices = N_CHOICES, default = "PN")
    Physical_condition = models.TextField(blank=True, default = "None")
    parent_name = models.CharField(blank=False, max_length=100)
    Parent_Contact = models.CharField(blank=False, max_length=15)
    Alternative_contact = models.CharField(blank=True, max_length=15)
    Parent_Email = models.EmailField(blank = False)
    Alternative_email = models.EmailField(blank = True)
    Previous_school = models.CharField(blank=True, max_length=100)

    Birth_certificate = models.FileField(upload_to="media/Student_applications/nur", validators = [validate_file_size])
    Clinical_card_showing_vaccination_taken  = models.FileField(upload_to="media/Student_applications/nur", validators = [validate_file_size])
    Approved = models.BooleanField(default=False)
    Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Full_names


class Teacher_applications(models.Model):
    Full_names = models.CharField(blank=False, max_length=100)
    Date_of_birth = models.DateField(blank=False)
    Gender = models.CharField(blank=False, max_length=100, choices = SEX_CHOICES, default = "M")
    Section_of_choice = models.CharField(blank=False, max_length=10, choices = TEACHER_CHOICES, default = "P")
    Physical_condition = models.TextField(blank=True, default = "None")
    Residence = models.CharField(blank=True, max_length=100)
    Contact = models.CharField(blank=False, max_length=15)
    Alternative_contact = models.CharField(blank=True, max_length=15)
    Email = models.EmailField(blank = False)
    Alternative_email = models.EmailField(blank = True)
    Previous_occupation = models.CharField(blank=True, max_length=100)
    Hand_written_application = models.FileField(upload_to="media/Teacher_applications/", validators = [validate_file_size])
    Highest_certificate  = models.FileField(upload_to="media/Teacher_applications/", validators = [validate_file_size])
    CV  = models.FileField(upload_to="media/Teacher_applications/", validators = [validate_file_size])
    National_ID  = models.FileField(upload_to="media/Teacher_applications/", validators = [validate_file_size])
    Picture_4X4_white_or_red_background  = models.FileField(upload_to="media/Teacher_applications/", validators = [validate_file_size])
    Approved = models.BooleanField(default=False)
    Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Full_names
