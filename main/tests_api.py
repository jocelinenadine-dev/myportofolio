from django.contrib.auth.models import User, Group
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from main.models import Experience, Award

class BaseAPITestCase(APITestCase):
    def setUp(self):
        # Setup group
        self.editor_group, _ = Group.objects.get_or_create(name="Editor")

        # 1. Guest (Unauthenticated)
        self.guest_client = self.client_class()

        # 2. Regular User
        self.regular_user = User.objects.create_user(
            username="regular_user",
            password="Password123!"
        )

        # 3. Editor
        self.editor_user = User.objects.create_user(
            username="editor_user",
            password="Password123!"
        )
        self.editor_user.groups.add(self.editor_group)

        # 4. Superuser
        self.superuser = User.objects.create_superuser(
            username="super_admin",
            password="SuperPassword123!",
            email="admin@example.com"
        )

        # Sample Experience
        self.experience = Experience.objects.create(
            title="BEM Fasilkom UI - Staff",
            description="Staff of Department",
            category="organization"
        )

        # Sample Award
        self.award = Award.objects.create(
            title="Juara 1 Duta GenRe DKI Jakarta",
            rank="1st Winner",
            issuer="BKKBN DKI Jakarta",
            category="advocacy",
            year="2024",
            description="Penghargaan tingkat provinsi"
        )


class ExperienceAPITests(BaseAPITestCase):
    def test_guest_can_list_experiences(self):
        url = reverse('api-experience-list')
        response = self.guest_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.experience.title)
        self.assertEqual(response.data[0]['is_starred'], False)
        self.assertEqual(response.data[0]['stars_count'], 0)

    def test_guest_can_retrieve_experience_detail(self):
        url = reverse('api-experience-detail', kwargs={'pk': self.experience.id})
        response = self.guest_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(self.experience.id))

    def test_guest_cannot_create_experience(self):
        url = reverse('api-experience-list')
        data = {
            'title': 'New Guest Experience',
            'description': 'Description',
            'category': 'committee'
        }
        response = self.guest_client.post(url, data, format='json')
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_guest_cannot_toggle_star(self):
        url = reverse('api-experience-star', kwargs={'pk': self.experience.id})
        response = self.guest_client.post(url)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_regular_user_can_toggle_star(self):
        self.client.force_authenticate(user=self.regular_user)
        url = reverse('api-experience-star', kwargs={'pk': self.experience.id})
        
        # First toggle: star added
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['is_starred'])
        self.assertEqual(response.data['stars_count'], 1)
        self.assertTrue(self.experience.starred_by.filter(id=self.regular_user.id).exists())

        # Second toggle: star removed
        response2 = self.client.post(url)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertFalse(response2.data['is_starred'])
        self.assertEqual(response2.data['stars_count'], 0)
        self.assertFalse(self.experience.starred_by.filter(id=self.regular_user.id).exists())

    def test_regular_user_cannot_create_experience(self):
        self.client.force_authenticate(user=self.regular_user)
        url = reverse('api-experience-list')
        data = {
            'title': 'Regular User Attempt',
            'description': 'Attempting create',
            'category': 'volunteer'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_regular_user_cannot_update_or_delete_experience(self):
        self.client.force_authenticate(user=self.regular_user)
        detail_url = reverse('api-experience-detail', kwargs={'pk': self.experience.id})
        
        # PUT
        put_response = self.client.put(detail_url, {'title': 'Updated Title', 'description': 'Updated'}, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_403_FORBIDDEN)

        # DELETE
        del_response = self.client.delete(detail_url)
        self.assertEqual(del_response.status_code, status.HTTP_403_FORBIDDEN)

    def test_editor_can_update_experience_but_cannot_create_or_delete(self):
        self.client.force_authenticate(user=self.editor_user)
        list_url = reverse('api-experience-list')
        detail_url = reverse('api-experience-detail', kwargs={'pk': self.experience.id})

        # Editor cannot create
        create_res = self.client.post(list_url, {'title': 'Editor Attempt', 'description': 'Desc', 'category': 'research'}, format='json')
        self.assertEqual(create_res.status_code, status.HTTP_403_FORBIDDEN)

        # Editor CAN update (PATCH)
        patch_res = self.client.patch(detail_url, {'title': 'BEM Fasilkom UI - Updated by Editor'}, format='json')
        self.assertEqual(patch_res.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, 'BEM Fasilkom UI - Updated by Editor')

        # Editor cannot delete
        del_res = self.client.delete(detail_url)
        self.assertEqual(del_res.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_has_full_crud_on_experience(self):
        self.client.force_authenticate(user=self.superuser)
        list_url = reverse('api-experience-list')

        # 1. Create
        create_data = {
            'title': 'Compfest Lead Admin',
            'description': 'Leadership experience',
            'category': 'committee'
        }
        create_res = self.client.post(list_url, create_data, format='json')
        self.assertEqual(create_res.status_code, status.HTTP_201_CREATED)
        new_id = create_res.data['id']

        # 2. Retrieve
        detail_url = reverse('api-experience-detail', kwargs={'pk': new_id})
        get_res = self.client.get(detail_url)
        self.assertEqual(get_res.status_code, status.HTTP_200_OK)
        self.assertEqual(get_res.data['title'], 'Compfest Lead Admin')

        # 3. Update
        patch_res = self.client.patch(detail_url, {'title': 'Compfest Vice Project Officer'}, format='json')
        self.assertEqual(patch_res.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_res.data['title'], 'Compfest Vice Project Officer')

        # 4. Delete
        del_res = self.client.delete(detail_url)
        self.assertEqual(del_res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Experience.objects.filter(id=new_id).exists())

    def test_experience_validation_empty_title(self):
        self.client.force_authenticate(user=self.superuser)
        list_url = reverse('api-experience-list')
        bad_data = {
            'title': '   ',
            'description': 'Valid description',
            'category': 'internship'
        }
        response = self.client.post(list_url, bad_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)

    def test_experience_xss_sanitization(self):
        self.client.force_authenticate(user=self.superuser)
        list_url = reverse('api-experience-list')
        data = {
            'title': '<b>Google Ambassador</b>',
            'description': '<p>Deskripsi kepemimpinan</p>',
            'category': 'ambassador'
        }
        res = self.client.post(list_url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['title'], 'Google Ambassador')
        self.assertEqual(res.data['description'], 'Deskripsi kepemimpinan')

    def test_experience_filter_by_title_and_category(self):
        url = reverse('api-experience-list')
        # Filter matching
        res = self.guest_client.get(f"{url}?title=BEM")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)

        # Filter not matching
        res_empty = self.guest_client.get(f"{url}?title=NonExistentTitleXYZ")
        self.assertEqual(res_empty.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_empty.data), 0)


