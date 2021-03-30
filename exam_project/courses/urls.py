from django.urls import path, include
from rest_framework import routers

from courses.views import CoursePrLangViewset, NewCourseViewset, \
    ChooseCourseViewset, ReviewCourseViewset, CreatePrLangViewset, CreateCourseViewset

router = routers.DefaultRouter()
router.register('courseprlan', CoursePrLangViewset, basename='courseprlan')
router.register('newcourse', NewCourseViewset, basename='newcourse')
router.register('choosecourse', ChooseCourseViewset, basename='choosecourse')
router.register('reviewcourses', ReviewCourseViewset, basename='reviewcourses')
router.register('createcourse', CreateCourseViewset, basename='createcourse')
router.register('createproglang', CreatePrLangViewset, basename='createproglang')


urlpatterns = [
    path('', include(router.urls))
]