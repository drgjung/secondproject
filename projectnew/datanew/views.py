from django.shortcuts import render
from django.http import Http404
from datanew.models import Item

def index(request):
    items = Item.objects.exclude(age=60)
    return render(request, 'datanew/index.html', {'items': items,})

def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'datanew/item_detail.html', {'item': item,})
