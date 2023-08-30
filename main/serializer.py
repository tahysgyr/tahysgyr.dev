from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title','date','user','description','tag')