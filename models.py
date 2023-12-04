from django.db import models




from django.db import models

class ApplyScheme(models.Model):
    sname = models.CharField(max_length=100)
    desc = models.TextField()
    eligibility = models.TextField()
    reqdocs = models.TextField()
    lastdate = models.DateField()

    def __str__(self):
        return self.sname


from django.db import models

class AddCrops(models.Model):
    cname = models.CharField(max_length=100)
    desc = models.TextField()
    season = models.TextField()
    soildetails = models.TextField()
    pesticides = models.TextField()

    def __str__(self):
        return self.cname


# models.py
from django.db import models

class Applicant(models.Model):
    Applicant_Name = models.CharField(max_length=100)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    address = models.TextField()
    aadhar_card = models.ImageField(upload_to='aadhar_cards/', null=True, blank=True)
    ration_card = models.ImageField(upload_to='ration_cards/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ), default='pending')

    def __str__(self):
        return self.name
