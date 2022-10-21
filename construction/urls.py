from django.urls import path
from construction.views import home, contact, about


urlpatterns = [
    path('about/', about),
    path('contact/', contact),
    path('', home)
]
