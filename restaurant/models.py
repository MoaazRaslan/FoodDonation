from django.db import models
from django.utils import timezone
from user.models import User
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()

    def __str__(self):
        return self.name
    

class Donation(models.Model):
    status = models.CharField()
    expiry_date = models.DateTimeField(blank=False)
    created_at = models.DateTimeField(blank=False)
    note = models.TextField()
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='donations')


class DonationApproved(models.Model):
    class StatusChoices(models.TextChoices):
        AC = 'Accepted'
        PD = 'Pending'
        RJ = 'Rejected'

    donation = models.ForeignKey(Donation,on_delete=models.PROTECT,related_name='donation_approved')
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name= 'donation_approved')
    decision_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PD
    )

