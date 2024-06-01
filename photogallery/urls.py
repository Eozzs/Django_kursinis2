from django.urls import path
from photogallery.views import IndexPageView, my_trips, trip_photos, IntroPageView, BookPageView, GalleryPageView, search, register

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('my_trips/', my_trips, name='my_trips'),
    path('my_trips/<int:trip_id>', trip_photos, name='trip_photos'),
    #path('photo-gallery/', GalleryPageView.as_view(), name='photo_gallery'),
    path('intro/', IntroPageView.as_view(), name='intro'),
    path('book/', BookPageView.as_view(), name='book'),
    path('search/', search, name='search'),
    path('register/', register, name='register'),
]