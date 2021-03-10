from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Victor vancan',
            'email': 'victor@gmail.com',
            'assunto': 'Um assunto qualquer',
            'mensagem': 'Uma mensagem qualquer',
        }
        self.client = Client()

    def test_from_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)


    def test_form_invalid(self):
        dados = {
            'nome': 'Victor vancan',
            'email': 'victro@gmail.com'
        }
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)
