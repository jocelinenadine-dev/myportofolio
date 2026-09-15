import json
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.forms import AwardForm
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

    def test_create_award_get(self):
        response = self.client.get(reverse("main:create_award"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "award_form.html")
        self.assertIsInstance(response.context["form"], AwardForm)

    def test_create_award_post_valid(self):
        data = {
            "title": "Koko Cici Jakarta 2026",
            "rank": "Finalist",
            "issuer": "Dinas Pariwisata DKI Jakarta",
            "category": "pageant",
            "year": "2026",
            "description": "Finalis Duta Wisata dan Budaya Tionghoa Jakarta.",
        }
        response = self.client.post(reverse("main:create_award"), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("main:show_awards"))
        self.assertTrue(Award.objects.filter(title="Koko Cici Jakarta 2026").exists())

    def test_create_award_post_invalid(self):
        data = {
            "title": "",  # missing required title
            "rank": "Winner",
        }
        response = self.client.post(reverse("main:create_award"), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "award_form.html")
        self.assertTrue(response.context["form"].errors)

    def test_delete_award_post(self):
        award_to_delete = Award.objects.create(
            title="Sample Award to Delete",
            rank="3rd Winner",
            issuer="Sample Org",
            category="academic",
            year="2023",
            description="Sample description",
        )
        response = self.client.post(reverse("main:delete_award", kwargs={"award_id": award_to_delete.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("main:show_awards"))
        self.assertFalse(Award.objects.filter(id=award_to_delete.id).exists())

    def test_get_awards_json(self):
        response = self.client.get(reverse("main:get_awards_json"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["content-type"], "application/json")
        data = json.loads(response.content.decode("utf-8"))
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)
        self.assertEqual(data[0]["fields"]["title"], self.award.title)

    def test_get_awards_json_with_filter(self):
        response = self.client.get(reverse("main:get_awards_json") + "?title=GenRe")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["fields"]["title"], self.award.title)

        # Non-matching search
        response_empty = self.client.get(reverse("main:get_awards_json") + "?title=NonExistentQueryXYZ")
        data_empty = json.loads(response_empty.content.decode("utf-8"))
        self.assertEqual(len(data_empty), 0)

    def test_show_awards_search_query(self):
        response = self.client.get(reverse("main:show_awards") + "?title=GenRe")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.award.title)

        response_not_found = self.client.get(reverse("main:show_awards") + "?title=NonExistentQueryXYZ")
        self.assertEqual(response_not_found.status_code, 200)
        self.assertContains(response_not_found, "Tidak ada penghargaan dengan nama")

    def test_get_awards_xml(self):
        response = self.client.get(reverse("main:get_awards_xml"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["content-type"], "application/xml")
        self.assertContains(response, self.award.title)

    def test_get_awards_xml_with_filter(self):
        response = self.client.get(reverse("main:get_awards_xml") + "?title=GenRe")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.award.title)

        response_empty = self.client.get(reverse("main:get_awards_xml") + "?title=NonExistentQueryXYZ")
        self.assertEqual(response_empty.status_code, 200)
        self.assertNotContains(response_empty, self.award.title)
