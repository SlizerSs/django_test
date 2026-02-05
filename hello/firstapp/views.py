from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect, HttpResponseNotFound
from .forms import UserForm
from .models import Person


def index(request):
    userform = UserForm()
    people = Person.objects.all()
    return render(request, "firstapp/index.html", {"form": userform, "people": people})


def create(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            klient = Person()
            klient.name = request.POST.get("name")
            klient.age = request.POST.get("age")
            klient.save()
    return HttpResponseRedirect("/")


def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "firstapp/edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиeнт не найден</h2>")


def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиeнт не найден</h2>")


def about(request):
    return HttpResponse("/about")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def products(request, productid=1):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт N {0} Категория: {1}</h2>".format(productid,
                                                            category)
    return HttpResponse(output)


def users(request, id, name):
    id = request.GET .get("id", 1)
    name = request.GET.get("name", "Максим")
    output = "<h2>Пользователь</h2><hЗ>id: {0} Имя: {1}</hЗ >".format(id, name)
    return HttpResponse(output)
