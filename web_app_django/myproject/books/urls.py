from django.urls import path
from .views import book_list
# tu jest defincja endpointów (routów) - '' głowny, bedzie wyswietlał dane z metody book_list zawartej w views
urlpatterns = [
    path('', book_list, name='book_list')
]
