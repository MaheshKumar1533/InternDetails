# Generated by Django 4.1.13 on 2024-02-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Internships', '0006_rename_type_internships_intern_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
