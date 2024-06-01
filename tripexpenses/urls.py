from django.urls import path
from tripexpenses import views
from .views import myexpenses
# from tripexpenses.views import 

urlpatterns = [
    path('myexpenses', myexpenses, name='myexpenses'),
]

