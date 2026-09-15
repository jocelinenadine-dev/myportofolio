from django.urls import path
from main.views import (
    show_main,
    show_experience,
    show_awards,
    create_award,
    delete_award,
    get_awards_json,
    get_awards_xml,
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('experience/', show_experience, name='show_experience'),
    path('awards/', show_awards, name='show_awards'),
    path('awards/add/', create_award, name='create_award'),
    path('awards/<uuid:award_id>/delete/', delete_award, name='delete_award'),
    path('api/awards/', get_awards_json, name='get_awards_json'),
    path('api/awards/xml/', get_awards_xml, name='get_awards_xml'),
]