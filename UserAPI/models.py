from django.db import models


class UserModel(models.Model):
    UserId=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=50)

    def __str__(self):
        return str(self.UserId)