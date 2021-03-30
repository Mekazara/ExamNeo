from django.contrib import admin
from courses.models import Course, ProgrammingLanguage, \
    CourseDetail, ChooseCourse

admin.site.register(Course)
admin.site.register(ProgrammingLanguage)
admin.site.register(CourseDetail)
admin.site.register(ChooseCourse)