from rest_framework import fields, serializers
from .models import Article


class ArticleSerializers(serializers.ModelSerializer):
   class Meta:
       model = Article
       #fields = ['id', 'title', 'author', 'email']
       fields = '__all__'