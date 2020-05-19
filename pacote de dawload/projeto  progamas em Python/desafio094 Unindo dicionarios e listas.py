#desafio094 Unindo dicionarios e listas
# Crie um progama que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre: A) Quantas pssoas cadastradas
# B) A média de idade / C) Uma lista com mulheres / D) Uma lista com idade acima da média
lista = []
dicionario = {}
soma = 0
media = 0
while True:
    dicionario['nome'] = str(input('Nome: ').strip().upper())
    while True:
        dicionario['sexo'] = str(input('Sexo [M/F} ').strip().upper()[0])
        if dicionario['sexo'] in 'MF':
            break
    dicionario['idade'] = int(input('Idade: '))
    soma = soma + dicionario['idade']
    lista.append(dicionario.copy())
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar [S/N] ').strip().upper()[0])
    if pergunta == 'N':
        break
media = soma / len(lista)
print('-='*30)
print(f'A) Aõ todo foram {len(lista)} pessoas cadastradas')      # a)
print(f'B) A média de idade é de {media:.2f} anos')              # b)
print('C) As mulheres cadastradas foram ', end='')

for t in lista:                                     #c) para cada titulo na lista mostre     
    if t['sexo'] in 'F':                            # se o titulo sexo estiver em F
        print(f'{t["nome"]}', end=',')                       # mostre o conteudo do titulo nome
print()
print('D) lista das pessoas que estão acima da media: ')
for t in lista:                                 
    if t['idade'] >= media:                         # se o titulo idade for maior que a media das idades    
        print('   ')
        for k, v in t.items():                      # t dicionario
            print(f'{k} = {v}; ', end='')                     # mostre (k) titulo e (v) conteudo
        print()
print('<<..Fim!..>>')






            
        
    