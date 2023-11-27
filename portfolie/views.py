from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    person = Person.objects.all()
    services = Services.objects.all()
    project = Project.objects.all()
    testimonial = Testimonial.objects.all()
    blog = Blog.objects.all()
    
    contexte = {
        'person': person ,
        'services': services ,
        'project': project , 
        'testimonial': testimonial , 
        'blog': blog ,


        }
    return render(request,'index.html', contexte)