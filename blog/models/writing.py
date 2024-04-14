from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from blog.models import category_model
from django.contrib.auth.models import User
from blog.abstract_model import data_abstract_model


class writing_model( data_abstract_model):
    image = models.ImageField(upload_to= "writing_images")
    title = models.CharField( max_length= 30 , blank= False, null= False)
    content = RichTextField()
    slug = AutoSlugField(populate_from = "title", unique=True)
    categories = models.ManyToManyField(category_model, related_name= "writing")
    writer = models.ForeignKey('account.custom_user_model', related_name= "writings", on_delete= models.CASCADE) #writer silindiğinde tüm data uçar

    class Meta():
        db_table = "writing"
        verbose_name_plural = "writings"
        verbose_name = "writing"
    
    def __str__(self):
        return self.title



