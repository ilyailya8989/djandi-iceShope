from django.urls import path


from .views import index, index1, contact


urlpatterns = [
    path('', index),
    path('index/', index1),
    path('contact/', contact),
]
