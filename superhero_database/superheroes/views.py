from django.shortcuts import render
from .models import Superhero
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .forms import SuperheroForm


# Initial listing view
def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)


# Display view for details
def detail(request, superhero_id):
    context = {}
    context["superhero"] = Superhero.objects.get(id=superhero_id)
    return render(request, 'superheroes/detail.html', context)


# Create view for details
# Refactored to use forms
def create(request):
    context = {}
    form = SuperheroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('superheroes:index'))

    context['form'] = form
    return render(request, 'superheroes/create.html', context)


# update view for details
# Refactored to use forms
def update(request, superhero_id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    superhero_obj = get_object_or_404(Superhero, id=superhero_id)

    # pass the object as instance in form
    form = SuperheroForm(request.POST or None, instance=superhero_obj)

    # save the data from the form and return
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('superheroes:index'))

    # add form dictionary to context
    context["form"] = form
    return render(request, 'superheroes/update.html', context)


# delete view for details
# Refactored to use forms
def delete(request, superhero_id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    superhero_obj = get_object_or_404(Superhero, id=superhero_id)

    if request.method == "POST":
        # delete object
        superhero_obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect(reverse('superheroes:index'))
    context['superhero'] = superhero_obj
    return render(request, 'superheroes/delete.html', context)
