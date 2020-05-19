# Aula 19 Dicionarios.  É assim que tratamos os dicionarios
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}       # Não precisa de append em dicionarios
pessoas['nome'] = 'Leandro'                 # Modificando o conteudo , Gustavo por Leandro
pessoas['peso'] = 98.5                      # Adicionando um titulo, e o conteudo dele
#del pessoas['sexo']                         # Remove o titulo (sexo)
for k, v in pessoas.items():
    print(f'{k} = {v}')                     # K = titulos  /   v = conteudo dos titulos
