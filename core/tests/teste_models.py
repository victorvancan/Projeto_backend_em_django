import uuid
from django.test import TestCase
from model_mommy import mommy
from core.models import get_file_path

class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServicoTestCase(TestCase):

    def setUp(self):
        self.servicos = mommy.make('Servico')

    def test_str(self):
        self.assertEquals(str(self.servicos), self.servicos.servicos)

class CargoTestCase(TestCase):

    def setUp(self):
        self.cargos = mommy.make('Cargo')

    def test_str(self):
        self.assertEquals(str(self.cargos), self.cargos.cargos)


class FuncionarioTestCase(TestCase):

    def setUp(self):
        self.funcionarios = mommy.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(self.funcionarios), self.funcionarios.nome)


class FeatureTestcase(TestCase):

    def setUp(self):
        self.features = mommy.make('Feature')

    def test_str(self):
        self.assertEquals(str(self.features), self.features.features)