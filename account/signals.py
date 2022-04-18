from account.models import CustomUser, Principal, Teachers, Students, Subjects, Academic_years, Classes
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender = CustomUser)
def create_user_profiles(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Principal.objects.create(admin = instance)
        if instance.user_type == 2:
            Teachers.objects.create(admin=instance)
        if instance.user_type == 3:
            Students.objects.create(admin=instance)

@reciever(post_save, sender=CustomUser)
def save_user_profile(sender, instance,**kwargs):
    if instance.user_type == 1:
        instance.Principal.save()
    if instance.user_type == 2:
        instance.Teachers.save()
    if instance.user_type == 3:
        instance.Students.save()
