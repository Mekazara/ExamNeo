from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from courses.models import Course, CourseDetail, ChooseCourse, ProgrammingLanguage
from courses.serializers import CourseDetailPrLangSerializer, NewCourseSerializer, \
    CoursesListSerilizer, ChooseCourseSerializer, CourseDetailSerializer, CourseShortDetailSerializer, \
    CreateCourseSerializer, CreatePrLangSerializer


class CoursePrLangViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailPrLangSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = CoursesListSerilizer
        return super().list(request, *args, **kwargs)

class NewCourseViewset(viewsets.ModelViewSet):
    queryset = CourseDetail.objects.all()
    serializer_class = NewCourseSerializer

class ReviewCourseViewset(viewsets.ModelViewSet):
    queryset = CourseDetail.objects.all()
    serializer_class = CourseShortDetailSerializer

class CreateCourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CreateCourseSerializer

class CreatePrLangViewset(viewsets.ModelViewSet):
    queryset = ProgrammingLanguage.objects.all()
    serializer_class = CreatePrLangSerializer

class ChooseCourseViewset(viewsets.ModelViewSet):
    queryset = ChooseCourse.objects.all()
    serializer_class = ChooseCourseSerializer

    def create(self, request, *args, **kwargs):
        user = self.request.user
        serializer = ChooseCourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        # if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_201_CREATED)

