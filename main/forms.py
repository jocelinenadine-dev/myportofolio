from django.core.exceptions import ValidationError
from django.forms import ModelForm, Select, Textarea, TextInput
from django.utils.html import strip_tags
from main.models import Award, Experience


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "category",
            "description",
            "thumbnail",
        ]

        labels = {
            "title": "Posisi / Peran Organisasi",
            "category": "Kategori Pengalaman",
            "description": "Deskripsi & Tanggung Jawab",
            "thumbnail": "URL Thumbnail / Logo (Opsional)",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Staff of Public Relations BEM Fasilkom UI",
                    "maxlength": 255,
                    "class": "form-input",
                }
            ),
            "category": Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Jelaskan peran, tanggung jawab, dan dampak dari pengalaman ini...",
                    "rows": 4,
                    "class": "form-textarea",
                }
            ),
            "thumbnail": TextInput(
                attrs={
                    "placeholder": "https://example.com/logo.png",
                    "class": "form-input",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Posisi atau peran tidak boleh kosong atau hanya berisi tag HTML.")
        return title

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"]).strip()
        if not description:
            raise ValidationError("Deskripsi tidak boleh kosong atau hanya berisi tag HTML.")
        return description

    def clean_thumbnail(self):
        thumbnail = self.cleaned_data.get("thumbnail")
        if thumbnail:
            return strip_tags(thumbnail).strip()
        return thumbnail


class AwardForm(ModelForm):
    class Meta:
        model = Award
        fields = [
            "title",
            "rank",
            "issuer",
            "category",
            "year",
            "description",
        ]

        labels = {
            "title": "Nama Penghargaan / Title",
            "rank": "Peringkat / Rank",
            "issuer": "Institusi / Penyelenggara",
            "category": "Kategori Bidang",
            "year": "Tahun Perolehan",
            "description": "Deskripsi dan Rincian Prestasi",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Puteri Duta GenRe Kota Jakarta Pusat",
                    "maxlength": 255,
                    "class": "form-input",
                }
            ),
            "rank": TextInput(
                attrs={
                    "placeholder": "Contoh: 1st Winner & Best Group Talent",
                    "maxlength": 100,
                    "class": "form-input",
                }
            ),
            "issuer": TextInput(
                attrs={
                    "placeholder": "Contoh: BKKBN Kota Jakarta Pusat",
                    "maxlength": 255,
                    "class": "form-input",
                }
            ),
            "category": Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "year": TextInput(
                attrs={
                    "placeholder": "Contoh: 2024",
                    "maxlength": 10,
                    "class": "form-input",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan proses seleksi, peran advokasi, atau dampak dari penghargaan ini...",
                    "rows": 4,
                    "class": "form-textarea",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama penghargaan tidak boleh kosong atau hanya berisi tag HTML.")
        return title

    def clean_rank(self):
        rank = strip_tags(self.cleaned_data["rank"]).strip()
        if not rank:
            raise ValidationError("Peringkat tidak boleh kosong atau hanya berisi tag HTML.")
        return rank

    def clean_issuer(self):
        issuer = strip_tags(self.cleaned_data["issuer"]).strip()
        if not issuer:
            raise ValidationError("Penyelenggara tidak boleh kosong atau hanya berisi tag HTML.")
        return issuer

    def clean_year(self):
        year = strip_tags(self.cleaned_data["year"]).strip()
        if not year:
            raise ValidationError("Tahun perolehan tidak boleh kosong atau hanya berisi tag HTML.")
        return year

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"]).strip()
        if not description:
            raise ValidationError("Deskripsi tidak boleh kosong atau hanya berisi tag HTML.")
        return description
