"""Exercicio do beecrwod 1085, nele rodamos 100 valores de entreada, fizemos a comparação com a
passada e vimos qual o maior numero informado e sua posição entre as 100 entradas"""

maior = int(input())
posicao = 1

for i in range(2, 101):
    x = int(input())
    if x > maior:
        maior = x
        posicao = i

print(maior)
print(posicao)
