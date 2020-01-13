from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Question , Profile
from django.contrib.auth.models import User
from api.serializers import QuestionSerializer
import datetime

@api_view(['POST','GET'])
def question(request):

    if request.method == 'GET':
        name = request.GET.get('name' , request.GET.get('name',None))
        title = request.GET.get('title' , request.GET.get('title',None))
        content = request.GET.get('content' , request.GET.get('content',None))
        replys = request.GET.get('replys' , request.GET.get('replys',None))
        times = request.GET.get('times' , request.GET.get('times',None))
        questions = Question.objects.all()

        if name:
            questions = questions.filter(name=name)

        if title:
            questions = questions.filter(title=title)

        if content:
            questions = question.filter(content=content)

        if replys:
            questions = question.filter(replys=replys)

        serializer = QuestionSerializer(questions, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        ques = request.data["params"]
        name = ques["name"]
        title = ques["title"]
        content = ques["content"]
        replys = ques["replys"]
        times = datetime.datetime.now().date() + datetime.timedelta(days=31)

        Question(name = name, title = title, content = content , replys=replys , times=times).save()

        return Response(data=status.HTTP_201_CREATED)
