from django.contrib import admin
from blog.models import category_model,writing_model

admin.site.register(category_model)

@admin.register(writing_model)
class writings_admin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_display = ("title", "writer", "creation_date" , "updated_date")



