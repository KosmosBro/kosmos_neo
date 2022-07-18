# from django.test import TestCase
#
#
# class TestCategoryApi(APITestCase):
#     @classmethod
#     def setUp(cls):
#         cls.user = User.objects.create_superuser(username='kosmos_admin', password='1234kosmos_admin')
#         cls.company = Category.objects.create(name='Company', id=2)
#
#     def test_category_api(self):
#         self.client.login(username='kosmos_admin', password='1234kosmos_admin')
#
#         url = '/api/category/'
#
#         data = {
#             'name': 'title',
#             'company': self.company.id
#         }
#
#         response = self.client.get(url, data=data, format='json')
#         self.assertEqual(response.status_code, 200)
#
#     def test_category_add_api(self):
#         self.client.login(username='kosmos_admin', password='1234kosmos_admin')
#
#         url = '/api/category/'
#
#         data = {
#             'name': 'title1',
#             'company': [self.company.id]
#         }
#         response = self.client.post(url, data=data, format='json')
#         self.assertEqual(response.status_code, 201)
#
#     def test_category_update_api(self):
#         self.client.login(username='kosmos_admin', password='1234kosmos_admin')
#
#         data = {
#             'name': 'Company',
#             'company': [self.company.id]
#
#         }
#
#         response = self.client.put('/api/category/2/', data, format='json')
#         self.assertEqual(response.status_code, 200)
#
#     def test_category_delete_api(self):
#         self.client.login(username='kosmos_admin', password='1234kosmos_admin')
#
#         data = {
#             'name': 'Company',
#             'company': [self.company.id]
#
#         }
#
#         response = self.client.delete('/api/category/2/', data, format='json')
#         self.assertEqual(response.status_code, 204)
#
#     def test_category_api_fail(self):
#         self.client.login(username='kosmos_admin', password='1234kosmos_admin')
#
#         url = '/api/category/'
#
#         data = {
#             'name': '@',
#             'company': [self.company.id]
#
#         }
#
#         with self.assertRaises(TypeError):
#             Category.objects.create(data, url)
