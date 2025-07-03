from django.core.management.base import BaseCommand
from users.models import CustomUser
from counterparties.models import Counterparties
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from getpass import getpass


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        #CustomUser.objects.all().delete()

        # Создаем новую группу
        new_group, created = Group.objects.get_or_create(name="API_access")

        print("Создаем новую группу", new_group, created)

        if created:
            ct = ContentType.objects.get_for_model(Counterparties)
            #ct = ContentType.objects.get(app_label="app", model="Session")
            #
            permission = Permission.objects.create(
               codename="API_access",
               name="Имеет доступ к API",
               content_type=ct,
            )
            new_group.permissions.add(permission)

            print("Подключили пермишены")

        # Создаем суперпользователя
        email = input('Enter your e-mail: ')

        user = CustomUser._default_manager.filter(
            email=email,
        )
        if not user:
            user = CustomUser._default_manager.create(
                email=email,
            )
            print('Enter password: ')
            # Пароль не отображается при вводе
            password = getpass()
            print('Enter password repeated: ')
            # Пароль не отображается при вводе
            password2 = getpass()
            if password == password2:
                user.set_password(password)
                user.is_active = True
                user.is_staff = True
                user.is_superuser = True
                user.groups.add(new_group)
                user.save()
                print('Admin added')
            else:
                print('Рasswords do not match')
        else:
            print('This e-mail already exists')

