from customer.models import *
from api.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date,timedelta,datetime

class ReservationCheckView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({'msg':"success"})
    def post(self,request,*args,**kwargs):
        try:
            start_date=datetime.strptime(request.data.get("start_date"), "%Y-%m-%d").date()
            end_date=datetime.strptime(request.data.get("end_date"), "%Y-%m-%d").date()
            car=Car.objects.get(id=request.data.get("cid"))
            if not Reservation.objects.filter(start_date__gte=start_date,end_date__lte=end_date,car=car):
                amount=((end_date-start_date).days)*car.price
                if request.data.get("pickup")=="1":
                    amount+=1500
                data={
                    'status':'available',
                    'start_date':request.data.get("start_date"),
                    'end_date':request.data.get("end_date"),
                    'price':amount,
                    'cid':car.id
                }
                return Response(data)
            return Response({'msg':"success"})
        except:   
            return Response({'msg':"failed"})

