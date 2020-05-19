#desafio092 Cadastro de trabalhador em python
# Crie um progama que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em
# um dicionario se por acaso a ctps for diferente de zero, o dicionario receberá tambem o ano de contratação
# e o salario. Calcule e acrecente, alem da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime                                 # Importar o ano atual
estrutura = {}
ano_atual = datetime.now().year                            # ano atual
estrutura['nome'] = str(input('Nome: ').strip().upper())                    # criando titulo e conteudo
ano_nascimento = int(input('Ano de nascimento: '))                      
estrutura['idade'] = ano_atual - ano_nascimento                         # calculando a idade do usuario
estrutura['ctps'] = int(input('Carteira de trabalho ( 0 não tem) '))
if estrutura['ctps'] != 0:                     # se for diferente de 0 adicionar outros dados
    estrutura['contratação'] = int(input('Ano de contratação: '))
    estrutura['salario'] = float(input('Salario: R$'))
    estrutura['aposentadoria'] = estrutura['idade'] + (estrutura['contratação'] + 35) - ano_atual

print('-='*20)
for k, v in estrutura.items():                 # mostrar titulo e conteudo da estrutura
    print(f'  - {k} tem o valor {v}')
print('-='*20)
    
        


