from django.contrib import admin
from .models import Answers,CourseOutcomes,Subject,Content,questions,ProgramOutcomess,PAnswers,POquestions
# Register your models here.
admin.site.register(Answers)
admin.site.register(CourseOutcomes)
admin.site.register(Subject)
admin.site.register(Content)
admin.site.register(questions)
admin.site.register(POquestions)
admin.site.register(PAnswers)
admin.site.register(ProgramOutcomess)


