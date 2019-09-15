from django.contrib import admin

from .models import CourseOutcomes,Answers,Subject
admin.site.register(CourseOutcomes)
admin.site.register(Answers)
admin.site.register(Subject)