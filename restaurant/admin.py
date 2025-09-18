from django.contrib import admin
from .models import Restaurant,Donation,DonationApproved

admin.site.register(Restaurant)
admin.site.register(Donation)
admin.site.register(DonationApproved)
