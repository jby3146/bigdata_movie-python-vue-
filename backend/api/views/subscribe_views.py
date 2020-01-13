from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Subscribe
from api.models import Profile
from django.contrib.auth.models import User
from api.serializers import SubscribeSerializer
import datetime
import re

@api_view(['GET', 'DELETE'])
def subscribe(request) :

    if request.method == 'GET':
        clkbtn = request.GET.get('clkbtn', None)
        chkperiod = request.GET.get('usernametime', None)
        cancelsub = request.GET.get('cancelsub', None)
        subscribes = Subscribe.objects.all()

        ############### 로그인 시 period 값 확인 ##################
        if chkperiod :
            user = User.objects.all().filter(username= chkperiod)
            
            uid = 0
            for u in user.values_list():
                uid = int(u[0])

            subscribes = subscribes.filter(userid = uid)

            if subscribes :
                today = datetime.datetime.now().date()
 
                period = ""
                for s in subscribes:
                    period = s.period
                    print(period)
                
                period = datetime.datetime.strptime(period, "%Y-%m-%d").date()

                if (period - today).days <= 0 :
                    subscribes.delete()
        ###########################################################

        ###############마이페이지에서 구독 버튼 클릭#################
        if clkbtn :
            user = User.objects.all().filter(username=clkbtn)
            
            uid = 0
            for u in user.values_list():
                uid = int(u[0])

            subscribes = subscribes.filter(userid = uid)

            period = datetime.datetime.now().date() + datetime.timedelta(days=31)
            Subscribe(userid=uid, period=period).save()
            subscribes = subscribes.filter(userid=uid)
        ###########################################################
        
        ####################구독취소 버튼 클릭#######################
        if cancelsub :
            user = User.objects.all().filter(username= cancelsub)
            
            uid = 0
            for u in user.values_list():
                uid = int(u[0])

            subscribes = subscribes.filter(userid = uid)
            subscribes.delete()
        ###########################################################

        serializer = SubscribeSerializer(subscribes, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        subscribe = Subscribe.objects.all()
        subscribe.delete()
        return Response(status=status.HTTP_200_OK)
