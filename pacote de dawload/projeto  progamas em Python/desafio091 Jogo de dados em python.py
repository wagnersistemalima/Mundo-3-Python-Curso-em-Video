# desafio091 Jogo de dados em python
# Crie um progama onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em
# um dicionario. No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero
# de dado
from random import randint
from time import sleep
from operator import itemgetter            # função para ordenar dicionario
estrutura = {}
estrutura['jogador1'] = randint(0, 6)
estrutura['jogador2'] = randint(0, 6)
estrutura['jogador3'] = randint(0, 6)
estrutura['jogador4'] = randint(0, 6)
estrutura_ordenada = []                    # criando outro dicionario para ordenar o primeiro
print('-='*20)
for t, c in estrutura.items():             # para cada titulo (t), e conteudo (c) mostre titulo e conteudo
    print(f'{t} tirou {c} no dado')
    sleep(1)
estrutura_ordenada = sorted(estrutura.items(), key=itemgetter(1), reverse=True) # (1) ordena conteudo (0) ordena titulo

print('-='*20)
print('== Ranking dos Jogadores ==')

for i, v in enumerate(estrutura_ordenada):  # para cada indice e valor mostre na lista ordenada v[0] jogador [v1] numero
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)



