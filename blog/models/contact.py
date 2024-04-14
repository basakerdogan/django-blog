from django.db import models

class contact_model(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30, blank=False, null=False)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta():
        db_table = "contact"
        verbose_name_plural = "contacts"
        verbose_name = "contact"
    
    def __str__(self):
        return self.email
