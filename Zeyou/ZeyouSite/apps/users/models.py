from django.db import models
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# four departments: a:小助手  b:文案   c:顾问   d:助教
class User(AbstractUser):
    username = models.CharField(max_length=64, db_index=True, unique=True)
    phone = models.CharField(max_length=64, db_index=True, unique=True)
    email = models.EmailField(unique=True, db_index=True)
    password = models.CharField(max_length=128)
    department = models.CharField(max_length=128)

    #student = models.ManyToManyField(to='Student')
    #academy = models.ManyToManyField(to='Academy')

    def __str__(self):
        return '<User {}>'.format(self.username)


# student=Student(name="xizhou", gender="M", phone="123456", identity=0, graduation_date="2021-05-01")
class Student(models.Model):
    # 客户状态
    customer_state = models.IntegerField(db_index=True, default=0)

    # 客户来源
    source = models.CharField(max_length=64, db_index=True, default="")

    # 加好友日期
    date_to_add = models.DateField(db_index=True, default=timezone.now())  # timezone?

    # 姓名
    name = models.CharField(max_length=64, db_index=True, unique=True)

    # 性别
    gender = models.CharField(max_length=1, db_index=True, default="")

    # 微信号
    wechat_num = models.CharField(max_length=64, db_index=True, unique=True, default="")

    # 地区
    area = models.CharField(max_length=64, db_index=True, default="")

    # 电话号码
    phone = models.CharField(max_length=64, db_index=True, default="")

    # 所属小助手
    little_assistant = models.CharField(max_length=64, db_index=True, default="")

    # 所属顾问
    consultant = models.CharField(max_length=64, db_index=True, default="")

    # 所属服务顾问
    service_consultant = models.CharField(max_length=64, db_index=True, default="")

    # 所属文案
    paper_writer = models.CharField(max_length=64, db_index=True, default="")

    # 客户身份 家长or学生
    identity = models.IntegerField(default=0)

    # 学校类型
    school_type = models.CharField(max_length=64, db_index=True, default="")

    # 学校名
    school = models.CharField(max_length=64, db_index=True, default="")

    # 课程体系
    curriculum_system = models.CharField(max_length=64, db_index=True, default="")

    # 课程体系备注
    curriculum_system_note = models.CharField(max_length=64, db_index=True, default="")

    # 毕业时间
    graduation_date = models.DateField(db_index=True, default=timezone.now())

    # 申请层级
    application_level = models.CharField(max_length=64, db_index=True, default="")

    # 专业方向
    major = models.CharField(max_length=64, default="")

    # 目标国家
    target_country = models.CharField(max_length=64, default="")

    # 成绩
    GPA = models.CharField(max_length=64, default="")
    TOEFL = models.CharField(max_length=64, default="")
    IELTS = models.CharField(max_length=64, default="")
    SAT = models.CharField(max_length=64, default="")
    ACT = models.CharField(max_length=64, default="")
    GRE = models.CharField(max_length=64, default="")

    def __str__(self):
        return '<Student {}>'.format(self.name)


class Academy(models.Model):
    # 姓名
    name = models.CharField(max_length=64, db_index=True, unique=False, default="")

    # 客户来源
    source = models.CharField(max_length=64, db_index=True, default="")

    # 产品类型
    product_type = models.CharField(max_length=64, db_index=True, default="")

    # 分配助教
    teaching_assistant = models.CharField(max_length=64, db_index=True, default="")

    # 所属销售人员
    sales = models.CharField(max_length=64, db_index=True, default="")

    # 授课老师
    teacher = models.CharField(max_length=64, db_index=True, default="")

    # 购买时间
    date_of_purchasing = models.DateField(db_index=True, default=datetime.utcnow)  # timezone?

    # 产品内容
    product = models.CharField(max_length=64, db_index=True, default="")

    # 上课日期
    date_of_lecture = models.DateField(db_index=True, default=datetime.utcnow)

    # 预计课时
    hours_of_lecture = models.IntegerField(default=0)

    # price/hour
    price_per_hour = models.IntegerField(default=0)

    # price
    price_overall = models.IntegerField(default=0)

    # 推进状态
    cur_state = models.CharField(max_length=64, db_index=True, default="")

    #student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return '<Academy {}>'.format(self.name)
