from django.shortcuts import render, redirect, get_object_or_404
from photogallery.models import Trip, Photo, Post
from django.views.generic.base import TemplateView
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages



def my_trips(request):
    trips_count = Trip.objects.all().count()
    trips_list_ordered = Trip.objects.all().order_by('continent')
    
    data = {
        "trips_count": trips_count,
        "trips_list_ordered": trips_list_ordered,
    }

    return render(request, "my_trips.html", context=data)


def trip_photos(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    
    photos_count = trip.photos.count()
    posts_count = trip.posts.count()

    photos_list = Photo.objects.filter(trip=trip)

    reactions = {}

    for photo in photos_list:
        print(photo)
        react = Post.objects.filter(photo=photo).values('reaction').annotate(Count('reaction'))
        reactions[photo] = list(react)
    
    data = {
        'trip': trip,
        'photos_list': photos_list,
        'photos_count': photos_count,
        'posts_count': posts_count,
        'photo': photo,
        'reactions': reactions,
    }

    return render(request, 'trip_photos.html', context=data)


def search(request):
    query = request.GET.get('query')
    search_results = Trip.objects.filter(Q(city__icontains=query) | Q(country__icontains=query) | Q(continent__icontains=query) | Q(date__icontains=query))
    return render(request, 'search.html', {'trips': search_results, 'query': query})


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'User {username} already exists.')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
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
                    
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'User {username} has been successfully registered.')
                    return redirect('login')
        else:
            messages.error(request, 'Passowrds do not match!')
            return redirect('register')
    return render(request, 'registration/register.html')


def validate_password(password):
    errors = []

    # Check for minimum length
    if len(password) < 7:
        errors.append("Password must be at least 8 characters long.")

    # Check for presence of digits
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit.")

    # Check for presence of uppercase letters
    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")

    if errors:
        raise ValueError(errors)



class IndexPageView(TemplateView):
    template_name = "index.html"

class IntroPageView(TemplateView):
    template_name = "intro.html"

class GalleryPageView(TemplateView):
    model = Photo
    template_name = "photo_gallery.html"

class BookPageView(TemplateView):
    template_name = "book.html"
