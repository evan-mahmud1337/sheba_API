from django.contrib import admin
from video.models import *
# Register your models here.

admin.site.register(CrimeVideos)
admin.site.register(Comment)

admin.site.register(EntertainmentVideos)
admin.site.register(EntertainmentComment)