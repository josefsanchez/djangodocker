"""
    Vistas de programa de boletos de aerolínea
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def calcular (request):
    if request.method == "POST":
        clase = request.POST["clase"]
    response = HttpResponse("Here's the text of the Web page.")
    
@login_required
def boleto_view (request):
        return render(request, 'boleto.html')


