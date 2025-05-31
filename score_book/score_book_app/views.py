from django.shortcuts import render
from rest_framework import viewsets

from score_book_app.models import Student, Score, Subject
from score_book_app.serializers import StudentSerializer, ScoreSerializer, SubjectSerializer


class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get']

class SubjectApi(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    http_method_names = ['get']

class ScoreApi(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    http_method_names = ['get']
