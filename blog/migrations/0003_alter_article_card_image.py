# Generated by Django 3.2.5 on 2021-09-05 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_admission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='card_image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
