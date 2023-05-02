a = int(input('Escreva um número inteiro'))
b = int(input('Escreva um número inteiro'))
c = int(input('Escreva um número inteiro'))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Equilátero')
    elif a == b or a == c or b == c :
        print('Isósceles')
    else: 
        print('Escaleno')
else:
    print('Não é um triângulo')