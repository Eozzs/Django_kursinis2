from photogallery.models import Trip, Photo, Post, GuestBook, GuestPost

from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic.base import TemplateView

from django.db.models import Count
from django.db.models import Q
from django.contrib.auth.forms import User

from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from photogallery.forms import GuestPostForm, PostForm
from django.views.decorators.csrf import csrf_protect


class TripListView(generic.ListView):
    model = Trip
    queryset = Trip.objects.all().order_by('continent')
    template_name = 'trips.html'

def trip_photos(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    
    photo_reactions = {}
    
    for photo in trip_photos:
        trip_photos = Photo.objects.filter(trip=trip)
        reactions = Post.objects.filter(photo=photo).values('reaction').annotate(reaction_count=Count('reaction'))
        photo_reactions[photo] = list(reactions)
    
    data = {
        'trip': trip,
        'photo_reactions': photo_reactions,
    }

    return render(request, 'trip.html', context=data)

def photo_comment(request, photo_id):
    #return HttpResponse('veikia')
    if (request.method =='POST'):
        form = PostForm(request.POST)
        if (form.is_valid()):
            post_comment = form.cleaned_data['comment']
            post_reaction= form.cleaned_data['reaction']
            post = Post.objects.create[comment=post_comment, reaction=post_reaction]
            post.save()
    form = PostForm()
    return render(request, 'trip.html', {'form': form})


# SEARCH_TRIP

def search(request):
    query = request.GET.get('query')
    search_results = Trip.objects.filter(Q(city__icontains=query) | Q(country__icontains=query) | Q(continent__icontains=query) | Q(date__icontains=query))
    return render(request, 'search.html', {'trips': search_results, 'query': query})


# PAPRASTI TEMPLATES

class IndexPageView(TemplateView):
    template_name = "index.html"

class IntroPageView(TemplateView):
    template_name = "intro.html"


# SVECIU KNYGA - CLASS-BASED VIEWS

class GuestBookListView(generic.ListView):
    model = GuestBook
    template_name = 'guest_book.html'

class GuestBookDetailView(LoginRequiredMixin, FormMixin, generic.DetailView):
    model = GuestBook
    template_name = 'guest_book_posts.html'
    form = GuestPostForm

    def get_success_url(self):
        return reverse('guest_book_posts', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.game = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(GuestBookDetailView, self).form_valid(form)


# VARTOTOJO REGISTRACIJA

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'User {username} already exists.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Email {email} already exists.')
                    return redirect('register')
                else:
                    try:
                        validate_password(password)
                    except ValueError as e:
                        for error in e.args[0]:
                            messages.error(request, error)
                        return redirect('register')
                    
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'User {username} has been successfully registered.')
                    return redirect('login')
        else:
            messages.error(request, 'Passowrds do not match!')
            return redirect('register')
    return render(request, 'registration/register.html')


def validate_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit.")

    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")

    if errors:
        raise ValueError(errors)
    





    # BANDYMAI >>

    # def get_success_url(self):
    #     return reverse('my_photos', kwargs={'pk': self.object.id})

    # def post(self, request, *args, **kwargs):
    #     photo_id = request.POST['photo_id']
    #     photo = Photo.objects.get(id=photo_id)
    #     self.object = self.get_object()
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form, photo)
    #     else:
    #         return self.form_invalid(form)

    # def form_valid(self, form, photo):
    #     form.instance.photo = photo
    #     form.instance.user = self.request.user
    #     form.save()
    #     return super(TripDetailView, self).form_valid(form)