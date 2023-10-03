# Generated by Django 3.0.7 on 2020-07-13 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('selectcourse', '0007_auto_20200709_0542'),
        ('rollcallmodule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendancerec',
            fields=[
                ('attendanceID', models.AutoField(primary_key=True, serialize=False)),
                ('attdatetime', models.DateTimeField(null=True)),
                ('attendance', models.BooleanField(default=True)),
                ('studentphoto', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'attendancerec',
            },
        ),
        migrations.CreateModel(
            name='attendate',
            fields=[
                ('attdateid', models.AutoField(primary_key=True, serialize=False)),
                ('attdate', models.DateTimeField()),
                ('TSelectCourse', models.ForeignKey(db_column='scid', on_delete=django.db.models.deletion.CASCADE, to='selectcourse.TSelectCourse')),
            ],
            options={
                'db_table': 'attendate',
            },
        ),
        migrations.CreateModel(
            name='studentrec',
            fields=[
                ('stuid', models.AutoField(primary_key=True, serialize=False)),
                ('stunum', models.CharField(max_length=50)),
                ('stuname', models.CharField(max_length=50)),
                ('TSelectCourse', models.ForeignKey(db_column='scid', on_delete=django.db.models.deletion.CASCADE, to='selectcourse.TSelectCourse')),
            ],
            options={
                'db_table': 'studentrec',
            },
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.AddField(
            model_name='attendancerec',
            name='attendetails',
            field=models.ForeignKey(db_column='attdateid', on_delete=django.db.models.deletion.CASCADE, to='rollcallmodule.attendate'),
        ),
        migrations.AddField(
            model_name='attendancerec',
            name='course',
            field=models.ForeignKey(db_column='courseid', on_delete=django.db.models.deletion.CASCADE, to='selectcourse.Tcourse'),
        ),
        migrations.AddField(
            model_name='attendancerec',
            name='studetails',
            field=models.ForeignKey(db_column='stuid', on_delete=django.db.models.deletion.CASCADE, to='rollcallmodule.studentrec'),
        ),
        migrations.AddField(
            model_name='attendancerec',
            name='term',
            field=models.ForeignKey(db_column='termid', on_delete=django.db.models.deletion.CASCADE, to='selectcourse.Tterm'),
        ),
    ]