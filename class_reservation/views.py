from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from class_reservation.serializers import UserSerializer, GroupSerializer, TeacherSerializer, CategorySerializer, ClassSerializer, StudentSerializer
from class_reservation.models import Category, Class, Teacher, Student

# this handles all of out get, post, delete, edit commands for users and groups
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined') # grab all the objects and order them newest to oldest 
    serializer_class = UserSerializer
    permission_class = {permissions.IsAuthenticated}

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all() # grab all the objects
    serializer_class = GroupSerializer
    permission_class = {permissions.IsAuthenticated}

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all() # grab all the objects
    serializer_class = ClassSerializer
    permission_class = {permissions.IsAuthenticatedOrReadOnly} #if !loggedIn => can read but cant change

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all() # grab all the objects
    serializer_class = CategorySerializer
    permission_class = {permissions.IsAuthenticatedOrReadOnly} #if !loggedIn => can read but cant change

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all() # grab all the objects
    serializer_class = TeacherSerializer
    permission_class = {permissions.IsAuthenticatedOrReadOnly} #if !loggedIn => can read but cant change

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all() # grab all the objects
    serializer_class = StudentSerializer
    permission_class = {permissions.IsAuthenticatedOrReadOnly} #if !loggedIn => can read but cant change