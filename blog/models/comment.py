from blog.abstract_model import data_abstract_model
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from blog.models import writing_model
from django.utils.html import format_html

class comment_model(data_abstract_model):
    writer = models.ForeignKey('account.custom_user_model', related_name= "comment" , on_delete= models.CASCADE)
    writing = models.ForeignKey(writing_model, related_name= "comment", on_delete= models.CASCADE)
    comment = RichTextField()

    class Meta():
        db_table = "comment"
        verbose_name_plural = "comments"
        verbose_name = "comment"
    
    def __str__(self):
        return self.writer.username
   
    def get_comment(self):
        return format_html(self.comment [:20] + "...")  #admin paneldeki yorum satırı için düzenleme
    
    get_comment.short_description = "comment"