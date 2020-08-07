from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from heptagon_machine_test import serializer
from blog_posts import models


@api_view(['POST'])
def create_post(request):
    try:
        blog_post = models.Post.objects.create(title=request.data['title'], body=request.data['body'])
        blog_post.save()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_all_posts(request):
    try:
        blog_post = models.Post.objects.all()
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serialized = serializer.GetPostSerializer(blog_post, many=True)

    return Response({'Blog Posts': serialized.data})

@api_view(['GET'])
def get_post(request, id):
    try:
        blog_post = models.Post.objects.get(id=id)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serialized = serializer.GetPostSerializer(blog_post)

    return Response({'Blog Posts': serialized.data})


@api_view(['DELETE'])
def delete_post(request, id):
    try:
        del_post = models.Post.objects.get(id=id)
        del_post.delete()
        blog_post = models.Post.objects.all()
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serialized = serializer.GetPostSerializer(blog_post, many=True)

    return Response({'Blog Posts': serialized.data})


@api_view(['PUT'])
def update_post(request, id):
    try:
        post_update = models.Post.objects.filter(id=id)
        post_update.update(body=request.data['body'])
        blog_post = models.Post.objects.get(id=id)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serialized = serializer.GetPostSerializer(blog_post)

    return Response({'Blog Posts': serialized.data})


@api_view(['GET'])
def get_all_comments(request):
    try:
        blog_comment = models.Comment.objects.all()
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serialized = serializer.GetCommentSerializer(blog_comment, many=True)

    return Response({'Blog Comments': serialized.data})

@api_view(['GET'])
def get_comment(request, id):
    try:
        blog_comment = models.Comment.objects.get(id=id)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serialized = serializer.GetCommentSerializer(blog_comment)

    return Response({'Blog Comments': serialized.data})


@api_view(['GET'])
def get_blog_details(request, id):
    try:
        post = models.Post.objects.get(id=id)
        comments = models.Comment.objects.filter(post_id=id)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    post_serialized = serializer.GetPostSerializer(post)
    comments_serialized = serializer.GetCommentSerializer(comments, many=True)
    return Response({'Post' : post_serialized.data, 'Comments' : comments_serialized.data})


@api_view(['POST'])
def create_comment(request, id):
    try:
        blog_comment = models.Comment.objects.create(author=request.data['author'], body=request.data['body'], post_id=id)
        blog_comment.save()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_comment(request, id, cid):
    try:
        del_comment = models.Comment.objects.get(id=cid)
        del_comment.delete()
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Return blog post with available comments
    try:
        post = models.Post.objects.get(id=id)
        comments = models.Comment.objects.filter(post_id=id)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    post_serialized = serializer.GetPostSerializer(post)
    comments_serialized = serializer.GetCommentSerializer(comments, many=True)
    return Response({'Post' : post_serialized.data, 'Comments' : comments_serialized.data})


@api_view(['PUT'])
def update_comment(request, id, cid):
    try:
        comment_update = models.Comment.objects.filter(id=cid)
        comment_update.update(body=request.data['body'])
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Return blog post with available comments
    try:
        post = models.Post.objects.get(id=id)
        comments = models.Comment.objects.filter(post_id=id)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    post_serialized = serializer.GetPostSerializer(post)
    comments_serialized = serializer.GetCommentSerializer(comments, many=True)
    return Response({'Post': post_serialized.data, 'Comments': comments_serialized.data})