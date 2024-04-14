from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class custom_user_model(AbstractUser):
    avatar = models.ImageField(upload_to= "avatar/", blank=True, null=True)
       
    class Meta():
        db_table = "user"
        verbose_name_plural = "users"
        verbose_name = "user"
    
    def __str__(self):
        return self.username


    
