from django import forms

from .models import  Answers,CourseOutcomes,Subject,Content,questions


class feedbackform(forms.ModelForm):
    class Meta:
        model=Answers
        fields=[
                'answer',
        ]