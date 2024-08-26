from django.db import models

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    classification = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
