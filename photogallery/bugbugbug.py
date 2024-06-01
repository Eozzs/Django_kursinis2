from photogallery.models import Trip, Photo, Post
from django.shortcuts import render, get_object_or_404
from django.db.models import Count

reactions = Post.objects.all().values('reaction').annotate(Count('reaction'))
print(reactions)
