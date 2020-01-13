from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import create_profile
from api.models import User
from api.models import Profile
from api.serializers import ProfileSerializer


@api_view(['POST','GET'])
def signup(request):

    if request.method == 'POST':
        user = request.data["params"]
        username = user["username"]
        password = user["password"]
        age = user["age"]
        occupation = user["occupation"]
        gender = user["gender"]

        create_profile(username=username, password=password, age=age, occupation=occupation, gender=gender)

        return Response(data=status.HTTP_201_CREATED)
