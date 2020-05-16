# desafio072 Número por extenso
# Crie um progama que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu progama deverá ler um número pelo teclado(entre 0 e 20) e mostralo por extenso.
numero = 0
numero_tupla = ('Zero', 'Um', 'Dois', 'Treis', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
                  'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove',
                  'Vinte')
status = True
while status:
    numero = int(input('Digite um número entre [0 e 20]: '))
    if numero >= 0 and numero <= 20:
        print(f'Voce digitou o número {numero_tupla[numero]}')
    else:
        print('Tente novamente!')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]:')).strip().upper()[0]
        if opcao == 'N':
            status = False
print('Volte sempre!')
