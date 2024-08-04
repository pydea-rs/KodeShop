# Generated by Django 3.2.25 on 2024-08-04 06:02

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
            ],
            options={
                'verbose_name': 'دسته',
                'verbose_name_plural': 'دسته ها',
            },
        ),
    ]