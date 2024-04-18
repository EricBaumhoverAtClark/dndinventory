from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


from .models import Character, Inventory, Item, Equipment

def character(request, id):
    chr = Character.objects.get(pk=id)
    inventory = request.GET.get('inventory',0)
    
    print(inventory)
    
    if inventory:
        
        inventory_object = Inventory.objects.get(pk=inventory)
        
        equipment = request.GET.get('equipment','')
        if equipment:
            equipment_object = Equipment.objects.get(pk=equipment)
        
            new_item = Item(inventory=inventory_object, equipment=equipment_object)
            new_item.save()
            
        return redirect(to="character", id=id)
    
    item_id = request.GET.get('item_id', 0)

    if item_id:
        Item.objects.get(pk=item_id).delete()
        return redirect(to="character", id=id)

    
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

def customize_item(request, character_id, item_id, property):
    
    if request.user.is_authenticated:

        character = Character.objects.get(pk=character_id)
        
        if character.user == request.user:

            item = Item.objects.get(pk=item_id)

            if item.inventory.character == character:

                setattr(item, property, request.POST.get(property, getattr(item, property)))
                item.save()



    return redirect(to="character", id=character_id)

def home(request):

    if request.user.is_authenticated:
        characters = Character.objects.filter(user=request.user)
    
        context = {"characters": characters}
        return render(request, "dndinventory/home.html", context)
    else:
        return render(request, "dndinventory/home.html", {})

def user(request):

    if request.user.is_authenticated:
        characters = Character.objects.filter(user=request.user)
    
        context = {"characters": characters}
        return render(request, "dndinventory/user.html", context)
    else:
        return render(request, "dndinventory/user.html", {})

class signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
