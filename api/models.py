from django.db import models

# Create your models here.
class ShortLink(models.Model):
    short_code = models.URLField(null=False)
    original_link = models.URLField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    accessed = models.IntegerField(default=0)