# desafio082 Dividindo valores em várias listas
# Crie um progama que vai ler varios números e colocar em uma lista. Depois disso crie duas listas extras
# que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteudo das tres listas geradas.
lista_geral = []
lista_par = []
lista_impar = []
status = True
while status:
    numeros = int(input('Digite um número:'))
    opcao = ' '
    while opcao not in 'SN':                 # Enquanto a opcao não estiver em "S/N' repete o laço
        opcao = str(input('Quer continuar?[S/N]:').strip().upper()[0])
        if opcao in 'N':     # Se a opção for não. encerrar progama
            status = False
    lista_geral.append(numeros)    # adicionar os números na lista geral
    if numeros % 2 == 0:      # se os numeros forem pares colocar na lista de pares
        lista_par.append(numeros)
        lista_par.sort()
    elif numeros % 2 == 1:    # Se os numeros forem impares, colocar na lista de impares
        lista_impar.append(numeros)
        lista_impar.sort()
print(f'A lista geral é: {lista_geral}')
print(f'A lista de números pares é: {lista_par}')
print(f'A lista de números impares é: {lista_impar}')
