#desafio84 lista composta e analise de dados.
# Faça um progama que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final mostre;
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
status = True
lista = []
dado = []
maior = menor = 0
while status:
    dado.append(str(input('Nome:').strip().upper())) # adiciona o nome em uma lista temporaria/ dado[0] Nome
    dado.append(float(input('Peso:'))) # adiciona o peso em uma lista temporaria / dado[1] Peso
    if len(lista) == 0:        # Se eu nao cadstrei ninguem ainda na lista
        maior = dado[1]        # Maior vai ser o primeiro peso digitado na lista temporaria dado
        menor = dado[1]        # Menor vai ser o primeiro peso digitado na lista temporaria dado
    else:                      # Se não for o primeiro: verificar
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])              # adiciona uma copia do dado a lista principal
    dado.clear()                       # Apaga os dado da lista temporaria, para começar de novo
    pergunta1 = ' '
    while pergunta1 not in 'SN':
        pergunta1 = str(input('Quer continuar?[S/N]:').strip().upper()[0])
        if pergunta1 in 'N':
            status = False

print(f'Os dados foram {lista}')                                      # (A 70)(B 55)(C 60)
print(f'{len(lista)} pessoas cadastradas')  # A) # Comprimento da lista.  1  .   2  .  3  .
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for pessoa in lista:                        # para cada pessoa na lista. pessoa[0] nome / pessoa[1] peso
    if pessoa[1] == maior:                  # Se o peso for = maior
        print(f'[{pessoa[0]}]', end='')               # Mostre nome das pessoas.
print()
print(f'O menor peso foi de {menor}Kg', end='')
for pessoa in lista:                        # para cada pessoa na lista. pessoa[0] nome / pessoa[1] peso
    if pessoa[1] == menor:                  # para cada peso menor = menor
        print(f'[{pessoa[0]}] ', end='')               # Mostre nomes das pessoas
print()
print('Fim')



