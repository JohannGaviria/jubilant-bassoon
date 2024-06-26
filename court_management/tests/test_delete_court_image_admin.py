from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from authentication.models import User
from court_management.models import SurfaceType, CourtStatus, CourtType, Court, CourtImage


# Tests para eliminar imagen de las canchas
class DeleteCourtImageAdminTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            full_name="test Admin",
            email="admin@example.com",
            password="adminpassword",
            phone="+57 301 203 4354",
            birth_date="1990-01-01"
        )
        self.client.force_authenticate(user=self.admin_user)
        self.court_status = CourtStatus.objects.create(status="Available")
        self.surface_type = SurfaceType.objects.create(type="Grass")
        self.court_type = CourtType.objects.create(type="Soccer")
        self.court = Court.objects.create(
            name="Emerald Field",
            code="CZ501",
            size="20x40",
            location="1234 Evergreen Avenue, Springfield, Illinois",
            price_hour="100.00",
            description="Emerald Field is a premier sports facility located in Springfield, Illinois.",
            surface_type=self.surface_type,
            court_status=self.court_status,
            court_type=self.court_type
        )
        self.court_image = CourtImage.objects.create(
            court=self.court,
            image=SimpleUploadedFile(name='test_image.jpg', content=open('uploads/test_image_1.jpg', 'rb').read(), content_type='image/jpeg')
        )
        self.url = reverse('delete_court_image_admin', args=[self.court_image.id])


    # Prueba exitosa
    def test_successfully(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertFalse(CourtImage.objects.filter(id=self.court_image.id).exists())


    # Prueba con imagen de cancha que no existe
    def test_nonexistent_court_image(self):
        nonexistent_image_url = reverse('delete_court_image_admin', args=[999])
        response = self.client.delete(nonexistent_image_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba sin autenticación
    def test_authentication(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
