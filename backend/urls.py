
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('BlogAPI/',include("blog.urls")),
    path('UserAPI/',include("acoounts.urls")),
    path('',TemplateView.as_view(template_name='index.html'))

    
]
