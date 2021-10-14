carrinho = []

carrinho.append(('Produto 1', 30.50))
carrinho.append(('Produto 2', '10'))
carrinho.append(('Produto 3', 130))
carrinho.append(('Produto 4', 49))
carrinho.append(('Produto 5', 25))

total = sum([float(y) for x,y in carrinho])

print(total)