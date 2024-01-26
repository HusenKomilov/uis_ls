from rest_framework.serializers import ModelSerializer
from .models import Author, Category, Tags, Post, ContactUsRequest, ContactUs, FAQ


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('pk', 'title', 'image', 'description', 'content', 'facebook_url', 'twitter_url', 'instagram_url',
                  'pinterest_url', 'is_top')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class ContactUsRequestSerializer(ModelSerializer):
    class Meta:
        model = ContactUsRequest
        fields = '__all__'


class ContactUsSerializer(ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class FAQSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
