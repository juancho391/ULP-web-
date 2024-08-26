from django.shortcuts import render

# Create your views here.
def paginaPrincipal(request):
    return render(request, 'PaginaPrincipal.html')


def pagina1(request):
    return render(request, 'pagina.html')