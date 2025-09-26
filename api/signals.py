from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile, NutritionPlan


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_and_plan(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)
        NutritionPlan.objects.get_or_create(user=instance)
