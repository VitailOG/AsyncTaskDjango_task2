from djoser.signals import user_registered
from django.dispatch import receiver


@receiver(user_registered)
def my_handler(user, request, **kwargs):
    user.is_staff = True
    user.save()
