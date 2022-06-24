from django.contrib import admin
from apps.account.models import Memberhsip, Customer, Subscription

# Register your models here.
admin.site.register(Memberhsip)
admin.site.register(Customer)
admin.site.register(Subscription)