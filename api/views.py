from rest_framework.response import Response
from django.shortcuts import render


def index(request):
    return Response('ciao')
