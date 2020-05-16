#desafio078 maior e menor valores na lista
# faça um progama que leia 5 valores númericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas recpectivas posiçoes na lista.
lista_numero = []
maior = menor = 0
for c in range(0, 5):
    lista_numero.append(int(input(f'Digite  o {c}º valor:')))
    if c == 0:
        maior = lista_numero[c]
        menor = lista_numero[c]
    else:
        if lista_numero[c] > maior:
            maior = lista_numero[c]
        if lista_numero[c] < menor:
            menor = lista_numero[c]

print(f'Voce digitou os valores {lista_numero}')
print(f'O maior valor digitado foi {maior} nas posiçoes ', end='')
for indice, valor in enumerate(lista_numero):   # For vai varrer a lista inteira enumerando os valores
    if valor == maior:
        print(f'{indice}...', end='')     # Indice é a posição do numero
print()
print(f'O menor valor digitado foi {menor} nas posiçoes ', end='')
for indice, valor in enumerate(lista_numero):   # Repetir a varredura para enumerar os valores
    if valor == menor:
        print(f'{indice}...', end='')
print()





