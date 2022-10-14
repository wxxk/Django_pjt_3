from django.db import models

# Create your models here.
class Review(models.Model):
  star_grade = (
    ('1','★'),
    ('2','★★'),
    ('3','★★★'),
    ('4','★★★★'),
    ('5','★★★★★'),
  )

  title = models.CharField(max_length=100)
  content = models.TextField()
  movie_name = models.CharField(max_length=100)
  grade = models.CharField(max_length=1, choices=star_grade)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)