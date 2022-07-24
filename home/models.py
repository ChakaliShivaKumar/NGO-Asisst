from django.db import models
from django.core.validators import MinValueValidator


class Client(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    ]
    MARTIAL_CHOICES = [
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        ('Separated', 'Separated'),
        ('Divorced', 'Divorced'),
        ('Single', 'Single'),
    ]
    PROSTHETIC_CHOICES = [
        ("Prosthetic Leg", "Prosthetic Leg"),
        ("Caliper", "Caliper"),
        ("Cruthces", "Cruthces"),
        ("Hands", "Hands"),
        ("Knee Cap", "Knee Cap"),
        ("L.S.Belt", "L.S.Belt"),
        ("Soft Collar", "Soft Collar")
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=10, choices=MARTIAL_CHOICES)
    edu_back = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MinValueValidator(1)])
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    prosthetic_being_used = models.CharField(
        max_length=100, choices=PROSTHETIC_CHOICES)

    class Meta:
        app_label = 'home'

    def __str__(self):
        return self.name
