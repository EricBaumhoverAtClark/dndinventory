from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


from .models import Character, Inventory, Item

def character(request, id):
    chr = Character.objects.get(pk=id)
    
    context = {"character": chr}
    return render(request, "dndinventory/character.html", context)
    
def home(request):

    if request.user.is_authenticated:
        characters = Character.objects.filter(user=request.user)
    
        context = {"characters": characters}
        return render(request, "dndinventory/home.html", context)
    else:
        return render(request, "dndinventory/home.html", {})


class signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
