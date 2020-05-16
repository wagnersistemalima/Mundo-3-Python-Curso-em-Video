# desafio086 Matrize em python
# Crie um progama que crie uma matriz de dimensão 3 x 3 e preencha com valores lido pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):          # For de alimentação da matriz linha
    for coluna in range(0, 3):      # For de alimentação da matriz coluna
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha}, {coluna}: '))
print('-='*30)
for linha in range(0, 3):          # For para mostrar a estrutura na tela
    for coluna in range(0, 3):      # For para mostrar a estrutura na tela
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()


