from django.contrib import admin
from main.models import Experience, Award


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "started_at", "ended_at", "is_ongoing")
    list_filter = ("category",)
    search_fields = ("title", "description")


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ("title", "rank", "issuer", "category", "year")
    list_filter = ("category", "year")
    search_fields = ("title", "rank", "issuer", "description")

