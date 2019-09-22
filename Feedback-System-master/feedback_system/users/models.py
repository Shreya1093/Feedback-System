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


    def __str__(self):
        return self.name
class questions(models.Model):
    courseid=models.ForeignKey(CourseOutcomes,on_delete=models.CASCADE)
    question=models.TextField()
    questionid=models.IntegerField()
    def __str__(self):
        return str(self.question) + "," + str(self.questionid) + "," + str(self.courseid)

class Answers(models.Model):

    answer=models.CharField(max_length=1)
    courseid = models.ForeignKey(CourseOutcomes, on_delete=models.CASCADE,null=True,blank=True)
    questionid=models.ForeignKey(questions,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return str(self.questionid)
class Content(models.Model):
    subid=models.ForeignKey(Subject,on_delete=models.CASCADE)
    content=models.TextField()
    def __str__(self):
        return str(self.pk)+self.subid.name

