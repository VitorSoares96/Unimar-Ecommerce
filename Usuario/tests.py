# Usuario/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class UsuarioModelsAndSignalsTest(TestCase):
    """Testa os modelos e sinais do app Usuario."""

    def test_profile_is_created_for_new_user(self):
        """Verifica se um Profile é criado automaticamente para um novo User."""
        self.assertEqual(Profile.objects.count(), 0)
        user = User.objects.create_user(username='test_user', password='123', first_name='Nome Teste')
        
        # O signal deve ter criado um perfil
        self.assertEqual(Profile.objects.count(), 1)
        
        profile = Profile.objects.first()
        self.assertEqual(profile.usuario, user)
        self.assertEqual(str(profile), 'Nome Teste')
        self.assertFalse(profile.vendedor)
        self.assertEqual(profile.bios, 'Olá, este é o meu Perfil!')