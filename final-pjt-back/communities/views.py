from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework import status

# Create your views here.
@api_view(['POST','GET'])
def create_or_read_articles(request):
    if request.method=='POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='GET':
        articles=Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

@api_view(['PUT','DELETE'])
def update_or_delete_article(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method=='DELETE':
        article.delete()
        data = {
            "delete": f"article {article_pk} is deleted"
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method=='PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_comment(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    user = request.user
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def update_or_delete_comment(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    
    if request.method=='DELETE':
        comment.delete()
        data = {
            "delete": f"comment {comment_pk} is deleted"
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method=='PUT':
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)