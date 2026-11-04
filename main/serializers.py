from django.utils.html import strip_tags
from rest_framework import serializers
from main.models import Experience, Award

class ExperienceSerializer(serializers.ModelSerializer):
    stars_count = serializers.IntegerField(source='starred_by.count', read_only=True)
    is_starred = serializers.SerializerMethodField()
    period = serializers.CharField(read_only=True)
    is_ongoing = serializers.BooleanField(read_only=True)

    class Meta:
        model = Experience
        fields = [
            'id',
            'title',
            'description',
            'category',
            'thumbnail',
            'started_at',
            'ended_at',
            'period',
            'is_ongoing',
            'stars_count',
            'is_starred',
        ]
        read_only_fields = ['id', 'started_at', 'period', 'is_ongoing', 'stars_count', 'is_starred']

    def get_is_starred(self, obj):
        request = self.context.get('request')
        if request and request.user and request.user.is_authenticated:
            return obj.starred_by.filter(id=request.user.id).exists()
        return False

    def validate_title(self, value):
        cleaned = strip_tags(value).strip() if isinstance(value, str) else ''
        if not cleaned:
            raise serializers.ValidationError("Judul pengalaman tidak boleh kosong atau hanya berisi tag HTML.")
        if len(cleaned) < 3:
            raise serializers.ValidationError("Judul pengalaman minimal 3 karakter.")
        return cleaned

    def validate_description(self, value):
        cleaned = strip_tags(value).strip() if isinstance(value, str) else ''
        if not cleaned:
            raise serializers.ValidationError("Deskripsi tidak boleh kosong atau hanya berisi tag HTML.")
        return cleaned

    def validate_thumbnail(self, value):
        if value:
            return strip_tags(value).strip()
        return value

    def validate(self, attrs):
        started_at = attrs.get('started_at') or (self.instance.started_at if self.instance else None)
        ended_at = attrs.get('ended_at')
        if ended_at and started_at and ended_at < started_at:
            raise serializers.ValidationError({
                'ended_at': 'Tanggal selesai tidak boleh lebih awal dari tanggal mulai.'
            })
        return attrs


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = [
            'id',
            'title',
            'rank',
            'issuer',
            'category',
            'year',
            'description',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate_title(self, value):
        cleaned = strip_tags(value).strip() if isinstance(value, str) else ''
        if not cleaned:
            raise serializers.ValidationError("Judul penghargaan tidak boleh kosong atau hanya berisi tag HTML.")
        return cleaned

    def validate_rank(self, value):
        cleaned = strip_tags(value).strip() if isinstance(value, str) else ''
        if not cleaned:
            raise serializers.ValidationError("Peringkat tidak boleh kosong atau hanya berisi tag HTML.")
        return cleaned

    def validate_issuer(self, value):
        cleaned = strip_tags(value).strip() if isinstance(value, str) else ''
        if not cleaned:
            raise serializers.ValidationError("Penyelenggara tidak boleh kosong atau hanya berisi tag HTML.")
        return cleaned

    def validate_description(self, value):
        cleaned = strip_tags(value).strip() if isinstance(value, str) else ''
        if not cleaned:
            raise serializers.ValidationError("Deskripsi tidak boleh kosong atau hanya berisi tag HTML.")
        return cleaned

    def validate_year(self, value):
        cleaned = str(value).strip()
        if not cleaned.isdigit() or len(cleaned) != 4:
            raise serializers.ValidationError("Tahun penghargaan harus berupa 4 digit angka (contoh: 2024).")
        return cleaned
