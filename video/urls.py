from django.contrib import admin
from django.urls import path
from video.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('crimevideo/<int:pk>', CrimeVideosView.as_view(),name='crime_view'),
    path('crimevideo', CrimeVideosView.as_view(),name='crime_view_item'),
    path('crimevideocomment/<int:video_id>', CommentViewitem.as_view(),name='comment_view'),

    path('entertainmentvideo/<int:pk>', EntertainmentVideosView.as_view(),name='crime_view'),
    path('entertainmentvideo', EntertainmentVideosView.as_view(),name='crime_view_item'),
    path('entertainmentvideocomment/<int:video_id>', CommentViewitem.as_view(),name='comment_view'),
    path('myenterteinment/', MyEntertainmenVideos.as_view(), name="myenterteinmen"),
    path('myvrimevideos/', MyCrimeVideos.as_view(), name="mycrimevideos"),
    path('crime-videos/', CrimeVideoSearchAPIView.as_view(), name='crime_videos_search'),
    path('entertainment-videos/', EntertainmentVideoSearchAPIView.as_view(), name='entertainment_videos_search'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
