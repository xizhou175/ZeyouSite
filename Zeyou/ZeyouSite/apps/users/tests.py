from django.test import TestCase
from datetime import datetime, timedelta

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.forms.models import model_to_dict
import json

from .models import User, Academy


def create_user_json(username, password, password2, email, phone, department):
    dic = {"password": password, "password2": password2, "email": email, "phone": phone, "username": username,
           "department": department}
    return dic


def login_user_json(username, password):
    dic = {"username": username, "password": password}
    return dic


def update_user_json(username, phone, email, user_id, department):
    dic = {"user_id": user_id, "username": username, "phone": phone, "email": email,
           "department": department}
    return dic


def update_pwd_json(user_id, old_password, new_password, confirmed_password):
    dic = {"user_id": user_id, "old_password": old_password, "new_password": new_password,
           "confirm_password": confirmed_password}
    return dic


def create_student_json(customer_state, source, date_to_add, name, gender, wechat_num, area, phone, little_assistant,
                        consultant, service_consultant, paper_writer, identity, school_type, school, curriculum_system,
                        curriculum_system_note, graduation_date, application_level, major, target_country, GPA, TOEFL,
                        IELTS,
                        SAT, ACT, GRE):
    pass


def create_simple_student(name, little_assistant, consultant, service_consultant, paper_writer):
    dic = {"name": name, "little_assistant": little_assistant, "consultant": consultant,
           "service_consultant": service_consultant, "paper_write": paper_writer}
    return


class UserModelTests(TestCase):

    def test_create_authorize_user(self):
        user1 = create_user_json("zhouxi", "12345", "12345", "xizhou175@gmail.com", "123456", "abcd")
        res = self.client.post(reverse('dataManager:createUser'), user1)
        self.assertEqual(res.status_code, 400)

        user2 = create_user_json("huhuapei", "12345678", "12345678", "huhuapei@gmail.com", "12345", "abcdef")
        res = self.client.post(reverse('dataManager:createUser'), user2)
        self.assertEqual(res.status_code, 201)

        user3 = create_user_json("huhuapei", "12345678", "12345678", "huhuapei@gmail.com", "12345", "abcd")
        res = self.client.post(reverse('dataManager:createUser'), user3)
        self.assertEqual(res.status_code, 400)  # created

        user4 = create_user_json("huhuapei", "12345678", "12345678", "huhuapei@gmail.com", "12345", "abce")
        res = self.client.post(reverse('dataManager:createUser'), user4)
        self.assertEqual(res.status_code, 400)

        login_user2 = login_user_json("huhuapei", "12345678")
        res = self.client.post(reverse('dataManager:authorization'), login_user2)
        self.assertEqual(res.status_code, 200)

        login_user2 = login_user_json("huhuapei", "12345678")
        res = self.client.post(reverse('dataManager:authorization'), login_user2)
        self.assertEqual(res.status_code, 200)

    def test_update_user(self):
        user1 = User(username="xizhou", phone="13774295492", email="xizhou175@gmail.com", department="ab")
        user1.save()

        update_user1 = update_user_json("zhouxi", "123456", "xizhou175@gmail.com", 1, "abc")
        res = self.client.post(reverse('dataManager:userUpdate'), update_user1)
        user1 = User.objects.get(id=1)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(user1.username, "zhouxi")
        self.assertEqual(user1.email, "xizhou175@gmail.com")
        self.assertEqual(user1.phone, "123456")
        self.assertEqual(user1.department, "ab")


    def test_update_pwd(self):
        user1 = User(username="xizhou", phone="13774295492", email="xizhou175@gmail.com",
                     department="ab")
        user1.set_password("12345678")
        user1.save()

        update_user1 = update_pwd_json(1, "12345678", "123456789", "123452789")
        res = self.client.post(reverse('dataManager:pwdUpdate'), update_user1)
        user1 = User.objects.get(id=1)
        self.assertContains(res, "The passwords do not match twice, please re-enter")
        self.assertTrue(user1.check_password("12345678"))

        update_user1 = update_pwd_json(1, "12345678", "123456789", "123456789")
        res = self.client.post(reverse('dataManager:pwdUpdate'), update_user1)
        user1 = User.objects.get(id=1)
        self.assertContains(res, "Successfully modified")
        self.assertTrue(user1.check_password("123456789"))

    '''
    def test_filter_department(self):
        """
        little_assistant = 'Cindy'  'Mary'
        consultant = 'Mary'  'Tony'   'Cindy'
        service_consultant = 'Tony'   'Mary'
        paper_writer = 'Simon'   'Cindy'
        """
        student1 = Student(name='1', little_assistant='Cindy', consultant='Mary', wechat_num="123",
                           service_consultant='Tony', paper_writer='Simon')
        student2 = Student(name='1', little_assistant='Cindy', consultant='Cindy', wechat_num="345",
                           service_consultant='Mary', paper_writer='Simon')
        student1.save()
        student2.save()

        Cindy = User(username='Cindy', phone='123456', password='12345678', email='Cindy@gmail.com', department='abd')
        Mary  = User(username='Mary', phone='123456', password='12345678', email='Cindy@gmail.com', department='abc')
        Tony = User(username='Tony', phone='123456', password='12345678', email='Cindy@gmail.com', department='bc')
        Simon = User(username='Simon', phone='123456', password='12345678', email='Cindy@gmail.com', department='d')
    '''
