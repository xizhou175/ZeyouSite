from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import CreateStudentSerializer
from datetime import date, datetime


class StudentView(CreateAPIView):
    """
    学生注册
    """
    serializer_class = CreateStudentSerializer


class UpdateStudent(APIView):

    def post(self, request):
        data = request.data

        customer_state = data['customer_state']
        source = data['source']
        date_to_add = data['date_to_add']
        graduation_date = data['graduation_date']
        name = data['name']
        gender = data['gender']
        wechat_num = data['wechat_num']
        area = data['area']
        phone = data['phone']
        little_assistant = data["little_assistant"]
        consultant = data["consultant"]
        service_consultant = data["service_consultant"]
        paper_writer = data["paper_writer"]
        identity = int(data['identity'])
        school = data["school"]
        school_type = data["school_type"]
        curriculum_system = data["curriculum_system"]
        curriculum_system_note = data["curriculum_system_note"]
        application_level = data["application_level"]
        major = data["major"]
        target_country = data["target_country"]
        GPA = data["GPA"]
        TOEFL = data["TOEFL"]
        IELTS = data["IELTS"]
        SAT = data["SAT"]
        ACT = data["ACT"]
        GRE = data["GRE"]

        d_add = date(date_to_add[0], date_to_add[1], date_to_add[2])
        d_grad = date(graduation_date[0], graduation_date[1], graduation_date[2])

        try:
            Student.objects.filter(id=data["student_id"]).update(customer_state=customer_state, date_to_add=d_add, graduation_date=d_grad,
                                  source=source, name=name, wechat_num=wechat_num, area=area, phone=phone, gender=gender, identity=identity,
                                  little_assistant=little_assistant, consultant=consultant, service_consultant=service_consultant,
                                  paper_writer=paper_writer, school=school, school_type=school_type,
                                  curriculum_system=curriculum_system, curriculum_system_note=curriculum_system_note,
                                  application_level=application_level, major=major, target_country=target_country,
                                  GPA=GPA, TOEFL=TOEFL, IELTS=IELTS, SAT=SAT, ACT=ACT, GRE=GRE)
        except:
            return Response({"message":"Parameters are incomplete and cannot be saved","status":400})

