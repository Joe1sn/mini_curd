from django.db import models

# 被管理对象
class obj(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    brithday = models.DateField()
    id_number = models.CharField(max_length=32)