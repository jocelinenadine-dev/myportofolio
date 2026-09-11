from django.shortcuts import render
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


def show_experience(request):
    context = {
        "name": "Joceline Nadine Immanuella",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_awards(request):
    context = {
        "name": "Joceline Nadine Immanuella",
        "award_list": Award.objects.all().order_by("-year", "-created_at"),
    }
    return render(request, "awards.html", context)