from rest_framework import serializers
from courses.models import Course, CourseDetail

class CourseDetailSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = CourseDetail
        fields = ['id', 'title', 'programming_language', 'duration', 'price_per_month', 'total_price']

    def get_total_price(self, instance):
        total_price = instance.duration * instance.price_per_month
        return total_price

class CourseDetailPrLangSerializer(serializers.ModelSerializer):
    courses = CourseDetailSerializer(many=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'address', 'courses']

class NewCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDetail
        fields = ['id', 'title', 'programming_language', 'duration', 'price_per_month']


