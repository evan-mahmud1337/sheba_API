from django.db import models

# Create your models here.


class Gallery(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='gallery/gallery_images/') 

    # def __str__(self):
    #     return self.title
