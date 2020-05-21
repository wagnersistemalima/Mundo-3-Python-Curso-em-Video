# faça um progama que tenha uma função chamada area(), que receba as dimensoes de um terreno retangular (largura e comprimento) e mostre a area do terreno.
def calculo(largura, comprimento):
    c = largura * comprimento
    print(f'A area de um terreno {largura} x {comprimento} é de {c} metros')



#progama principal
print('-='*20)
print('    Controle de Terrenos    ')
print('-='*20)
larg = float(input('Largura (m) '))
compr = float(input('Comprimento (m) '))
calculo(larg, compr)                          # chamar a função