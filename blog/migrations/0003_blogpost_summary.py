# Generated by Django 5.0.7 on 2024-11-01 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='summary',
            field=models.TextField(blank=True, max_length=128, null=True, verbose_name='خلاصه و موضوع پست'),
        ),
    ]