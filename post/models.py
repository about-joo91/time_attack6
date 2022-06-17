from django.db import models

# Create your models here.
class TechSkill(models.Model):
    stack_name = models.CharField(max_length=30)

class Company(models.Model):
    company_name = models.CharField(max_length=128)
    business_area = models.ManyToManyField('BusinessArea')

class BusinessArea(models.Model):
    area_name = models.CharField(max_length=100)


class JopPost(models.Model):
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=80)
    job_desc = models.TextField()
    skills = models.ManyToManyField('TechSkill')

