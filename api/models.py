from django.db import models

# Create your models here.
class ShortLink(models.Model):
    short_code = models.URLField(null=False)
    url = models.URLField(null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    accessCount = models.IntegerField(default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'short_code': self.short_code,
            'url': self.url,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
        }
    
    def stats(self):
        return {
            'id': self.id,
            'short_code': self.short_code,
            'url': self.url,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
            'accessCount': self.accessCount
        }