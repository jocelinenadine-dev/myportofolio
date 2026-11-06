from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from main.models import Experience, Award
from main.serializers import ExperienceSerializer, AwardSerializer
from main.permissions import IsPortfolioRolePermission

class ExperienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint untuk mengelola entitas Experience.
    Mendukung Role-Based Access Control (RBAC) dan aksi dedicated Star Toggle.
    """
    serializer_class = ExperienceSerializer
    permission_classes = [IsPortfolioRolePermission]

    def get_queryset(self):
        queryset = Experience.objects.all().order_by('-started_at')
        title = self.request.query_params.get('title', None)
        category = self.request.query_params.get('category', None)
        if title:
            queryset = queryset.filter(title__icontains=title.strip())
        if category:
            queryset = queryset.filter(category=category.strip())
        return queryset

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def star(self, request, pk=None):
        """
        Dedicated endpoint untuk melakukan toggle status bintang (star).
        Hanya dapat diakses oleh pengguna terautentikasi (Regular User, Editor, Superuser).
        """
        experience = self.get_object()
        user = request.user
        if experience.starred_by.filter(id=user.id).exists():
            experience.starred_by.remove(user)
            is_starred = False
        else:
            experience.starred_by.add(user)
            is_starred = True

        return Response({
            'status': 'success',
            'id': str(experience.id),
            'title': experience.title,
            'is_starred': is_starred,
            'stars_count': experience.starred_by.count(),
        }, status=status.HTTP_200_OK)


class AwardViewSet(viewsets.ModelViewSet):
    """
    API endpoint untuk mengelola entitas Award (Honors & Awards).
    Mendukung Role-Based Access Control (RBAC).
    """
    serializer_class = AwardSerializer
    permission_classes = [IsPortfolioRolePermission]

    def get_queryset(self):
        queryset = Award.objects.all().order_by('-created_at')
        title = self.request.query_params.get('title', None)
        category = self.request.query_params.get('category', None)
        if title:
            queryset = queryset.filter(title__icontains=title.strip())
        if category:
            queryset = queryset.filter(category=category.strip())
        return queryset
