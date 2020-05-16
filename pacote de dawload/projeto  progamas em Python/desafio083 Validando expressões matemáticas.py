# desafio083 Validando expressões matemáticas
# Crie um progama onde o usuario digite uma expressão qualquer que use parenteses. seu aplicativo
# deverá analizar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = input('Digite a expressão: ').strip()
print(expressao)
parentese1 = expressao.count('(')    # Contar quantas vezes aparece o elemento (
parentese2 = expressao.count(')')    # Contar quantas vezes aparece o elemento )
if parentese1 != parentese2:         # se a quntidade de parentese fo um numero impa ta errado
    print('Expressão invalida!')
elif parentese1 == parentese2:       # se a quantidade de parentese for par, tudo certo
    print('Expressão válida!')
