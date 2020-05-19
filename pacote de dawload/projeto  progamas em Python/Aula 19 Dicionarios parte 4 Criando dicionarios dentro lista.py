# Aula 19 Dicionarios.  É assim que tratamos os dicionarios
brasil = []                                          # Criando uma lista   [0] [1] [2] ex:
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}    # Criando dicionarios
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}         # Criando dicionarios
brasil.append(estado1)                          # Adicionando os dicionarios a lista
brasil.append(estado2)
print(estado1)                                  #1º mostra o dicionario1
print('-='*20, '1º')
print(estado2)                                  #2º mostra o dicionario2
print('-='*20, '2º')
print(brasil)                        #3º mostra a lista toda, os dicionarios (1º e 2º estado)
print('-='*40, '3º')
print(brasil[0])                     #4º mostra o primeiro dicionario dentro da lista[0] ( 1º estado)
print('-='*20, '4º')
print(brasil[0]['uf'])               #5º mostra [0] 1º dicionario, e o conteudo do titulo uf = cidade
print('-='*20, '5º')
print(brasil[1]['sigla'])            #6º mostra [1]  2º dicionario, e o conteudo do titulo sigla = SP
print('-='*20, '6º')



