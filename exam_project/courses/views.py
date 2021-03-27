from django.shortcuts import render
from rest_framework import viewsets

from courses.models import Course, CourseDetail
from courses.serializers import CourseDetailPrLangSerializer, NewCourseSerializer

class CoursePrLangViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailPrLangSerializer

class NewCourseViewset(viewsets.ModelViewSet):
    queryset = CourseDetail.objects.all()
    serializer_class = NewCourseSerializer




