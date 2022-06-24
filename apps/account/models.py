from django.db import models
from django.contrib.auth.models import User


# Create your models here.
MEMBERSHIP_CHOICES = (
    ('Premium', 'pre'),
    ('Free', 'free')
)

class Memberhsip(models.Model):
    slug = models.SlugField(null=True, blank=True)
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, default='Free', max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.membership_type
    

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='user_membership')
    name = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True)
    membership = models.ForeignKey(Memberhsip, related_name='user_membership', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
       return self.user.username

class Subscription(models.Model):
    user_membership = models.ForeignKey(Customer, related_name='subscription', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    def __str__(self):
      return self.user_membership.user.username