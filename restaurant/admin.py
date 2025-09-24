from django.contrib import admin
from .models import Donation,DonationApproved

admin.site.register(Donation)
admin.site.register(DonationApproved)
