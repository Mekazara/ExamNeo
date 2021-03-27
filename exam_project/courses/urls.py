from django.urls import path, include
from rest_framework import routers

from courses.views import CoursePrLangViewset, NewCourseViewset

router = routers.DefaultRouter()
router.register('courseprlan', CoursePrLangViewset, basename='courseprlan')
router.register('newcourse', NewCourseViewset, basename='newcourse')

urlpatterns = [
    path('', include(router.urls))
]