from django.forms import ModelForm
from django import forms
from blog.models import Admission,Teacher_applications, Sitemessages, article, Schoolinfos, Form1_applications, Form2_4_applications, Lowersixth_applications, Class1_applications, Class2_6_applications, Nursery_applications

class DateInput(forms.DateInput):
    input_type = 'date'
class EmailInput(forms.EmailInput):
    input_type = 'email'
class ChoiceInput(forms.Select):
    input_type = 'choices'
class TextInput(forms.TextInput):
    input_type = 'text'


class PostForm(ModelForm):
    class Meta:
        model = article
        fields = ['title', 'description','card_image','content']

class SchoolinfosForm(ModelForm):
    class Meta:
        model = Schoolinfos
        fields = ['Email1', 'Email2','Number1','Number2','Number3','Pobox','Location1','Location2','Location3']

class Form1_applicationsForm(ModelForm):
    class Meta:
        model = Form1_applications
        fields = ['Full_names', 'Date_of_birth','Gender','Admission_Class','Physical_condition','parent_name','Parent_Contact','Alternative_contact','Parent_Email','Alternative_email','Town_of_Residence','Previous_school','Birth_certificate','Acceptance_slip','Class6_report_card']
        widgets = {
        'Date_of_birth': DateInput(),
        'Parent_Email': EmailInput(),
        'Alternative_email': EmailInput(),
        'Sex': ChoiceInput(),
        'Physical_condition': TextInput(),
        'Admission_Class': ChoiceInput()
        }


class Form2_4_applicationForm(ModelForm):
    class Meta:
        model = Form2_4_applications
        fields = ['Full_names', 'Date_of_birth','Gender','Admission_Class','Physical_condition','parent_name','Parent_Contact','Alternative_contact','Parent_Email','Alternative_email','Town_of_Residence','Previous_school','Birth_certificate','Previous_class_report_card']
        widgets = {
        'Date_of_birth': DateInput(),
        'Parent_Email': EmailInput(),
        'Alternative_email': EmailInput(),
        'Sex': ChoiceInput(),
        'Physical_condition': TextInput(),
        'Admission_Class': ChoiceInput()
        }

class LowerSixth_applicationForm(ModelForm):
    class Meta:
        model = Lowersixth_applications
        fields = ['Full_names', 'Date_of_birth','Gender','Admission_Class','Physical_condition','parent_name','Parent_Contact','Alternative_contact','Parent_Email','Alternative_email','Town_of_Residence','Previous_school','Birth_certificate','GCE_results_slip_or_printed_page_of_results','Form5_report_card']
        widgets = {
        'Date_of_birth': DateInput(),
        'Parent_Email': EmailInput(),
        'Alternative_email': EmailInput(),
        'Sex': ChoiceInput(),
        'Physical_condition': TextInput(),
        'Admission_Class': ChoiceInput()
        }

class Class1_applicationForm(ModelForm):
    class Meta:
        model = Class1_applications
        fields = ['Full_names', 'Date_of_birth','Gender','Admission_Class','Physical_condition','parent_name','Parent_Contact','Alternative_contact','Parent_Email','Alternative_email','Previous_school','Birth_certificate','Nursery_school_certificate','Clinical_card_showing_vaccination_taken']
        widgets = {
        'Date_of_birth': DateInput(),
        'Parent_Email': EmailInput(),
        'Alternative_email': EmailInput(),
        'Sex': ChoiceInput(),
        'Physical_condition': TextInput(),
        'Admission_Class': ChoiceInput()
        }

class Class2_6_applicationForm(ModelForm):
    class Meta:
        model = Class2_6_applications
        fields = ['Full_names', 'Date_of_birth','Gender','Admission_Class','Physical_condition','parent_name','Parent_Contact','Alternative_contact','Parent_Email','Alternative_email','Previous_school','Birth_certificate','Previous_class_report_card']
        widgets = {
        'Date_of_birth': DateInput(),
        'Parent_Email': EmailInput(),
        'Alternative_email': EmailInput(),
        'Sex': ChoiceInput(),
        'Physical_condition': TextInput(),
        'Admission_Class': ChoiceInput()
        }

class Nursery_applicationForm(ModelForm):
    class Meta:
        model = Nursery_applications
        fields = ['Full_names', 'Date_of_birth','Gender','Admission_Class','Physical_condition','parent_name','Parent_Contact','Alternative_contact','Parent_Email','Alternative_email','Birth_certificate','Clinical_card_showing_vaccination_taken']
        widgets = {
        'Date_of_birth': DateInput(),
        'Parent_Email': EmailInput(),
        'Alternative_email': EmailInput(),
        'Sex': ChoiceInput(),
        'Physical_condition': TextInput(),
        'Admission_Class': ChoiceInput()
        }

class Teacher_applicationForm(ModelForm):
    class Meta:
        model = Teacher_applications
        fields = ['Full_names', 'Date_of_birth','Gender','Section_of_choice','Physical_condition','Residence','Contact','Alternative_contact','Email','Alternative_email','Previous_occupation','Hand_written_application','Highest_certificate','CV','National_ID','Picture_4X4_white_or_red_background']
        widgets = {
        'Date_of_birth': DateInput(),
        'Email': EmailInput(),
        'Alternative_email': EmailInput(),
        'Sex': ChoiceInput(),
        'Physical_condition': TextInput(),
        'Section_of_choice': ChoiceInput()
        }
