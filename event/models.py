from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event/images/', blank=True, null=True)  # You may specify the upload_to path as per your requirement
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    event_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['created_date']
        

    def __str__(self):
        return self.title
    

class Donation(models.Model):
    full_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purpose = models.CharField(max_length=255, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)  # Specify max_length for the note field

    def __str__(self):
        return f"{self.full_name}'s donation"
