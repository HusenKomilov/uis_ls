from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.AuthorList.as_view()),
    path('author/<int:pk>/', views.AuthorDetail.as_view()),

    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),

    path('tags/', views.TagsList.as_view()),
    path('tags/<int:pk>/', views.TagsDetail.as_view()),

    path('post/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view()),

    path('get_question/', views.get_contact_request_view),
    path('create_request_question/', views.ContactUsRequestCreateView.as_view()),

    path('get_faq_view/', views.get_contact_request_view),
    path('create_faq/', views.FAQCreateView.as_view()),

]
