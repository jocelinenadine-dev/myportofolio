from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import AwardForm, ExperienceForm
from main.models import Experience, Award


def show_main(request):
    context = {
        "name": "Joceline Nadine Immanuella",
        "npm": "2506656835",
        "study_program": "B.Sc. Information Systems",
        "bio": (
            "Information Systems student at Universitas Indonesia passionate "
            "about technology development, strategic team collaboration, and youth leadership."
        ),
    }
    return render(request, "index.html", context)


def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all().order_by("-started_at")

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
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


def create_experience(request):
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


def edit_experience(request, experience_id):
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


def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


def get_awards_json(request):
    title_query = request.GET.get("title", "").strip()
    awards = Award.objects.all().order_by("-year", "-created_at")

    if title_query:
        awards = awards.filter(title__icontains=title_query)

    awards_json = serializers.serialize("json", awards)
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


def create_award(request):
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


def edit_award(request, award_id):
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


def delete_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)

    if request.method == "POST":
        award.delete()
        messages.success(request, "Penghargaan berhasil dihapus!")
        return redirect("main:show_awards")

    return redirect("main:show_awards")
