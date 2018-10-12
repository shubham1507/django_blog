from django.urls import path,include

from django.contrib import admin
from blog import views
admin.autodiscover()

urlpatterns = [

    path('admin/', admin.site.urls),
    #path(r'test/', views.post_list)
    path(r'', include('blog.url')),
]
