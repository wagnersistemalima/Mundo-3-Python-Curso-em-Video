# desafio073 Tuplas com times de futebol
# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol.
# na ordem de colocação. depois mostre.
# A) Os 5 primeiros / B) Os ultimos 4 colocados. / C) Times em ordem alfabetica
# D) Em que posição está o time da Chapecoense.

tupla_time = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo',
'Flumimense', 'Sport Recife', 'Ec Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-'*30)
print(f'Lista de times do brasileirão {tupla_time}')
print('-'*30)
print(f'Os 5 primeiros colocados são: {tupla_time[0:5]}')
print('-'*30)
print(f'Os ultimos 4 colocados são: {tupla_time[-4:]}')
print('-'*30)
print(f'Os times em ordem alfabetica é {sorted(tupla_time)}') # Ordem alfabetica
print(f'O Chapecoense está na {tupla_time.index("Chapecoense")+1}º posição')
# 0 a 8 Chapecoense ta na 7 pois o 0 conta como 1. para ageitar soma + 1
