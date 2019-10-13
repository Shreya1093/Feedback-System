from django import forms

from .models import  ProgramOutcomess,POquestions,PAnswers,CourseOutcomes,Subject,Content


class feedbackform(forms.ModelForm):
    class Meta:
        model=PAnswers
        fields=[
                'panswer',
        ]