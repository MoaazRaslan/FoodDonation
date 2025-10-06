from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from .models import DonationApproved,Donation
from django.core.cache import cache

@receiver([post_save,post_delete],sender = Donation)
def delete_donation_cache(sender,instance,**kwargs):
    cache.delete_pattern('*donation_list*')



@receiver(post_save,sender = DonationApproved,dispatch_uid = "send_evaluator_notify")
def send_evaluator_notify(sender,instance,created,**kwargs):
    if created:
        print(f"hi {instance.user.username} you have Donation to approve!")