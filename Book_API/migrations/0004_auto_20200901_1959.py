# Generated by Django 3.1 on 2020-09-01 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book_API', '0003_auto_20200901_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name_plural': 'Sales'},
        ),
        migrations.RemoveField(
            model_name='sales',
            name='stock',
        ),
    ]
