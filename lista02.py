#----EXERCICIO 1----
#Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem serum triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

L1 = float(input('Primeiro lado do triângulo: '))
L2 = float(input('Segundo lado do triângulo: '))
L3 = float(input('Terceiro lado do triângulo: '))
if (L1 + L2 > L3) and (L2 + L3 > L1) and (L1 + L3 > L2):
    print ('Esses lados formam um triângulo.')
    print('Classificação do triângulo: ')

    if (L1 == L2) and (L2 == L3):
        print ('Equilatero, pois todos os lados são iguais.')
    elif (L1 == L2 or L2 == L3) or (L1 == L3):
        print ('Isosceles, pois tem dois lados iguais e um diferente.')
    elif (L1 != L2) and (L2 != L3) and (L1 != L3):
        print ('Escaleno, pois todos os lados são diferentes.')

else:
    print ('Esses lados não formam um triângulo.')
x = input ()

#---EXERCICIO 2----
#Determine se um ano é bissexto. Verifique no Google como fazer isso...

ano = int(input('Insira um ano: '))
if (ano % 4 == 0):
    print ('Ano bissexto')
else:
    print ('Ano comum')
x = input()

#---EXERCICIO 3----
#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.

kg = float(input('Quantos kg de peixes foram pescados?: '))
if kg > 50:
    print('Multado!')
    print(f'Valor da multa: R$ {(kg - 50) * 4},00')
    print(f"Kg's excedidos: {kg - 50}Kg")
else:
    print('Parabéns! Você não excedeu o valor permitido.') 
    print(f'Valor da multa: R$ 0,00')
    print(f"Kg's excedidos: 0 Kg")
x = input ()



#---EXERCICIO 4----
#Faça um Programa que leia três números e mostre o maior deles

x = float(input('Primeiro número: '))
y = float(input('Segundo número: '))
z = float(input('Terceiro número: '))
if (x > y) and (x > z):
    print(f'{x: .0f} é o maior número.')
elif (y > x) and (y > z):
    print(f'{y: .0f} é o maior número.')
else:
    print(f'{z: .0f} é o maior número.')
x = input ()

#---EXERCICIO 5----
#Faça um Programa que leia três números e mostre o maior e o menor deles.


x = float(input('Primeiro número: '))
y = float(input('Segundo número: '))
z = float(input('Terceiro número: '))

#Maior numero

if (x > y) and (x > z):
    print(f'{x: .0f} é o maior número.')
elif (y > x) and (y > z):
    print(f'{y: .0f} é o maior número.')
else:
    print(f'{z: .0f} é o maior número.')


#Menor numero
    
if (x < y) and (x < z):
    print(f'{x: .0f} é o menor número.')
elif (y < x) and (y < z):
    print(f'{y: .0f} é o menor número.')
else:
    print(f'{z: .0f} é o menor número.')
x = input ()


#---EXERCICIO 6----
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto,quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:

#a.  + Salário Bruto : R$
#b.  -IR (11%) : R$
#c.  -INSS (8%) : R$
#d.  -Sindicato ( 5%) : R$
#e.  = Salário Liquido : R$

h = float(input('Quanto voce ganha por hora?: '))
t = float(input('Quantas horas voce trabalha no mês?: '))
salario = (h * t)
IR = (salario * 11/100)
INSS = (salario * 8/100)
Sindicato = (salario * 5/100)
print (f'Salario Bruto: R${salario: .2f}')
print (f'- IR(11%): R${IR: .2f}')
print (f'- INSS(8%): R${INSS: .2f}')
print (f'- Sindicato(5%): R${Sindicato: .2f}')
print (f'Salário Liquido: {(salario - IR - INSS - Sindicato): .2f}')
x = input()

#---EXERCICIO 7----
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.

a = float(input('tamanho em m² da área a ser pintada:'))
L = a / 3
T = L / 18
Q = int (T) + 1
if L <= 18:
    print('1 Lata')
else:
    print(f'{Q} Latas serão necessárias')
print (f'Preço: R${(Q * 80): .2f}')
x = input()