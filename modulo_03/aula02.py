## Getter e Setter

## GETTER = GET/ retorna o valor configurado no setter (.)
## SETTER = SET / COnfigurando um valor (=)

# Getter e Setters são uma especie de proteção para o seus dados, onde você pode configurar alguma mudança no seu código,
# sem comprometer o que já foi feito anteriormente.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    ## getter para o nome
    @property
    def nome(self):
        return self._nome

    ## setter para o nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor.upper()

    ## getter
    @property
    def preco(self):
        return self._preco  ## por convenção eu não posso utilizar mais a variavel 'preço', por isso adicionamos o _

    # setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor


p1 = Produto('Camisa Nike', 50)
p1.desconto(15)
p2 = Produto('Jaqueta Renner', 'R$120')
p2.desconto(25)

print(p1.nome, p1.preco)
print(p2.nome, p2.preco)
