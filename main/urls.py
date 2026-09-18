from django.urls import path
from main.views import (
    show_main,
    show_experience,
    create_experience,
    edit_experience,
    delete_experience,
    get_experiences_json,
    get_experiences_xml,
    show_awards,
    create_award,
    edit_award,
    delete_award,
    get_awards_json,
    get_awards_xml,
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('experience/', show_experience, name='show_experience'),
    path('experience/add/', create_experience, name='create_experience'),
    path('experience/<uuid:experience_id>/edit/', edit_experience, name='edit_experience'),
    path('experience/<uuid:experience_id>/delete/', delete_experience, name='delete_experience'),
    path('api/experience/', get_experiences_json, name='get_experiences_json'),
    path('api/experience/xml/', get_experiences_xml, name='get_experiences_xml'),
    path('awards/', show_awards, name='show_awards'),
    path('awards/add/', create_award, name='create_award'),
    path('awards/<uuid:award_id>/edit/', edit_award, name='edit_award'),
    path('awards/<uuid:award_id>/delete/', delete_award, name='delete_award'),
    path('api/awards/', get_awards_json, name='get_awards_json'),
    path('api/awards/xml/', get_awards_xml, name='get_awards_xml'),
]