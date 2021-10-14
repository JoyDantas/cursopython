string = '0123456789012345678901234567890123456789'

n=10
comp = [string[i:i + n]for i in range(0,len(string),n)]
retorno = '.'.join(comp)
print(comp)
print(retorno)


