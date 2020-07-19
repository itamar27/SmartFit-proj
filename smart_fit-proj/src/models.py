from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Workout(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    scale = models.IntegerField()
    rating = models.IntegerField(blank =True, validators=[MaxValueValidator(10),MinValueValidator(1)], null=True)

    ex_1_name = models.CharField(max_length=255)
    ex_1_reps = models.CharField(max_length=255)
    ex_1_sets = models.CharField(max_length=255)
    ex_1_desc = models.TextField(max_length=160, blank=True, default='')

    ex_2_name = models.CharField(max_length=255, null=True, blank=True)
    ex_2_reps = models.CharField(max_length=255, null=True, blank=True)
    ex_2_sets = models.CharField(max_length=255, null=True, blank=True)
    ex_2_desc = models.TextField(max_length=160, blank=True, default='')

    ex_3_name = models.CharField(max_length=255, null=True, blank=True)
    ex_3_reps = models.CharField(max_length=255, null=True, blank=True)
    ex_3_sets = models.CharField(max_length=255, null=True, blank=True)
    ex_3_desc = models.TextField(max_length=160, blank=True, default='')
