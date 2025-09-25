from django.db import models
from django.utils import timezone
from user.models import User


class Donation(models.Model):
    PROCESSING_CHOICES = (
        ('queue','Queue'),
        ('processing','Processing'),
        ('finish','Finish')
    )
    status = models.CharField(max_length=30,choices=PROCESSING_CHOICES,default='queue')
    created_at = models.DateField(blank=False)
    expiry_date = models.DateField(blank=False)
    note = models.TextField(null=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='donations')


class DonationApproved(models.Model):
    STATUS_CHOICES = (
        ('processing','Processing'),
        ('accept','Accept'),
        ('reject','Reject')
    )
    donation = models.OneToOneField(Donation,on_delete=models.CASCADE,related_name='donation_approved')
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name= 'donation_approved')
    decision_date = models.DateTimeField(default=timezone.now)
    note = models.TextField(null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='processing'
    )

