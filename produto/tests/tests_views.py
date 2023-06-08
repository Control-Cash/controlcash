from django.test import TestCase
from django.urls import reverse
from produto.models import Produto
# Create your tests here.

class ProdutoViewVizualizarProduto(TestCase):
    @classmethod
    def setUpTestData(cls):
        num_produtos = 10
        preco_inicial = 1.0

        for produto_id in range(num_produtos):
            Produto.objects.create(
                nome=f'Guilherme {produto_id}',
                preco_venda=produto_id,
                descricao=f'Descrevendo o produto {produto_id}',
                quantidade_estoque=preco_inicial + preco_inicial
            )
        
    def test_view_url_exists_at_desired_location(self):
        reposta = self.client.get('/produto/')
        self.assertEqual(reposta.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resposta = self.client.get(reverse('homeProduto'))
        self.assertEqual(resposta.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('homeProduto'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
