from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    post_text = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")


    class Meta:
        ordering = ['-created',]

    
    def __str__(self):
        return self.post_text
