# Generated by Django 3.0.7 on 2021-01-01 18:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210102_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
