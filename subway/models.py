from django.db import models

# Create your models here.

class Station(models.Model):
  name = models.CharField(max_length=128)
  accessible = models.BooleanField(default=False)
  rat_count = models.IntegerField(null=True, blank=True)

  def __str__(self):
      return self.name

class Line(models.Model):
  name = models.CharField(max_length=128)
  express = models.BooleanField(default=False)
  stations = models.ManyToManyField(Station)

  def __str__(self):
      return self.name

class Train(models.Model):
  name = models.CharField(max_length=5)
  line = models.ForeignKey(Line, on_delete=models.CASCADE)

  def __str__(self):
      return self.name
