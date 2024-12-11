from django.contrib import admin

from appUser.models import Bookmark, Like, Review

# Register your models here.
admin.site.register(Bookmark)
admin.site.register(Like)
admin.site.register(Review)
