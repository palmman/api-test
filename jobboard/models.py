from django.db import models

# Create your models here.

class JobOffer(models.Model):

    compant_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=100)
    job_des = models.TextField(max_length=1000, null=True, blank=True)
    salary = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.compant_name} {self.job_title}'