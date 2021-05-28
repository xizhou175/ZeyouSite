from django.db import models
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


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
    date_of_purchasing = models.DateField(db_index=True, null=True)  # timezone?

    # 产品内容
    product = models.CharField(max_length=64, db_index=True, default="")

    # 上课日期
    date_of_lecture = models.DateField(db_index=True, null=True)

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