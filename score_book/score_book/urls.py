from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from score_book_app.views import StudentApi, ScoreApi, SubjectApi

router = routers.DefaultRouter()
router.register(r'api/studentlist', StudentApi)
router.register(r'api/scorelist', ScoreApi)
router.register(r'api/subjectlist', SubjectApi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
