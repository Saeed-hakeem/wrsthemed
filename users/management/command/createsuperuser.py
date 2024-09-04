# users/management/commands/createsuperuser.py
from django.core.management.base import BaseCommand
from users.models import User, Department, UserType, Rank

class Command(BaseCommand):
    help = 'Create a superuser with additional fields'

    def handle(self, *args, **kwargs):
        service_number = input('Service Number: ')
        name = input('Name: ')
        email = input('Email: ')
        password = input('Password: ')

        department_id = input('Department ID: ')
        usertype_id = input('UserType ID: ')
        rank_id = input('Rank ID: ')

        department = Department.objects.get(id=department_id)
        usertype = UserType.objects.get(id=usertype_id)
        rank = Rank.objects.get(id=rank_id)

        User.objects.create_superuser(
            service_number=service_number,
            email=email,
            password=password,
            department=department,
            usertype=usertype,
            rank=rank
        )
