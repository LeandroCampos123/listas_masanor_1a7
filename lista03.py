#Exercício 1
#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

n = int(input('Insira uma nota de 0 a 10: '))
while n < 0 or n > 10:
    print('Nota inválida!')
    n = int(input('Insira uma nota de 0 a 10: '))

print(f'Nota válida: {n}')


#Exercício 2
#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

u = str(input('Usuário: '))
s = str(input('Senha: '))
while u.lower() == s.lower():
    print('Usuario e senha nao podem ser iguais!')
    u = str(input('Usuário: '))
    s = str(input('Senha: '))
print ('Logado!')
    

#Exercício 3
#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a po pulação de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento

A = 80000
B = 200000
anos = 0
while A <= B:
    A = A + A * (3/100)
    B = B + B * (1.5/100)
    anos = anos + 1
print (f'Em {anos} anos A ultapassará B. ')

#Exercício 4
#A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F3= 2, etc.

f = int(input('Digite um número: '))
a,b = 1,1
x = 1
while x <= f - 2:
    a,b = b, a + b
    x += 1
    print (f' Numero em Fibonacci: {b}')

#Exercício 5
#Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides

a = int(input('A: '))
b = int(input('B: '))
a,b = b, a % b
while a % b != 0:
    a,b = b, a % b
    print (f"MDC: {b}")