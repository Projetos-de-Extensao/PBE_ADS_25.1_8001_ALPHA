from django.test import TestCase
from .models import Administrador

class AdministradorModelTest(TestCase):
    def test_criacao_administrador(self):
        admin = Administrador.objects.create(
            nome="Marcelina Oliveira",
            idAdministrador=1.01,
            enderecoEmail="marcelinaoliv@example.com",
            senha="senha123"
        )
        self.assertEqual(admin.nome, "Carlos Silva")
      
# Create your tests here.
