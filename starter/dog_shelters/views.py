from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.

# Generic views 
# TODO: Import generic views 
from django.views import generic

class DogDetailView(generic.DetailView):
    model = models.Dog
    template_name = 'dog_detail.html'
    context_object_name = 'dog'
    

def shelter_list(request):
    shelters = models.Shelter.objects.all()
    context = {'shelters':shelters}
    return render(request, 'shelter_list.html', context)

def shelter_detail(request, pk):
    shelter = get_object_or_404(models.Shelter, pk=pk)
    context = {'shelter':shelter}
    return render(request,'shelter_detail.html',context)
