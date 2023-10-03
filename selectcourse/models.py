from django.db import models

# Create your models here.

class term(models.Model):
    termid = models.AutoField(primary_key=True)
    termname = models.CharField(max_length=100)

    class Meta:
        db_table='term'

class course(models.Model):
    courseid = models.AutoField(primary_key=True)
    coursename = models.CharField(max_length=200)

    class Meta:
        db_table='course'

class selectcourse(models.Model):
    scid = models.AutoField(primary_key=True)
    term = models.ForeignKey('term', on_delete=models.CASCADE, db_column='termid')
    course = models.ForeignKey('course', on_delete=models.CASCADE, db_column='courseid')
    startdate = models.DateField(null=True)
    enddate = models.DateField(null=True)

    class Meta:
        db_table = 'selectcourse'