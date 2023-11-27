from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    #path("about/", Portfolie.as_view(template_name="portfolie_details.html")),
    #path("about/", Blog.as_view(template_name="blog_details.html")),
    
]
