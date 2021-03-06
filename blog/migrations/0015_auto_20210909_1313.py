# Generated by Django 3.2.5 on 2021-09-09 12:13

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210909_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_names', models.CharField(max_length=100)),
                ('Date_of_birth', models.DateField()),
                ('Sex', models.CharField(choices=[('M', ' Male'), ('F', 'Female')], default='M', max_length=100)),
                ('Section_of_choice', models.CharField(choices=[('S', 'SECONDARY'), ('P', 'PRIMARY'), ('N', 'NURSERY')], default='P', max_length=10)),
                ('Physical_condition', models.TextField(blank=True, default='None')),
                ('Residence', models.CharField(blank=True, max_length=100)),
                ('Contact', models.CharField(max_length=15)),
                ('Alternative_contact', models.CharField(blank=True, max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('Alternative_email', models.EmailField(blank=True, max_length=254)),
                ('Previous_occupation', models.CharField(blank=True, max_length=100)),
                ('Hand_written_application', models.FileField(upload_to='media/Teacher_applications/', validators=[blog.validators.validate_file_size])),
                ('Highest_certificate', models.FileField(upload_to='media/Teacher_applications/', validators=[blog.validators.validate_file_size])),
                ('CV', models.FileField(upload_to='media/Teacher_applications/', validators=[blog.validators.validate_file_size])),
                ('National_ID', models.FileField(upload_to='media/Teacher_applications/', validators=[blog.validators.validate_file_size])),
                ('Picture_4X4_white_or_red_background', models.FileField(upload_to='media/Teacher_applications/', validators=[blog.validators.validate_file_size])),
                ('Approved', models.BooleanField(default=False)),
                ('Created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='class1_applications',
            name='Admission_Class',
            field=models.CharField(choices=[('C1', 'Class1')], default='C1', max_length=10),
        ),
        migrations.AlterField(
            model_name='class2_6_applications',
            name='Admission_Class',
            field=models.CharField(choices=[('C6', 'Class6'), ('C5', 'Class5'), ('C4', 'Class4'), ('C3', 'Class3'), ('C2', 'Class2')], default='C2', max_length=10),
        ),
        migrations.AlterField(
            model_name='form1_applications',
            name='Admission_Class',
            field=models.CharField(choices=[('F1', 'Form1')], default='F1', max_length=10),
        ),
        migrations.AlterField(
            model_name='form2_4_applications',
            name='Admission_Class',
            field=models.CharField(choices=[('F4A', 'Form4 Arts'), ('F4S', 'Form4 Science'), ('F3', 'Form3'), ('F2', 'Form2')], default='F2', max_length=10),
        ),
        migrations.AlterField(
            model_name='lowersixth_applications',
            name='Admission_Class',
            field=models.CharField(choices=[('LSA', ' Lower Sixth Arts'), ('LSS', ' Lower Sixth Science')], default='LSA', max_length=10),
        ),
        migrations.AlterField(
            model_name='nursery_applications',
            name='Admission_Class',
            field=models.CharField(choices=[('PN', 'Pre-nursery'), ('N1', 'Nursery1')], default='PN', max_length=10),
        ),
    ]
