# Generated by Django 3.2.5 on 2021-07-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=50)),
                ('memail', models.CharField(max_length=50)),
                ('mpassword', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=120)),
                ('Last_Name', models.CharField(max_length=120)),
                ('Company_Name', models.CharField(max_length=200)),
                ('Company_Address', models.CharField(max_length=250)),
                ('Communication_Address', models.CharField(max_length=250)),
                ('Mobile_No', models.CharField(max_length=12)),
                ('Landline_No', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=120)),
                ('GST', models.CharField(max_length=120)),
                ('website', models.CharField(max_length=50)),
                ('psw', models.CharField(max_length=10)),
                ('psw_repeat', models.CharField(max_length=10)),
                ('date', models.DateField()),
            ],
        ),
    ]
