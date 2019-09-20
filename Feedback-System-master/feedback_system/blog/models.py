from django.db import models
from django.contrib.auth.models import User

class CourseOutcomes(models.Model):
    courseid=models.CharField(max_length=3)

class Subject(models.Model):
    subid=models.IntegerField()
    courseid=models.ForeignKey(CourseOutcomes,on_delete=models.CASCADE)
    name=models.TextField()
    content=models.TextField()
    questions=models.TextField()
class Answers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    answer=models.CharField(max_length=1)
    subid=models.ForeignKey(Subject,on_delete=models.CASCADE)