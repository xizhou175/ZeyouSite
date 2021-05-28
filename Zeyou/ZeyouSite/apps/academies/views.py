from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Academy
from .serializers import CreateAcademySerializer
from datetime import date, datetime


class AcademyView(CreateAPIView):
    """
    学生注册
    """
    serializer_class = CreateAcademySerializer


class AcademyUpdateView(APIView):
    def post(self, request):
        data = request.data

        name = data['name']
        source = data['source']
        date_of_purchasing = data['date_of_purchasing']
        hours_of_lecture = data['hours_of_lecture']
        price_overall = data["price_overall"]
        date_of_lecture = data['date_of_lecture']
        product_type = data['product_type']
        product = data['product']
        price_per_hour = data['price_per_hour']
        cur_state = data['cur_state']
        teacher = data['teacher']
        teaching_assistant = data['teaching_assistant']
        sales = data['sales']

        try:
            Academy.objects.filter(id=data["academy_id"]).update(name=name, source=source, price_overall=price_overall, date_of_purchasing=date_of_purchasing,
                                  date_of_lecture=date_of_lecture, hours_of_lecture=hours_of_lecture, product=product,
                                  product_type=product_type, price_per_hour=price_per_hour, cur_state=cur_state, teacher=teacher,
                                  teaching_assistant=teaching_assistant, sales=sales)

            return Response({"message": "Successfully updated", "status": 201})
        except:
            return Response({"message": "Parameters are incomplete and cannot be saved", "status": 400})
