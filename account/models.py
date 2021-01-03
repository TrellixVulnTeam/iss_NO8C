from django.db import models
from config import settings

# Create your models here.

# 계정


class Account(models.Model):
    user_id = models.CharField(max_length=20)   #아이디
    user_name = models.CharField(max_length=50) #이름
    phone_number = models.CharField(max_length=12)  #전화번호
    email = models.EmailField(max_length=30)    #이메일
    password = models.CharField(max_length=20)  #비밀번호