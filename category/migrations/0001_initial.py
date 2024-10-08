# Generated by Django 5.0.7 on 2024-09-17 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='نام دسته')),
                ('name_fa', models.CharField(max_length=30, unique=True, verbose_name='فارسی نام دسته')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='اسلاگ')),
                ('description', models.TextField(blank=True, max_length=256, verbose_name='توضیحات')),
                ('icon', models.ImageField(blank=True, upload_to='photos/categories/', verbose_name='آیکون')),
                ('branch_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='زیرشاخه دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
    ]
