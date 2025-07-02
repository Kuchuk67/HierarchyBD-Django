from django.core.management.base import BaseCommand
from users.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # CustomUser.objects.all().delete()

        # Создаем суперпользователя
        email = input('Enter your e-mail: ')

        user = CustomUser._default_manager.filter(
            email=email,
        )
        if not user:
            user = CustomUser.objects.create(
                email=email,
            )
            password = input('Enter password: ')
            password2 = input('Enter password repeated: ')
            if password == password2:
                user.set_password(password)
                user.is_active = True
                user.is_staff = True
                user.is_superuser = True
                user.save()
            else:
                print('Рasswords do not match')
        else:
            print('This e-mail already exists')

