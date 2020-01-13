from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.template import RequestContext

@api_view(['POST','GET'])
def login(request):

    if request.method == 'POST':
        user = request.data["params"]
        username = user["username"]
        password = user["password"]

        users = User.objects.all().filter(username= username)
        uid = 0

        for u in users.values_list():
            uid = int(u[0])

        users = authenticate(username = username, password = password)
        if users is not None:
            auth.login(request, users)
            return Response(data={"data":200,'uid':uid})
        else:
            return Response(data={"data":False})
