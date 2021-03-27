from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=35)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.title

class ProgrammingLanguage(models.Model):
    programming_language = models.CharField(max_length=35)

    def __str__(self):
        return self.programming_language

class CourseDetail(models.Model):
    title = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='courses')
    programming_language = models.ForeignKey(ProgrammingLanguage, on_delete=models.SET_NULL,
                                             null=True)
    duration = models.IntegerField()
    price_per_month = models.IntegerField()



    def __str__(self):
        return str(self.programming_language) + ' ' + str(self.title)

