# Aula 19 Dicionarios.  É assim que tratamos os dicionarios
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
for k in  pessoas.keys():  #Para cada uma das chaves: acessar titulos  Acessar as chaves, valores e os itens por laços
    print(k)

print('-='*10)

for k in pessoas.values():    # Acessar o conteudo do dicionario
    print(k)

print('-='*10)

for k, v in pessoas.items():   # Acessar os itens do dicionario onde k = titulos e v = conteudo
    print(f'{k} = {v}')             # K = titulos  /   v = conteudo dos titulos