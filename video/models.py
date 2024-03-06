from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from rest_framework.validators import ValidationError

# Create your models here.


def validate_video_size(value):
    max_size=300*1024*1024
    file_size=value.size
    if max_size<file_size:
        raise ValidationError('this file is more than 300MB ')
    return value


class CrimeVideos(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE, blank=True, null=True)
    video=models.FileField(upload_to='crime_videos',validators=[FileExtensionValidator(allowed_extensions=['MOV','mp4','mkv','webm']),validate_video_size])
    description=models.TextField(null=True,blank=True)
    title=models.CharField(max_length=300)
    view_count=models.IntegerField(default=0)
    views_by_devices=models.JSONField(default=list, blank=True, null=True)
    is_solved=models.BooleanField(default=False, blank=True, null=True)
    is_onboard=models.BooleanField(default=False, blank=True, null=True)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    video=models.ForeignKey(CrimeVideos,on_delete=models.CASCADE)
    comments=models.CharField(max_length=400)
    def __str__(self):
        return (self.video.title+'-'+self.comments[0:20])
    




class EntertainmentVideos(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    video=models.FileField(upload_to='entertainment_videos',validators=[FileExtensionValidator(allowed_extensions=['MOV','mp4','mkv','webm']),validate_video_size])
    description=models.TextField(null=True,blank=True)
    title=models.CharField(max_length=300)
    view_count=models.IntegerField(default=0)
    views_by_devices=models.JSONField(default=list)
    is_solved=models.BooleanField(default=False)
    is_onboard=models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
class EntertainmentComment(models.Model):
    video=models.ForeignKey(EntertainmentVideos,on_delete=models.CASCADE)
    comments=models.CharField(max_length=400)
    def __str__(self):
        return (self.video.title+'-'+self.comments[0:20])