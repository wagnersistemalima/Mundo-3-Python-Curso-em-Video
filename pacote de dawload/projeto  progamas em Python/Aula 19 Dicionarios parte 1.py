# Aula 19 Dicionarios.  É assim que tratamos os dicionarios
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(pessoas['idade'])
print(pessoas['sexo'])
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')  # Utilizar aspas duplas para a localização [" "]
print(pessoas.keys())                     # nome / sexo / idade
print(pessoas.values())                   # Gustavo / M / 22
print(pessoas.items())                    #Composição de elementos: lista e treis tuplas


