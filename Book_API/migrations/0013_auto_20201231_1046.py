# Generated by Django 3.1.2 on 2020-12-31 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book_API', '0012_carousel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='book',
            field=models.CharField(choices=[('Tamil', 'Tamil'), ('English', 'English'), ('Sinhala', 'Sinhala')], max_length=65),
        ),
        migrations.AlterField(
            model_name='sales',
            name='book',
            field=models.CharField(choices=[('Tamil', 'Tamil'), ('English', 'English'), ('Sinhala', 'Sinhala')], max_length=65),
        ),
    ]