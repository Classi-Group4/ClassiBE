from django.contrib.auth.models import User, Group
from rest_framework import serializers
from class_reservation.models import Category, Class, Teacher, Student

# Serializers allow complex data such as querysets and model instances to be 
# converted to native Python datatypes that can then be easily rendered into
# JSON , XML or other content types.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups'] #instead of using pk we will use a url


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Group
        fields = ['url', 'name'] 

class ClassSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Class
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'