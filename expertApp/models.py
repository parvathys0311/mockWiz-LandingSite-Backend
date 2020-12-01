from django.db import models

# Create your models here.
from pagesApp.models import Function

YEAR_CHOICES = (
    ('','Interviewing Experience'),
    ('lessThanOne','Less than 1 year'),
    ('oneToThree', '1 - 3 years'),
    ('threeToFive', '3 - 5 years'),
    ('fiveToTen', '5 - 10 years'),
    ('moreThanTen', 'More than 10 years')
)

class Expert(models.Model):
    expertId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=300, default='')
    email = models.EmailField(max_length=50, default='')
    expertiseFunction = models.ForeignKey(Function, on_delete=models.CASCADE, default='')
    yearsInterviewedFor = models.CharField(max_length=12, choices=YEAR_CHOICES, default='')

    def __str__(self):
        return self.firstName
