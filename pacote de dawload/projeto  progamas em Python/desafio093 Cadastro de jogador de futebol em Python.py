# desafio093 cadastro de jogador de futebol
# Crie um progama que gerencie o aproveitamento de um jogador de futebol. O progama vai ler o nome do jogador  e  quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um discionario, incluindo o total de gols feitos durante o campeonato.

estrutura = {}
lista = []                               # Guarda os gols
estrutura['nome'] = str(input('Nome do Jogador: '))
quantidade_partidas = int(input(f'Quantas partidas {estrutura["nome"]} jogou? '))
for c in range(1, quantidade_partidas + 1):
    lista.append(int(input(f'Quantidades de gols na {c}º partida? ')))
estrutura['gols'] = lista.copy()
estrutura['total'] = sum(lista)
print('-='*30)
print(estrutura)
print('-='*30)
for k, v in estrutura.items():                      # para cada titulo (k) moste seu conteudo (v)
    print(f'O campo {k} tem o valor {v}')



