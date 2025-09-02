from typing import List, TypedDict

class Item(TypedDict):
  nome: str
  preco: float

class CarrinhoDeCompras:
  def __init__(self):
    self.itens = list[Item]()
    self.desconto = 0

  def adicionar_item(self, nome: str, preco: float):
    self.itens.append(Item(nome=nome, preco=preco))

  def aplicar_desconto(self, percentual: float):
    self.desconto = percentual

  def total(self):
    subtotal = sum(item["preco"] for item in self.itens)
    if self.desconto:
        return subtotal - (subtotal * self.desconto / 100)
    return subtotal