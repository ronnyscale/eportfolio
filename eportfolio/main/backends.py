from django.contrib.auth.backends import ModelBackend
from .models import Student


class StudentBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            student = Student.objects.get(user__username=username)
            if student.user.check_password(password):
                return student.user
        except Student.DoesNotExist:
            return None
