from django.db import models

# Create your models here.
class User(models.Model):
    user_nickname = models.CharField(max_length=100, primary_key=True, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)
    
    def _str_(self):
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email}'
    
class Pergunta(models.Model):
    user_pergunta = models.CharField(max_length=100)