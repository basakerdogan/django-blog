from django.contrib import admin
from blog.models import category_model,writing_model,comment_model

admin.site.register(category_model)

@admin.register(writing_model)
class writings_admin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_display = ("title", "writer","creation_date" , "updated_date")

@admin.register(comment_model)
class comments_admin(admin.ModelAdmin):
    search_fields = ("writer__username", "writing__id") # writer__username :writer user name i almak için yaptık
    list_display = ("writer","creation_date","updated_date", "get_comment")
    
   




