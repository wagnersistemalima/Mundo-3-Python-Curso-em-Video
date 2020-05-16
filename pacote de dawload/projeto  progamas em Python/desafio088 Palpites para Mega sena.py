# desafio088 Palpites para Mega sena
# Faça um progama que ajude um jogador da Mega Sena a criar palpites. O progama vai perguntar quantos jogos
# serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
dados = []
lista_principal = []
print('-='*30)
print('{:^60}'.format('Joga na Mega sena'))
print('-='*30)
pergunta = int(input('Quantos jogos você quer o palpite?'))
total = 1                                  # Controlador das Quantidade de palpites
while total <= pergunta:
    cont = 0                               # Controlador da quantidade de numeros
    while True:
        numero = randint(1, 60)
        if numero not in dados:            # Se o número não estiver na lista
            dados.append(numero)           # Guardar cada palpite de 6 numeros em uma lista temporaria dados
            cont = cont + 1                # Controlador da quantidade de numeros
        if cont >= 6:
            break
    dados.sort()                            # Ordenar a lista temporaria na ordem crescente
    lista_principal.append(dados[:])        # Adicionar uma copia de dados na lista principal a cada palpite
    dados.clear()                           # Depois apagar dados, para receber um novo palpite
    total = total + 1                       # Controlador de quantidades de palpites
print('-='*3, f'Sorteando {pergunta} Jogos', '=-'*3)
for indice, palpite in enumerate(lista_principal):     # Para cada indice: ex 1ºpalpite/ 2ºpalpite
    print(f'Jogo {indice+1}: {palpite}')
    sleep(1)
print('-='*3, '< Boa Sorte! >', '-='*3)

