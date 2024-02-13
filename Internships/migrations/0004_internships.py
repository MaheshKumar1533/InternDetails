# Generated by Django 4.2.6 on 2024-02-13 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Internships', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='internships',
            fields=[
                ('internId', models.AutoField(primary_key=True, serialize=False)),
                ('internshipName', models.CharField(max_length=30)),
                ('sdate', models.DateField()),
                ('edate', models.DateField()),
                ('type', models.CharField(max_length=30)),
                ('rollno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Internships.student')),
            ],
        ),
    ]