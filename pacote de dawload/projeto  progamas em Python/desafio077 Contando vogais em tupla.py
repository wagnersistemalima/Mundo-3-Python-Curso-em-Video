# desafio077 Contando vogais em tupla
# Crie um progama que tenha uma tupla com varias palavras. (não usar acentos). Depois disso, voc~e deve
# mostrar, para cada palavra, quais são as suas vogais.
palavras = ('aprender', 'progamar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'progamador', 'futuro')
for palavra in palavras:       # Para cada palavra dentro da tupla palavra
    print(f'\nNa palavra {palavra.upper()} temos ', end='') # imprimir quebrando linha
    for letra in palavra:   # Para cada letra dentro da palavra
        if letra.lower() in 'aeiou':  #lower transformar para minusculo
            print(letra, end=' ')