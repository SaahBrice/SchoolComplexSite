# Generated by Django 3.2.5 on 2021-09-09 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210909_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lowersixth_applications',
            name='Admission_Class',
            field=models.CharField(blank=True, choices=[('LSA', ' Lower Sixth Arts'), ('LSS', ' Lower Sixth Science'), ('F4A', 'Form4 Arts'), ('F4S', 'Form4 Science'), ('F3', 'Form3'), ('F2', 'Form2'), ('F1', 'Form1'), ('C6', 'Class6'), ('C5', 'Class5'), ('C4', 'Class4'), ('C3', 'Class3'), ('C2', 'Class2'), ('C1', 'Class1'), ('PN', 'Pre-nursery'), ('N1', 'Nursery1')], default='LSA', max_length=10),
        ),
    ]
