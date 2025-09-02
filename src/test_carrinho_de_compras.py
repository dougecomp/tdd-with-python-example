from unittest import TestCase

from .carrinho_de_compras import CarrinhoDeCompras

class TestCarrinhoDeCompras(TestCase):
  def test_adicionar_item_e_calcular_total(self):
    carrinho = CarrinhoDeCompras()

    carrinho.adicionar_item("Livro", 50.0)
    carrinho.adicionar_item("Caneta", 5.0)
    
    self.assertEqual(carrinho.total(), 55.0)

  def test_aplicar_desconto(self):
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Mochila", 200.0)

    carrinho.aplicar_desconto(10)  # 10%

    self.assertEqual(carrinho.total(), 180.0)

  def test_itens_no_carrinho(self):
    carrinho = CarrinhoDeCompras()
    
    carrinho.adicionar_item("Livro", 50.0)
    carrinho.adicionar_item("Caneta", 5.0)
    carrinho.adicionar_item("Mochila", 200.0)
    carrinho.adicionar_item("Camisa", 100.0)
    
    self.assertEqual(carrinho.itens, [
      {"nome": "Livro", "preco": 50.0},
      {"nome": "Caneta", "preco": 5.0},
      {"nome": "Mochila", "preco": 200.0},
      {"nome": "Camisa", "preco": 100.0}
    ])