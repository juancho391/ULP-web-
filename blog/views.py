from django.shortcuts import render

# Create your views here.
def paginaPrincipal(request):
    return render(request, 'PaginaPrincipal.html')