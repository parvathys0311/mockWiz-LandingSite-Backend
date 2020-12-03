import uuid
from decimal import Decimal

from django.db import models
from django.db.models.signals import pre_save
from phone_field import PhoneField

# Create your models here.
from mockWizProject.utils import unique_slug_generator
from pagesApp.models import Function


def randomidgenerator():
    s = str(uuid.uuid4())
    firstSixChars = s[:6]
    return firstSixChars

YEAR_CHOICES = (
    ('','Interviewing Experience'),
    ('lessThanOne','Less than 1 year'),
    ('oneToThree', '1 - 3 years'),
    ('threeToFive', '3 - 5 years'),
    ('fiveToTen', '5 - 10 years'),
    ('moreThanTen', 'More than 10 years')
)

YN_CHOICES = (
    ('Y','Yes'),
    ('N','No'),
)

class Expert(models.Model):
    expertId = models.CharField(max_length=25, default=randomidgenerator, editable=False, primary_key=True, unique=True)
    firstName = models.CharField(max_length=300, default='')
    email = models.EmailField(max_length=50, default='')
    expertiseFunction = models.ForeignKey(Function, on_delete=models.CASCADE, default='')
    yearsInterviewedFor = models.CharField(max_length=12, choices=YEAR_CHOICES, default='')

    lastname = models.CharField(max_length=300, default='')
    phoneNumber = PhoneField(help_text='Contact phone number',default='')
    image = models.ImageField(upload_to='expert/profile',default='./mockWizProject/static/images/default.png')
    jobTitle = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=200, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    linkedInUrl = models.URLField(max_length=400, default='')
    price = models.DecimalField(decimal_places=2, max_digits=6, default=Decimal('49.00'),blank=True, null=True)
    charityName = models.CharField(max_length=300, default='', null=True)
    summary = models.TextField(default='',blank=True)
    noOfBookings = models.IntegerField(default=0,blank=True, null=True)
    slug = models.SlugField(max_length=250,null=True,blank=True)

    approved = models.CharField(max_length=1, choices=YN_CHOICES, default='', null=True,blank=True)
    published = models.CharField(max_length=1, choices=YN_CHOICES, default='', blank=True)
    starKey = models.CharField(max_length=1, choices=YN_CHOICES, default='', blank=True)

    def __str__(self):
        return self.firstName


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Expert)
