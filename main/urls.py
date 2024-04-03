from django.urls import path

from main.views import index, contact, view_student

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('view/<int:pk>/', view_student, name='contact'),
]
