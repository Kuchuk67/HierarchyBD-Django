from django.core.management.base import BaseCommand
from users.models import CustomUser
from counterparties.models import Counterparties
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from getpass import getpass
from partnerships.models import Partnerships
from counterparties.models import Counterparties

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = Counterparties.objects.get(pk=1)
        root = Partnerships.add_root()
        get = lambda node_id: Partnerships.objects.get(pk=node_id)
        
        get(root.pk).add_child(person=user)
        get(root.pk).add_child(person=user)
        get(root.pk).add_child(person=user)
        root2 =  get(root.pk).add_child(person=user)
        get(root2.pk).add_child(person=user)
        get(root2.pk).add_child(person=user)
        