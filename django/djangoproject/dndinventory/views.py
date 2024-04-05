from django.shortcuts import render

from .models import Character, Inventory, Item

def character(request, id):
    chr = Character.objects.get(pk=id)
    inventories = Inventory.objects.filter(character=chr)
    
    context = {"character": chr, "inventories": inventories}
    return render(request, "character.html", context)
