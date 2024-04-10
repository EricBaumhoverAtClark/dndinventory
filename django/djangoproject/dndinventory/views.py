from django.shortcuts import render

from .models import Character, Inventory, Item

def character(request, id):
    chr = Character.objects.get(pk=id)
    
    context = {"character": chr}
    return render(request, "character.html", context)
