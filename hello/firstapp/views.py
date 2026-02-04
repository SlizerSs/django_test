from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

# Create your views here.


def index(request):
    age = 50
    data = ["Ноутбуки", "Принтеры", "Сканеры", "диски", "Шнуры"]
    return render(request, "firstapp/index.html", context={"data": data, "age": age})


def about(request):
    return HttpResponse("/about")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def products(request, productid=1):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт N {0} Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request, id, name):
    id = request.GET .get("id", 1)
    name = request.GET.get("name", "Максим")
    output = "<h2>Пользователь</h2><hЗ>id: {0} Имя: {1}</hЗ >".format(id, name)
    return HttpResponse(output)
