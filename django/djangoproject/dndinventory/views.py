from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.db.models.fields import IntegerField, DecimalField


from .models import Character, Inventory, Item, Equipment

def character(request, id):
    chr = Character.objects.get(pk=id)
    inventory = request.GET.get('inventory',0)
    inventory_id = request.GET.get('inventory_id',0)
    inventory_name = request.GET.get('inventory_name',)
    
    print(inventory)
    #creating
    if inventory_name:
        return create_inventory(request, inventory_name, chr)
    #deleting
    if inventory_id:
        delete_inventory(request, inventory_id)
        return redirect(to="character", id=id)
    if inventory:
        try:
            inventory_object = Inventory.objects.get(pk=inventory)
            
            equipment = request.GET.get('equipment','')
            custom_name = request.GET.get('custom_name', "")
            if equipment:
                equipment_object = Equipment.objects.get(pk=equipment)
            
                new_item = Item(inventory=inventory_object, equipment=equipment_object)
                new_item.save()

            elif custom_name:
                custom_category = request.GET.get('custom_category', "")
                custom_price = request.GET.get('custom_price', 0)
                custom_weight = request.GET.get('custom_weight', 0)

                new_item = Item(inventory=inventory_object, custom_name=custom_name, custom_category=custom_category, custom_price=custom_price, custom_weight=custom_weight)
                new_item.save()
        except:
            # TODO Error
            return redirect(to="home")

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

                if Item._meta.get_field(property).get_internal_type() == IntegerField:
                    property = int(property)

                if Item._meta.get_field(property).get_internal_type() == DecimalField:
                    property = float(property)

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


# creating characters    
def create_character(request, character_name):
    # creates character and should insert into table
    new_character = Character.objects.create(name = character_name, user = request.user)
    return redirect(to="character", id=new_character.pk)
        

# deleting characters
def delete_character(request, character_id):
    if request.user.is_authenticated:
        # deletes character
        Character.objects.filter(pk=character_id).delete()

# creating inventory   
def create_inventory(request, inventory_name, chr):
    # creates inventory and should insert into table
    new_inventory = Inventory.objects.create(character = chr, name = inventory_name)
    return redirect(to="character", id=chr.pk)

def delete_inventory(request, inventory_id):
    if request.user.is_authenticated:
        # deletes inventory
        Inventory.objects.filter(pk=inventory_id).delete()

def user(request):

    if request.user.is_authenticated:
        characters = Character.objects.filter(user=request.user)
        character_id = request.GET.get('character_id',0)
        character_name = request.GET.get('character_name')
        context = {"characters": characters}
        if character_id:
            delete_character(request, character_id)
            return redirect(to="user",)
        if character_name:
            return create_character(request, character_name)
        return render(request, "dndinventory/user.html", context)
    else:
        return redirect(to="home",)

class signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
