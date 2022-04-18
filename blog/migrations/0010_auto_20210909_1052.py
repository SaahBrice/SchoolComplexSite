# Generated by Django 3.2.5 on 2021-09-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210909_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class1_applications',
            name='Sex',
            field=models.CharField(choices=[('M', ' Male'), ('F', 'Female')], default='M', max_length=100),
        ),
        migrations.AlterField(
            model_name='class2_6_applications',
            name='Sex',
            field=models.CharField(choices=[('M', ' Male'), ('F', 'Female')], default='M', max_length=100),
        ),
        migrations.AlterField(
            model_name='form1_applications',
            name='Sex',
            field=models.CharField(choices=[('M', ' Male'), ('F', 'Female')], default='M', max_length=100),
        ),
        migrations.AlterField(
            model_name='form2_4_applications',
            name='Sex',
            field=models.CharField(choices=[('M', ' Male'), ('F', 'Female')], default='M', max_length=100),
        ),
        migrations.AlterField(
            model_name='lowersixth_applications',
            name='Sex',
            field=models.CharField(choices=[('M', ' Male'), ('F', 'Female')], default='M', max_length=100),
        ),
        migrations.AlterField(
            model_name='nursery_applications',
            name='Sex',
            field=models.CharField(choices=[('M', ' Male'), ('F', 'Female')], default='M', max_length=100),
        ),
    ]