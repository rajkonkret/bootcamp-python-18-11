from django.urls import path
from .views import book_list
from .views import book_create

# tu jest defincja endpointów (routów) - '' głowny, bedzie wyswietlał dane z metody book_list zawartej w views
urlpatterns = [
    path('', book_list, name='book_list'),
    path('new/', book_create, name='book_create'),
]
