from django.shortcuts import render

def calculadora(request):
    return render(request, 'calculadora/calculadora.html')
