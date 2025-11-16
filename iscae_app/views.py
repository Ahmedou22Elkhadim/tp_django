from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from iscae_app.models import CustomUser, Item


def say_hello(request):
    return HttpResponse("Say Hello")




def say_hello_json(request):
    return JsonResponse({"Say Hello":"Say Hello"})




def html_page(request):
    users = CustomUser.objects.all()
    return render(request,'index.html',context={"nom":"mohamed","users":users})





def list_item(request):
    items = Item.objects.all()
    return render(request, 'items.html', context={"items":items})




