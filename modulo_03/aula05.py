from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camisa Nike', 99)
p2 = Produto('Celular', 1900)
p3 = Produto('Relógio Casio', 500)

carrinho.inserir_produto(p1)

