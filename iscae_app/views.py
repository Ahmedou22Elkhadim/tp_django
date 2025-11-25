from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from iscae_app.models import CustomUser, Item
from django.shortcuts import redirect

def say_hello(request):
    return HttpResponse("Say Hello")


def say_hello_json(request):
    return JsonResponse({"Say Hello":"Say Hello"})


def html_page(request):
    users = CustomUser.objects.all()
    return render(request,'index.html',context={"nom":"mohamed","users":users})

def create_item(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')

        Item.objects.create(name=name, description=description)

        return redirect('list_item')  

    return render(request, 'create_item.html')


def list_item(request):
    items = Item.objects.all()
    return render(request, 'items.html', context={"items":items})

def edit_item(request , id) :
    items = Item.objects.get(id = id)
    if request.method == "POST":
        items.name = request.POST.get('name')
        items.description = request.POST.get('description')
        items.save()
        return redirect('list_item')
    else :
        # items = Item(inistance=items)
       return render(request, 'edit_item.html', context = {'item' : items})
    
def supprimer_item(request , id) :
    items = Item.objects.get(id=id)
    # if request.method == "GET":
    items.delete()
    return redirect('list_item')






