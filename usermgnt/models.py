from django.db import models

class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        db_table='user'

