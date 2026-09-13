from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Award


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Riset Sistem Informasi",
            description="Membantu riset pemodelan arsitektur sistem informasi enterprise.",
            category="organization",
        )
        self.award = Award.objects.create(
            title="Puteri Duta GenRe Kota Jakarta Pusat",
            rank="1st Winner",
            issuer="BKKBN Kota Jakarta Pusat",
            category="advocacy",
            year="2024",
            description="Terpilih sebagai Juara 1 dan Duta GenRe Jakarta Pusat dalam advokasi kesehatan remaja.",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_awards")}"')


    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Riset Sistem Informasi")
        self.assertEqual(self.experience.category, "organization")
        self.assertTrue(self.experience.is_ongoing)


    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Organization")
        self.assertContains(response, "Ongoing")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_awards")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Completed")
        self.assertNotContains(response, "Ongoing")

    def test_award_model(self):
        self.assertEqual(str(self.award), "Puteri Duta GenRe Kota Jakarta Pusat (1st Winner)")
        self.assertEqual(self.award.category, "advocacy")
        self.assertEqual(self.award.year, "2024")


    def test_award_page_accessible_and_uses_template(self):
        response = self.client.get(reverse("main:show_awards"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "awards.html")

    def test_award_page_displays_data(self):
        response = self.client.get(reverse("main:show_awards"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.award.title)
        self.assertContains(response, self.award.rank)
        self.assertContains(response, self.award.issuer)
        self.assertContains(response, self.award.description)
        self.assertContains(response, "Advocacy &amp; Youth Leadership")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_empty_award_page(self):
        Award.objects.all().delete()
        response = self.client.get(reverse("main:show_awards"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada penghargaan yang ditambahkan.")


