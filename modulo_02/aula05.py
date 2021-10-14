'''
SETS ou conjuntos = suportam apenas elementos unicos
add (adiciona), update (atualiza), clear, discard
union (une)
intersection & (todos os elementos presentes no dois sets)
difference (elementos apenas no set da esquerda)
symmetric_difference ^(elementos que estçao nos dois sets, mas não em ambos)
'''

s1 = {1,2,3,4,5}
s2 = set()
s2.add(2)
s2.discard(2)
s2.update('a','python')

print(s2)
## sets não podem conter elementos duplicados
l1 = [1,1,2,3,1,2,3,5,6,'Joys','João']
l1 = set(l1)
print(l1)

l1 = list(l1)
print(l1)

## intersection

c1 = {1,1,2,5,2,18}
c2 = {1,2,3,4,5,6}

c3 = c1 | c2
c3 = c1 & c2 #presente em ambos os sets
c3 = c1 - c2
c3 = c2 - c1
c3 = c2 ^ c1
print(c3)
