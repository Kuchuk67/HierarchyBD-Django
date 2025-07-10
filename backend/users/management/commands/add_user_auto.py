from getpass import getpass
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from counterparties.models import Counterparties
from users.models import CustomUser
from typing import Any


class Command(BaseCommand):

    def handle(self, *args: Any, **kwargs: Any) -> None:

        # Создаем новую группу
        new_group, created = Group.objects.get_or_create(name="API_access")

        print("Создаем новую группу", new_group, created)

        if created:
            ct = ContentType.objects.get_for_model(Counterparties)
            permission = Permission.objects.create(
                codename="API_access",
                name="Имеет доступ к API",
                content_type=ct,
            )
            new_group.permissions.add(permission)

            print("Подключили пермишены")

        # Создаем суперпользователя
        email = "admin@example.com"

        user = CustomUser._default_manager.filter(
            email=email,
        )
        if not user:
            user_new: CustomUser = CustomUser._default_manager.create(
                email=email,
            )
            user_new.set_password("54321")
            user_new.is_active = True
            user_new.is_staff = True
            user_new.is_superuser = True
            user_new.groups.add(new_group)
            user_new.save()
            print("Admin added")
        else:
            print("This e-mail already exists")
