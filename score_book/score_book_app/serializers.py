from rest_framework import serializers

from .models import Student, Subject, Score

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','Name','Surname']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ScoreSerializer(serializers.ModelSerializer):
    Student = StudentSerializer()
    Subject = SubjectSerializer()
    class Meta:
        model = Score
        fields = '__all__'
