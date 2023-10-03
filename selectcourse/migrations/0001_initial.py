# Generated by Django 3.0.7 on 2020-06-29 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('CourseId', models.AutoField(primary_key=True, serialize=False)),
                ('CourseName', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'Course',
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('TermId', models.AutoField(primary_key=True, serialize=False)),
                ('TermName', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Term',
            },
        ),
    ]
