# Generated by Django 3.0.8 on 2020-08-01 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rollcallmodule', '0008_remove_attendancerec_attendetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancerec',
            name='attendetails',
            field=models.ForeignKey(db_column='attdateid', default=1, on_delete=django.db.models.deletion.CASCADE, to='rollcallmodule.attendate'),
            preserve_default=False,
        ),
    ]