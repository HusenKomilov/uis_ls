from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from .models import Author, Category, Post, Tags, ContactUsRequest, FAQ
from .serializers import AuthorSerializer, CategorySerializer, TagsSerializer, PostSerializer, \
    ContactUsRequestSerializer, FAQSerializer


class AuthorList(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagsList(ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class TagsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_contact_request_view(request):
    contact = ContactUsRequest.objects.all()
    serializers = ContactUsRequestSerializer(contact, many=True)
    context = {
        'status_code': 200,
        'data': serializers.data
    }
    return Response(context, request)


class ContactUsRequestCreateView(CreateAPIView):
    queryset = ContactUsRequest.objects.all()
    serializer_class = CategorySerializer


@api_view(['GET'])
def get_faq_view(request):
    faq = FAQ.objects.all()
    serializers = FAQSerializer(faq, many=True)
    context = {
        'status_code': 200,
        'data': serializers.data
    }
    return Response(context)


class FAQCreateView(CreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = (IsAdminUser,)
