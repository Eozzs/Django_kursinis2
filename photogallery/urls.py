from django.urls import path
from photogallery.views import IndexPageView, IntroPageView, TripListView, trip_photos, photo_comment, GuestBookListView, GuestBookDetailView, register, search

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('intro/', IntroPageView.as_view(), name='intro'),
    path('trips/', TripListView.as_view(), name='trips'),
    path('trip/<int:trip_id>', trip_photos, name='trip'),
    path('photo_comment/<int:photo_id>', photo_comment, name='photo_comment'),
    path('guest_book/', GuestBookListView.as_view(), name='guest_book'),
    path('guest_book_posts/<int:pk>', GuestBookDetailView.as_view(), name='guest_book_posts'),
    path('register/', register, name='register'),
    path('search/', search, name='search')
]
