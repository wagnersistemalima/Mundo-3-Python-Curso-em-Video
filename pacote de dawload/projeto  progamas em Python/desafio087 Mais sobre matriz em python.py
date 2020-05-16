# desafio087 Mais sobre matriz em python
# desafio086 Matrize em python
# Crie um progama que crie uma matriz de dimensão 3 x 3 e preencha com valores lido pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados. / B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_coluna = maior = 0
for linha in range(0, 3):                  # preenchendo a matriz
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para linha {linha} e para coluna {coluna}: '))
print('-='*30)
for linha in range(0, 3):                  # mostrar a matriz na tela
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')#formatação vai poder encaixar numeros com treis casas dec
        if matriz[linha][coluna] % 2 == 0:     # Se o elemento que acabou de ser exibido for par
            soma_par = soma_par + matriz[linha][coluna]
    print()                                           # quebra linha para deixar numeros na matriz quadrada                                     # Se não tiver este quebra linha, vai mostrar os numeros numa reta
print('-='*30)
print(f'A soma dos valores pares é {soma_par}')           # Resposta A)
for linha in range(0, 3):  # A coluna e fixa, so a linha vai variar
    soma_coluna = soma_coluna + matriz[linha][2]     # soma dos itens da terceira coluna
print(f'A soma dos valores da terceira coluna é {soma_coluna}')   # Resposta B)
for coluna in range(0, 3):  # A linha é fixa, so a coluna vai variar
    if coluna == 0:                     # Sinal que está na primeira coluna/   coluna[0]
        maior = matriz[1][coluna] # O maior elemento e sempre o primeiro, se a coluna for a primeira, entaõ maior e ela
    elif matriz[1][coluna] > maior: # se não nao for a primeira, comparamos com o maior da anterior, se for maior troca
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior}')       # Resposta C)








