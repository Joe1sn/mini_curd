from django.db import models

# 管理账户登录
class user(models.Model):
    username = models.CharField(max_length=20)  # 用户名
    password = models.CharField(max_length=32)  # sha1(密码)

# 被管理对象
class obj(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    brithday = models.DateTimeField()
    id_number = models.CharField(max_length=32)