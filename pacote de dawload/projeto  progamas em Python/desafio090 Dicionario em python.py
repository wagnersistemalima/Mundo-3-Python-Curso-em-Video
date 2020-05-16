# desafio090 Dicionario em python
# Faça um progama que leia nome e media de um aluno, guardando tabêm a situação em um dicionario.
# No final, mostre o conteúdo da estrutura na tela.
estrutura = {}

estrutura['nome'] = str(input('Nome:').strip().title()) # .title() deixa a primeira letra em maiusculo de cada nome
estrutura['media'] = float(input(f'Média de aluno {estrutura["nome"]}: '))
print('-='*20)

if estrutura["media"] >= 7.0:
    estrutura['situação'] = 'Aprovado'
elif estrutura["media"] >= 5 and estrutura["media"] < 7:
    estrutura['situação'] = 'Recuperação'
else:
    estrutura['situação'] = 'Reprovado'

for t, c in estrutura.items():            # para cada titulo (t), conteudo (c) / .items() mostre titulo e conteudo
    print(f'{t} é igual a {c}')




#print(f'Nome é igual a {estrutura["nome"]}')                  # [nome] tem que usar Duas aspas
#print(f'A media e igual a {estrutura["media"]:.1f}')          # [media] tem que usar Duas aspas
#print(f'Situação é igual a {estrutura["situação"]}')


