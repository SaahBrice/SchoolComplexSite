# Generated by Django 3.2.5 on 2021-08-13 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20210808_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequences',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.academic_years')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mark', models.CharField(blank=True, max_length=100)),
                ('sequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.sequences')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.students')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.subjects')),
            ],
        ),
    ]