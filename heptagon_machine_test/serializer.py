from rest_framework import serializers
from blog_posts import models


class GetPostSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Post
        fields = '__all__'


class GetCommentSerializer(serializers.ModelSerializer):
    class Meta:

        model = models.Comment
        fields = '__all__'