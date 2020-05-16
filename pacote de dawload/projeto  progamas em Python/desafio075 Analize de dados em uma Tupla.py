# desafio075 Analize de dados em uma Tupla
# Desenvolva um progama que leia quatros valores pelo teclado e guardeo-os em uma tupla. No final mostre:
# A) Quantas vezes apareceu o valor 9. / B) em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares

numeros = (int(input('Digite um valor:')), # Guardando valores em uma tupla numero
          int(input('Digite um valor:')),
          int(input('Digite um valor:')),
          int(input('Digite um valor:')))
print(numeros)
print(f'O número 9 apareceu {numeros.count(9)} vezes')     # contando quantas vezes o 9 apareceu # A)
if 3 in numeros: # condicao para index, pois se ele nao achar 3 na tupla ele dar erro. Se 3 estiver na tupla!
    print(f'O primeiro valor 3 foi digitado na {numeros.index(3) + 1}º posição')  # B)
else: # Se 3 nao estiver
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os numeros pares foram ', end='')
for n in numeros:   # Para cada numero, dentro de numero
    if n % 2 == 0:
        print(n, end='  ')

