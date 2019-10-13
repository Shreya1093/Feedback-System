from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User



class CourseOutcomes(models.Model):
    courseid=models.CharField(max_length=3)
    def __str__(self):
        return str(self.courseid)
class Subject(models.Model):
    subid=models.IntegerField()
    courseid=models.ForeignKey(CourseOutcomes,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)


    def __str__(self):
        return self.name
class questions(models.Model):
    courseid=models.ForeignKey(CourseOutcomes,on_delete=models.CASCADE)
    question=models.CharField(max_length=2000)
    questionid=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.question) #+ "," + str(self.questionid) + "," + str(self.courseid)

class Answers(models.Model):
    CHOICES = zip(range(1, 6), range(1, 6))
    answer = models.IntegerField(default=6,choices=CHOICES, blank=False)
    #answer=models.IntegerField(default=5, help_text='value 1 to 5', validators=[MaxValueValidator(5),
            #MinValueValidator(1)])
    courseid = models.ForeignKey(CourseOutcomes, on_delete=models.CASCADE,null=True,blank=True)
    question=models.ForeignKey(questions,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return str(self.answer)+" "+str(self.question)
class Content(models.Model):
    subid=models.ForeignKey(Subject,on_delete=models.CASCADE)
    content=models.TextField()
    def __str__(self):
        return str(self.pk)+self.subid.name

class ProgramOutcomess(models.Model):
    pid=models.IntegerField()
    poutcome=models.TextField()
    def __str__(self):
        return str(self.pid)


class POquestions(models.Model):
    pid=models.ForeignKey(ProgramOutcomess,on_delete=models.CASCADE)
    pquestion=models.CharField(max_length=2000)

    def __str__(self):
        return str(self.pid) #+ "," + str(self.questionid) + "," + str(self.courseid)

class PAnswers(models.Model):

    CHOICES = zip(range(1, 6), range(1, 6))
    panswer = models.IntegerField(default=6,choices=CHOICES, blank=False)
    #panswer=models.CharField(max_length=1)
    pid = models.ForeignKey(ProgramOutcomess, on_delete=models.CASCADE,null=True,blank=True)
    pquestion = models.ForeignKey(POquestions, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.panswer) + " " + str(self.pquestion)
