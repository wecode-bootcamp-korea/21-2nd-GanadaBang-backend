from django.db import models

class User(models.Model):
    email        = models.EmailField(max_length=100, unique=True, null=True)
    profile_url  = models.URLField()
    nick_name    = models.CharField(max_length=45)
    kakao_pk     = models.BigIntegerField()
    
    class Meta:
        db_table = 'users'