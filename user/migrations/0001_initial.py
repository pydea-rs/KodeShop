# Generated by Django 5.0.7 on 2024-09-17 15:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('fname', models.CharField(max_length=30, verbose_name='نام')),
                ('lname', models.CharField(max_length=30, verbose_name='نام خانوادگی')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='شماره موبایل')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='ایمیل')),
                ('ip', models.CharField(blank=True, max_length=20, verbose_name='IP')),
                ('joining_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='آخرین ورود')),
                ('is_staff', models.BooleanField(default=False, verbose_name='کاربر کارمند')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='کاربر ادمین')),
                ('is_activated', models.BooleanField(default=False, verbose_name='حساب کاربری فعال')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربر ها',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='photos/avatars/')),
                ('last_email_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('debt', models.IntegerField(default=0, verbose_name='بدهی شما')),
                ('postal_code', models.CharField(blank=True, max_length=10, verbose_name='کدپستی')),
                ('province', models.CharField(blank=True, max_length=30, verbose_name='استان')),
                ('city', models.CharField(blank=True, max_length=30, verbose_name='شهرستان')),
                ('address', models.TextField(blank=True, max_length=64, verbose_name='نشانی')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پروفایل',
                'verbose_name_plural': 'پروفایل ها',
            },
        ),
    ]
