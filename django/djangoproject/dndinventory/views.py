from django.shortcuts import render
from django.core.paginator import Paginator

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


from .models import Character, Inventory, Item, Equipment

def character(request, id):
    chr = Character.objects.get(pk=id)
    
    context = {"character": chr}
    return render(request, "dndinventory/character.html", context)
    
def search_equipment(request):
    if request.htmx:
        search = request.GET.get('q')
        page_num = request.GET.get('page', 1)

        if search:
            equipment = Equipment.objects.filter(name__icontains=search) | Equipment.objects.filter(category__icontains=search)
        else:
            equipment = Equipment.objects.none()
        page = Paginator(object_list=equipment, per_page=5).get_page(page_num)

        return render(
          request=request,
          template_name='dndinventory/equipment_results.html',
          context={
              'page': page
          }
        )
    return render(request, 'dndinventory/equipment_search.html')
    
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
    
