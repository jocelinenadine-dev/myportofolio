import datetime
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import AwardForm, ExperienceForm
from main.models import Experience, Award


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Joceline Nadine Immanuella",
        "npm": "2506656835",
        "study_program": "B.Sc. Information Systems",
        "bio": (
            "Information Systems student at Universitas Indonesia passionate "
            "about technology development, strategic team collaboration, and youth leadership."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Joceline Nadine Immanuella",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Joceline Nadine Immanuella",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response


def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all().order_by("-started_at")

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences, use_natural_foreign_keys=True)
    return HttpResponse(experiences_json, content_type="application/json")


def get_experiences_xml(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all().order_by("-started_at")

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_xml = serializers.serialize("xml", experiences)
    return HttpResponse(experiences_xml, content_type="application/xml")


def show_experience(request):
    json_response = get_experiences_json(request)
    experiences_deserialized = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [exp.object for exp in experiences_deserialized]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Joceline Nadine Immanuella",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)


@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Joceline Nadine Immanuella",
        "form": form,
        "is_edit": False,
    }
    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Joceline Nadine Immanuella",
        "form": form,
        "experience": experience,
        "is_edit": True,
    }
    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")


def get_awards_json(request):
    title_query = request.GET.get("title", "").strip()
    awards = Award.objects.all().order_by("-year", "-created_at")

    if title_query:
        awards = awards.filter(title__icontains=title_query)

    awards_json = serializers.serialize("json", awards, use_natural_foreign_keys=True)
    return HttpResponse(awards_json, content_type="application/json")


def get_awards_xml(request):
    title_query = request.GET.get("title", "").strip()
    awards = Award.objects.all().order_by("-year", "-created_at")

    if title_query:
        awards = awards.filter(title__icontains=title_query)

    awards_xml = serializers.serialize("xml", awards)
    return HttpResponse(awards_xml, content_type="application/xml")


def show_awards(request):
    json_response = get_awards_json(request)
    awards_deserialized = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    awards = [award.object for award in awards_deserialized]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Joceline Nadine Immanuella",
        "award_list": awards,
        "title_query": title_query,
    }
    return render(request, "awards.html", context)


@login_required(login_url="/login/")
def create_award(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = AwardForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Penghargaan baru berhasil ditambahkan!")
        return redirect("main:show_awards")

    context = {
        "name": "Joceline Nadine Immanuella",
        "form": form,
        "is_edit": False,
    }
    return render(request, "award_form.html", context)


@login_required(login_url="/login/")
def edit_award(request, award_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    award = get_object_or_404(Award, pk=award_id)
    form = AwardForm(request.POST or None, instance=award)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Penghargaan berhasil diperbarui!")
        return redirect("main:show_awards")

    context = {
        "name": "Joceline Nadine Immanuella",
        "form": form,
        "award": award,
        "is_edit": True,
    }
    return render(request, "award_form.html", context)


@login_required(login_url="/login/")
def delete_award(request, award_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    award = get_object_or_404(Award, pk=award_id)

    if request.method == "POST":
        award.delete()
        messages.success(request, "Penghargaan berhasil dihapus!")
        return redirect("main:show_awards")

    return redirect("main:show_awards")
