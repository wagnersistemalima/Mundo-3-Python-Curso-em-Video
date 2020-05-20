# Aprimore o desafio 093 para que ele funcione com varios jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

lista_time = []
estrutura = {}
lista = []                               # Guarda os gols
while True:
    estrutura.clear()                                       # limpar o dicionario guando começar o laço
    estrutura['nome'] = str(input('Nome do Jogador: ').title())
    quantidade_partidas = int(input(f'Quantas partidas {estrutura["nome"]} jogou? '))
    lista.clear()                                           # limpar a lista 
    for c in range(1, quantidade_partidas + 1):
        lista.append(int(input(f'Quantidades de gols na {c}º partida? ')))
    estrutura['gols'] = lista.copy()
    estrutura['total'] = sum(lista)
    lista_time.append(estrutura.copy())
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar [S/N] ').strip().upper()[0])
    if pergunta == 'N':
        break

print('-='*30)                                              # mostrar os resultados 
print('cod ', end='')                            # cabeçalho:
for i in estrutura.keys():                         # para cada titulo na estrutura titulos
    print(f'{i:<15}', end='')                   # formatado a esquerda 
print()                                             # sempre com quebra linha
print('-'*40)
for k, v in enumerate(lista_time):
    print(f'{k:>3} ', end='')                    # formatação da chave ou titulo alinhado a direita
    for d in v.values():                        # dado e valor
        print(f'{str(d):<15}', end='')
    print()                                         # sempre com quebra linha 
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 p/ parar) '))              # chave de buscar
    if busca == 999:
        break
    if busca >= len(lista_time):                        # len vai ser a quantidade de dicionaros = jogadores
        print(f'Erro! Não existe jogador com codigo {busca}')
    else:
        print(f' -- Levantamento do jogador {lista_time[busca]["nome"]}:')
        for i, g in enumerate(lista_time[busca]["gols"]):
            print(f'     No jogo {i+1} fez {g} gols')
    print('-='*40)
print('<< Volte sempre >>')