class AwardAPITests(BaseAPITestCase):
    def test_guest_can_list_awards(self):
        url = reverse('api-award-list')
        response = self.guest_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.award.title)

    def test_regular_user_cannot_create_or_modify_award(self):
        self.client.force_authenticate(user=self.regular_user)
        list_url = reverse('api-award-list')
        detail_url = reverse('api-award-detail', kwargs={'pk': self.award.id})

        # Create
        res_post = self.client.post(list_url, {'title': 'Hackathon Winner', 'rank': '1st', 'issuer': 'Tech', 'year': '2025', 'description': 'desc'}, format='json')
        self.assertEqual(res_post.status_code, status.HTTP_403_FORBIDDEN)

        # Update
        res_put = self.client.put(detail_url, {'title': 'Hacked', 'rank': '1st', 'issuer': 'Tech', 'year': '2025', 'description': 'desc'}, format='json')
        self.assertEqual(res_put.status_code, status.HTTP_403_FORBIDDEN)

        # Delete
        res_del = self.client.delete(detail_url)
        self.assertEqual(res_del.status_code, status.HTTP_403_FORBIDDEN)

    def test_editor_can_update_award_only(self):
        self.client.force_authenticate(user=self.editor_user)
        list_url = reverse('api-award-list')
        detail_url = reverse('api-award-detail', kwargs={'pk': self.award.id})

        # Cannot create
        res_post = self.client.post(list_url, {'title': 'New Award', 'rank': '1st', 'issuer': 'UI', 'year': '2026', 'description': 'desc'}, format='json')
        self.assertEqual(res_post.status_code, status.HTTP_403_FORBIDDEN)

        # CAN update
        res_patch = self.client.patch(detail_url, {'rank': 'Top 3 Finalist'}, format='json')
        self.assertEqual(res_patch.status_code, status.HTTP_200_OK)
        self.award.refresh_from_db()
        self.assertEqual(self.award.rank, 'Top 3 Finalist')

        # Cannot delete
        res_del = self.client.delete(detail_url)
        self.assertEqual(res_del.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_has_full_crud_on_award(self):
        self.client.force_authenticate(user=self.superuser)
        list_url = reverse('api-award-list')

        # Create
        data = {
            'title': 'Sistech Business Case Winner',
            'rank': '1st Winner',
            'issuer': 'Sistech 2026',
            'category': 'business',
            'year': '2026',
            'description': 'Winning business pitch competition'
        }
        res_post = self.client.post(list_url, data, format='json')
        self.assertEqual(res_post.status_code, status.HTTP_201_CREATED)
        new_id = res_post.data['id']

        # Retrieve
        detail_url = reverse('api-award-detail', kwargs={'pk': new_id})
        res_get = self.client.get(detail_url)
        self.assertEqual(res_get.status_code, status.HTTP_200_OK)
        self.assertEqual(res_get.data['year'], '2026')

        # Update
        res_patch = self.client.patch(detail_url, {'rank': 'Grand Champion'}, format='json')
        self.assertEqual(res_patch.status_code, status.HTTP_200_OK)
        self.assertEqual(res_patch.data['rank'], 'Grand Champion')

        # Delete
        res_del = self.client.delete(detail_url)
        self.assertEqual(res_del.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Award.objects.filter(id=new_id).exists())

    def test_award_validation_invalid_year(self):
        self.client.force_authenticate(user=self.superuser)
        list_url = reverse('api-award-list')
        bad_data = {
            'title': 'Test Award',
            'rank': 'Winner',
            'issuer': 'Test Issuer',
            'category': 'academic',
            'year': '24', # Invalid year format (not 4 digits)
            'description': 'Valid description'
        }
        response = self.client.post(list_url, bad_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('year', response.data)

    def test_award_xss_sanitization(self):
        self.client.force_authenticate(user=self.superuser)
        list_url = reverse('api-award-list')
        data = {
            'title': '<em>UI Business Winner</em>',
            'rank': '<strong>1st Place</strong>',
            'issuer': 'UI',
            'category': 'business',
            'year': '2026',
            'description': 'Deskripsi prestasi'
        }
        res = self.client.post(list_url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['title'], 'UI Business Winner')
        self.assertEqual(res.data['rank'], '1st Place')
