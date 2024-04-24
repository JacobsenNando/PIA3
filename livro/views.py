from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from .models import Livros
from usuarios.models import Usuario
import re


def home(request):
    if request.session.get("usuario"):
        return render(request, "search_page.html")
    else:
        return redirect("/auth/login/?status=2")


def search(request):
    if request.session.get("usuario"):
        busca = request.GET.get("search")
        filtro = request.GET.get("filtro")
        re_busca = r"^[a-zA-Z0-9][a-zA-Z0-9\s]*[a-zA-Z0-9]$"

        if not re.match(re_busca, busca.strip()):
            return HttpResponseForbidden()

        if filtro not in ["titulo", "autor", "genero"]:
            return HttpResponseForbidden()

        resultado = Livros.objects.filter(**{f"{filtro}__icontains": busca})

        paginator = Paginator(resultado, 20)  # Paginar os resultados, 20 por página
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, "home_page.html", {"livros": page_obj})

def ver_livro(request, id):
    if request.session.get("usuario"):
        livro = Livros.objects.get(id=id)
        return render(request, "ver_livro.html", {"livro": livro})


#-------------------------Área administrativa------------------------------#

def cadastrar_livro(request):
    if request.session.get("usuario") and request.session.get("admin"):
        return render(request, "cad_livro.html")
    else:
        return HttpResponseForbidden()

def valida_cadastro_livro(request):
    if request.session.get("usuario") and request.session.get("admin"):
        titulo = request.POST.get("titulo")
        autor = request.POST.get("autor")
        genero = request.POST.get("genero")

        
    else:
        return HttpResponseForbidden()
    
def editar_livro(request, id):
    if request.session.get("usuario") and request.session.get("admin"):
        return render(request, "cad_livro.html")
    else:
        return HttpResponseForbidden()
    
def valida_edicao_livro(request):
    if request.session.get("usuario") and request.session.get("admin"):
        return render(request, "cad_livro.html")
    else:
        return HttpResponseForbidden()

def valida_exclusao_livro(request):
    if request.session.get("usuario") and request.session.get("admin"):
        return render(request, "cad_livro.html")
    else:
        return HttpResponseForbidden()

