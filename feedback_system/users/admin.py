from django.contrib import admin
from .models import Answers,CourseOutcomes,Subject,Content
# Register your models here.
admin.site.register(Answers)
admin.site.register(CourseOutcomes)
admin.site.register(Subject)
admin.site.register(Content)