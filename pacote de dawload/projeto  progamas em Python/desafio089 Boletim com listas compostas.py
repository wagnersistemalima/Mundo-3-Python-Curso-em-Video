# desafio089 Boletim com listas compostas
# Crie um progama que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta
# No final, mostre um boletim contendo a média de cada um e permita que o usuario possa mostrar as notas de cada
# aluno individualmente.
lista_principal = list()
status = True
soma = 0
while status:
    nome = str(input('Aluno:').strip().upper())
    nota1 = float(input('1º nota:'))
    nota2 = float(input('2º nota:'))
    media = (nota1 + nota2) / 2
    lista_principal.append([nome, [nota1, nota2], media])    # nome[0] nota1[1] nota2[1] media[2]
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar?[S/N]:').strip().upper())
    if pergunta in 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')             # Formatação para mostrar boletim
print('-'*26)
for i, a in enumerate(lista_principal):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')               # Formatação para mostrar indice / nome / media
while True:
    print('-='*30)
    opc = int(input('Mostrar notas de qual aluno? (999 interromper):'))
    if opc == 999:
        print('Finalizando..')
        break
    if opc <= len(lista_principal) - 1:  # Aluno[0] Aluno[1] Aluno[2] <= quantidade de alunos cadasrados
        print(f'Notas de {lista_principal[opc][0]} são {lista_principal[opc][1]}')
print('Volte sempre!')