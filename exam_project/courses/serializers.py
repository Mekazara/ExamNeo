from rest_framework import serializers
from courses.models import Course, CourseDetail, ChooseCourse, ProgrammingLanguage


class CourseDetailSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    title = serializers.StringRelatedField()
    programming_language = serializers.StringRelatedField()
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

class CoursesListSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'address']

class NewCourseSerializer(serializers.ModelSerializer):
    duration = serializers.IntegerField(max_value=12, min_value=1)
    price_per_month = serializers.IntegerField(max_value=24000, min_value=1000)
    class Meta:
        model = CourseDetail
        fields = ['id', 'title', 'programming_language', 'duration', 'price_per_month']

class CourseShortDetailSerializer(serializers.ModelSerializer):
    title = serializers.StringRelatedField()
    programming_language = serializers.StringRelatedField()
    class Meta:
        model = CourseDetail
        fields = ['id', 'title', 'programming_language']

class ChooseCourseSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=10, min_length=9)
    full_name = serializers.CharField(max_length=60, min_length=7)

    class Meta:
        model = ChooseCourse
        fields = ['id', 'title', 'programming_language', 'user', 'phone', 'full_name']

class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CreatePrLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = '__all__'



