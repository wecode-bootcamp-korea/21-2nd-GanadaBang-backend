from django.db import models

class User(models.Model):
    email        = models.EmailField(max_length=100, unique=True)
    kakao_id     = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    name         = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'users'