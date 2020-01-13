from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import create_profile
from api.models import Profile
from django.contrib.auth.models import User
from api.serializers import ProfileSerializer
from django.db import connection

@api_view(['POST','GET'])
def user_update(request):

    if request.method == 'POST':
        pp = Profile.objects.all()
        update = request.data["params"]
        username = update["username"]
        age = update["age"]
        gender = update["gender"]
        occupation = update["occupation"]

        user = User.objects.all().filter(username= username)

        uid = 0
        for u in user.values_list():
            uid = int(u[0])

        profile = Profile.objects.all().filter(id=uid)

        if age :
            profile.update(age=age)
        if gender :
            profile.update(gender=gender)
        if occupation :
            profile.update(occupation=occupation)

        return Response(status=status.HTTP_201_CREATED)
