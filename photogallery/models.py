from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from datetime import date # PERZIURETI
from PIL import Image # PERZIURETI

class Trip(models.Model):
    CONTINENT = (
        ('Asia', 'Asia'), # Raktu pav.
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('South America', 'South America'),
        ('Africa', 'Africa'),
        ('Australia', 'Australia'),
        ('Antarctica', 'Antarctica')
    )

    continent = models.CharField('Continent', max_length=20, default='Asia', choices=CONTINENT)
    country = models.CharField('Country', max_length=50)
    city = models.CharField('City', max_length=50)
    date = models.DateField('Date')
    cover = ResizedImageField(size=[932, 699], upload_to='covers', default='covers/dfimg.jpg', blank=True)

    def __str__(self):
        return f'Trip: {self.city}, {self.country}'

    class Meta:
        verbose_name = 'Trip'
        verbose_name_plural = 'Trips'


class Photo(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True, related_name='photos')
    title = models.CharField('Photo title', max_length=500)
    description = models.TextField('Photo description', max_length=500, null=True, blank=True)
    photo = ResizedImageField(size=[1920, 1440], upload_to='photos', default='photos/dfimg.jpg', blank=True)

    def __str__(self):
        return f'Trip: {self.trip.city}, {self.trip.country} - Photo: {self.title}'
    
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True, related_name='posts')
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, related_name='posts') 
    comment = models.TextField('Comment', max_length=300, null=True, blank=True)
    
    REACTION = (
        ('Love it', 'Love it'),
        ('Amazing!', 'Amazing!'),
        ('Delicious', 'Delicious'),
        ('Hugs', 'Hugs'),
        ('You look great!', 'You look great!'),
    )
    reaction=models.CharField('Reaction', max_length=25, default=None, choices=REACTION, null=True, blank=True) 
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.photo} - Comment: {self.comment}, {self.reaction}'
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class GuestBook(models.Model):
    theme = models.CharField('Theme', max_length=500)
    theme_description = models.TextField('Theme description', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.theme
    
    class Meta:
        verbose_name = 'Guest book'
        verbose_name_plural = 'Guest book'


class GuestPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='guestposts') 
    guestbook = models.ForeignKey(GuestBook, on_delete=models.SET_NULL, null=True, related_name='guestposts')
    post = models.TextField('Comment', max_length=300, null=True, blank=True)
    picture = ResizedImageField(size=[1920, 1440], upload_to='pictures', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post
    
    class Meta:
        verbose_name = 'Guest post'
        verbose_name_plural = 'Guest posts'
