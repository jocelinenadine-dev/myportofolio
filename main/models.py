import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

    @property
    def period(self):
        title_lower = self.title.lower()
        if 'bem' in title_lower or 'compfest' in title_lower or 'koko cici' in title_lower or 'koci' in title_lower:
            return "2026 – Present"
        elif 'genre' in title_lower or 'generasi berencana' in title_lower:
            return "2024 – Present"
        elif 'google' in title_lower or 'gsa' in title_lower:
            return "2024 – 2025"
        elif 'sistech' in title_lower:
            return "2026"
        elif 'open house' in title_lower:
            return "2026"
        elif 'mpk' in title_lower or 'majelis' in title_lower:
            return "2023 – 2024"
        elif 'minara' in title_lower:
            return "2024 – 2025"
        elif 'pendidik sebaya' in title_lower or 'peer' in title_lower:
            return "2023 – 2024"
        elif 'numinous' in title_lower or 'mare nostra' in title_lower:
            return "2023 – 2024"
        elif self.is_ongoing:
            return f"{self.started_at.strftime('%Y')} – Present" if self.started_at else "Present"
        else:
            start_yr = self.started_at.strftime('%Y') if self.started_at else ""
            end_yr = self.ended_at.strftime('%Y') if self.ended_at else ""
            return f"{start_yr} – {end_yr}" if start_yr and end_yr and start_yr != end_yr else (start_yr or end_yr or "Completed")


class Award(models.Model):
    AWARD_CATEGORY_CHOICES = [
        ('advocacy', 'Advocacy & Youth Leadership'),
        ('pageant', 'Cultural & Tourism Pageant'),
        ('business', 'Business & Entrepreneurship'),
        ('public-health', 'Public Health & Campaign'),
        ('academic', 'Academic Excellence'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    rank = models.CharField(max_length=100, help_text="e.g. 1st Winner, Finalist, 1st Place, Favorite Winner")
    issuer = models.CharField(max_length=255, help_text="e.g. BKKBN Provinsi DKI Jakarta")
    category = models.CharField(max_length=30, choices=AWARD_CATEGORY_CHOICES, default='advocacy')
    year = models.CharField(max_length=10, help_text="e.g. 2024, 2026")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.rank})"