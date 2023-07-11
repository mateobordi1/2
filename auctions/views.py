from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Producto
from .forms import ProductoForm, OfertaForm


def index(request):
    lista = Producto.objects.all()
    return render(request, "auctions/index.html",{
        "lista": lista
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'auctions/producto.html', {
                "message": form.errors})
            print(form.errors)

    else:
        form = ProductoForm()
        user = request.user
        return render(request, 'auctions/producto.html', {
            "user": user,
            'form': form })

def articulo(request, producto_id):
    producto = Producto.objects.get(pk= producto_id)
    if request.method == "POST":
        if "oferta_" in request.POST:
            form = OfertaForm(request.POST)
            oferta = request.POST['oferta']
            if form.is_valid():
                if int(oferta) > producto.precioactual and int(oferta) >= producto.precioinicial:
                    form.save()
                    producto.precioactual = oferta
                    producto.save()
                    
                else:
                    return HttpResponse("no seas boludo si no le ganas a la otra oferta")
                    
            return HttpResponseRedirect(reverse('articulo', args=[producto_id])  )
        
    else:
        cliente = True
        if producto.vendedor == request.user:
            cliente = False

        return render(request, "auctions/articulo.html", {
            "producto": producto,
            "cliente": cliente
        })