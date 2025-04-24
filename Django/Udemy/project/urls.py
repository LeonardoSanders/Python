from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def my_view(request):
    return HttpResponse('Hello World!')

def home(request):
    return HttpResponse('Welcome!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', my_view),
    path('', home),
]
