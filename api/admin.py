from django.contrib import admin
from .models import Author, Category, Tags, Post, ContactUs, FAQ

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Post)
admin.site.register(ContactUs)
admin.site.register(FAQ)