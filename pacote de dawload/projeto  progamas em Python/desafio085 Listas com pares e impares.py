# desafio085 Listas com pares e impares
# Crie um progama onde o usuário possa digitar sete valores, numericos e cadastrios em uma lista unica,
# Que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem
# crescente.
lista = [[], []]
#       [0]  [1]
#      [par] [impar]
for c in range(1, 8):
    valor = int(input('Digite um valor:'))
    if valor % 2 == 0:
        lista[0].append(valor)             # Adicionar numero na posição 0 lista = [par]
        lista[0].sort()                    # Ordem crescente par
    elif valor % 2 == 1:
        lista[1].append(valor)             # Adicionar número na posição 1 lista = [Impar]
        lista[1].sort()                    # Ordem crescente impar
print(f'Lista principal {lista}')
print(f'Lista de numeros pares {lista[0]}')
print(f'Lista de numeros impares {lista[1]}')













