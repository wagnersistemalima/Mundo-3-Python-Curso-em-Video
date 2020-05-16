# desafio079 Valores únicos em uma lista
# Crie um progama onde o usuário possa digitar vários valores numéricos e cadastreo-os em uma lista
# Caso o número já exista la dentro, ele não será adcionado. No final, serão exibidos todos os
# valores únicos digitados, em ordem crescente.
status = True
lista_valores = []
while status:
    adcionar_valores = int(input('Digite um valor para adcionar na lista:').strip())
    if adcionar_valores not in lista_valores:  # Se o valor não estiver na lista adicionar
        lista_valores.append(adcionar_valores)
        lista_valores.sort()
        print('Numero adicionado com sucesso!')
        print(lista_valores)
    else:
        print('Numero duplicado! Não vou adicionar.')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar adicionando valores:[S/N]').strip().upper()[0])
    if opcao in 'N':    # Se a opcao estiver em 'N' Encerrar sistema
        status = False
print('-='*30)
print(f'Você digitou os números {lista_valores}')
print('Fim')



