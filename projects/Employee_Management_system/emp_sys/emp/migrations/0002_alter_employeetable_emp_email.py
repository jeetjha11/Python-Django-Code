# Generated by Django 4.2.10 on 2024-02-26 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeetable',
            name='emp_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]