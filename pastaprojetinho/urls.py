
from django.contrib import admin
from django.urls import path, include #ADD o include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('appDjango.urls'))#inclui a urls do app
]

