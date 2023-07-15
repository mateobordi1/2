from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,  get_object_or_404
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Producto, Comentario, Oferta,  Seguimiento, Ganadores
from .forms import ProductoForm, OfertaForm, ComentarioForm, SeguimientoForm, GanadoresForm


def index(request):
    lista = Producto.objects.all()
    return render(request, "auctions/index.html",{
        "lista": lista
    })

def lista_seguimiento(request):
    lista = Seguimiento.objects.filter(usuario=request.user.id)
    productos = []
    for seguimiento in lista: 
        producto = seguimiento.producto
        productos.append(producto)
    return render(request, "auctions/lista_seguimiento.html",{
        "lista": productos
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
        if "comentario_" in request.POST:
            form = ComentarioForm(request.POST)
            comentario = request.POST['comentario']
            if form.is_valid():
                form.save()
            else:
                    return HttpResponse("el comentario no es valido")

            return HttpResponseRedirect(reverse('articulo', args=[producto_id])  )

        if "q_seguimiento" in request.POST:
            producto = get_object_or_404(Producto, pk=producto_id)
            seguimiento = get_object_or_404(Seguimiento, producto=producto, usuario=request.user)
            seguimiento.en_seguimiento = False

            form = SeguimientoForm(request.POST or None, instance=seguimiento)
            if request.method == "POST" and form.is_valid():
                seguimiento.delete()
                return HttpResponseRedirect(reverse('articulo', args=[producto_id])  )

            else:
                return HttpResponse("no se pudo agregar a la lista de seguimiento")

        if "a_seguimiento" in request.POST:
            producto = get_object_or_404(Producto, pk=producto_id)
            seguimiento, created = Seguimiento.objects.get_or_create(producto=producto, usuario=request.user)
            seguimiento.en_seguimiento = True

            form = SeguimientoForm(request.POST or None, instance=seguimiento)
            if request.method == "POST" and form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('lista_seguimiento' ))

            else:
                return HttpResponse("no se pudo agregar a la lista de seguimiento")
        
        if "terminar" in request.POST:
            producto.vendido = True
            producto.save()
            form = GanadoresForm(request.POST)
            if form.is_valid and producto.precioinicial <= producto.precioactual :
                ganador = Oferta.objects.filter(producto_id=producto.id).latest('id')
                comprador_ganador_id = User.objects.get(id=ganador.comprador_id)
                producto_vendido_id = Producto.objects.get(id=ganador.producto_id)
                ganadores = Ganadores()
                ganadores.usuario_id = comprador_ganador_id
                ganadores.producto_id = producto_vendido_id
                ganadores.save()
                
                return HttpResponseRedirect(reverse('index'))

            return HttpResponse("el producto a sido quitado de la lista activa y no hay ningun ganador de la subasta")
        
    else:
        ganadores = False
        try:
            ganadores= Ganadores.objects.get(producto_id=producto.id)
        except Ganadores.DoesNotExist:
            ganadores = True

        cliente = True
        if producto.vendedor == request.user:
            cliente = False
        comentario = Comentario.objects.filter(producto_id=producto.id)

        try:
            seguimiento = Seguimiento.objects.get(usuario=request.user.id, producto=producto.id)
        except Seguimiento.DoesNotExist:
            seguimiento = True
        return render(request, "auctions/articulo.html", {
            "producto": producto,
            "cliente": cliente,
            "comentarios":comentario, 
            "seguimiento": seguimiento,
            "ganadores": ganadores
        })

def ganadores(request):
    ganadores = Ganadores.objects.all()
    return render(request, "auctions/ganadores.html",{
        "ganadores": ganadores
    })