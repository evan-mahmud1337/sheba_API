from rest_framework import serializers
from video.models import CrimeVideos,Comment


class CrimeVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimeVideos
        fields = ['id','video','description','title','view_count','views_by_devices','is_solved','is_onboard'] 


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','video','comments'] 





class EntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimeVideos
        fields = ['id','video','description','title','view_count','views_by_devices','is_solved','is_onboard'] 


class EntertainmentCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','video','comments'] 
