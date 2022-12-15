from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, pre_delete, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Question, Answer


# @receiver(pre_save, sender=Question)
# def create_answer(sender, instance, **kwargs):
#     answers = instance.answers
#     print(answers)
#     # answer = instance.
#     #     raise ValidationError("ERROR")
#
#
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()