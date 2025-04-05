from django.shortcuts import render
from django.http import HttpResponse

def mentorados(request):
    return HttpResponse('Estou no mentorados')
