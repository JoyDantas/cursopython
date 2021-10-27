from pessoa import Pessoa

p1 = Pessoa('Joys',26)
p2 = Pessoa('Felipe',24)

p1.comer('banana')
p1.falar('mapa astral')
p1.parar_comer()
p1.falar('mapa astral')
p1.estudar('python')
p1.parar_falar()
p1.estudar('python')
p2.falar('Amor')
p2.comer('batata frita')
p2.parar_falar()
p2.comer('batata frita')

print(p1.get_ano_nascimento())