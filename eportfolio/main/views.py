from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Student
from .forms import AchievementForm, LoginForm, StudentRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import uuid
from django.template.defaultfilters import slugify


# Главная страница
def index(request):
    students = Student.objects.all()
    return render(request, "main/index.html", {"students": students})


# Детальная информация о студенте
def detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "main/detail.html", {"student": student})


# Добавление достижения
def add_achievement(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = AchievementForm(request.POST, request.FILES)
        if form.is_valid():
            achievement = form.save(commit=False)
            achievement.student = student
            achievement.save()
    else:
        form = AchievementForm()
    return render(request, "main/add_achievement.html", {"form": form})


@login_required
def student_profile(request, username):
    user = User.objects.get(username=username)
    student = Student.objects.get(user=user)
    return render(
        request, "main/student_profile.html", {"student": student, "user": user}
    )


# Аутентификация
def user_register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data["username"]
            existing_users_count = User.objects.filter(username=username).count()
            if existing_users_count > 0:
                unique_username = create_unique_username(username)
            else:
                unique_username = username

            user = User.objects.create_user(
                username=unique_username,
                password=form.cleaned_data["password"],
                email=form.cleaned_data["email"],
            )

            first_name = form.cleaned_data.get("first_name", "")
            middle_name = form.cleaned_data.get("middle_name", "")
            last_name = form.cleaned_data.get("last_name", "")

            student = Student(user=user)
            if "photo" in form.cleaned_data:
                student.photo = form.cleaned_data["photo"]
            student.first_name = first_name
            student.middle_name = middle_name
            student.last_name = last_name
            student.location = form.cleaned_data.get("location", "")
            student.email = form.cleaned_data["email"]
            student.description = form.cleaned_data.get("description", "")

            student.save()

            messages.success(request, "Студент успешно зарегистрирован")
            return redirect("/")
    else:
        form = StudentRegistrationForm()

    return render(request, "main/register.html", {"form": form})


def create_unique_username(base_username):
    return f"{slugify(base_username)}-{uuid.uuid4().hex[:6]}"


def student_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            student = Student.objects.filter(user__username=username).first()

            if student is not None:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("profile")  # Перенаправляем на страницу профиля
                else:
                    messages.error(request, "Неверный имя пользователя или пароль")
            else:
                messages.error(request, "Пользователь с таким именем не найден")
    else:
        form = LoginForm()

    return render(request, "student_login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("/")
