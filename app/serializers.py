
from .models import Song
from rest_framework import serializers

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['id','song_title','song_url','song_image','song_data','song_lyrics','song_datetime']