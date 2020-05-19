# Aula 19 Dicionarios.  É assim que tratamos os dicionarios
estado = dict()                               # Criando dicionario
brasil = list()                               # Criando lista
for c in range(0, 3):                         # lendo o input 3 x
    estado['uf'] = str(input('Unidade federativa: ').strip().upper())   #
    estado['sigla'] = str(input('Sigla do Estado: ').strip().upper())   #
    brasil.append(estado.copy()) # .copy()  metodo intero python para fazer uma copia do dicionario/ [:] não fuciona
print(brasil)
print('-='*20, '1º')
for e in brasil:                 # Para cada dicionario (e) em lista, mostre dicionario
    for k, v in e.items():       # para cada titulo (k), e o conteudo dele (v) mostre os itens dos dicionarios (e)
        print(f'O campo {k} tem valor {v}')
print('-='*20, '2º')

for e in brasil:                 # para cada dicionario (e) em lista, mostre dicionario
    for v in e.values():         # para cada conteudo (v) dentro de dicionario (e)
        print(v, end=' ')
    print()
