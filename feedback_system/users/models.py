from django.db import models
from django.contrib.auth.models import User

class CourseOutcomes(models.Model):
    courseid=models.CharField(max_length=3)
    def __str__(self):
        return self.courseid
class Subject(models.Model):
    subid=models.IntegerField()
    courseid=models.ForeignKey(CourseOutcomes,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    questions=models.TextField()

    def __str__(self):
        return self.name
class Answers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    answer=models.CharField(max_length=1)
    subid=models.ForeignKey(Subject,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username+" Answer"+" for "+self.subid.name
class Content(models.Model):
    subid=models.ForeignKey(Subject,on_delete=models.CASCADE)
    content=models.TextField()