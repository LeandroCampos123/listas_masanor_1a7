#----EXERCICIO 1---- soma
#Faça um programa que peça dois números inteiros e imprima a soma desses dois números

a = int(input('Digite um numero'))
b = int(input('Digite mais um numero'))
print (a+b)
x = input()

#---EXERCICIO 2----
#Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

print ('Conversor de m para mm')
a = float(input('Insira uma quantidade em metros(m): '))
print (f'{a * 1000}mm') 
x = input ()


#---EXERCICIO 3----
#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

a = int(input('Digite uma quantidade de dias: '))
b = int(input('Digite uma quantidade de horas: '))
c = int(input('Digite uma quantidade de minutos: '))
d = int(input('Digite uma quantidade de segundos: '))
x = (c * 60)
y = (b * (60 * 60))
z = (a * ((60 * 60) * 24))
print (f'Todos esses valores em segundos resulta em: {x + y + z + d}s')
p = input ()


#---EXERCICIO 4----
#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário

salário = float(input('Digite o valor do salário: R$'))
aumento = float(input('Digite a porcentagem do aumento: '))
novo = (salário + (salário * (aumento / 100)))
print (f'Novo salário: {novo}')
x = input ()
                
#---EXERCICIO 5----
#Solicite o preço de uma mercador ia e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

a = float(input('Digite o valor do produto: '))
b = float(input('Adicione o percentual de desconto: '))
print (f'Desconto de {b}%')
print (f'Valor do produto com desconto: {a - (a * (b / 100))}')
x = input()

#---EXERCICIO 6----
#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem

print ('Calculador de tempo de viagem')
a = float(input('Insira a distancia a ser percorrida em Km: '))
b = float(input('Agora insira a velocidade media estimada em Km/h: '))
print (f'Você irá demorar {a / b} horas para chegar ao seu destino')
x = input()

#---EXERCICIO 7----
#Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C /5 + 32

print ('Conversor de °C para °F')
a = float(input('Insira a temperatura em °C: '))
print (f'Agora em Fahrenheit: {9 * (a / 5) + 32} °F')       
x = input()

#---EXERCICIO 8----
#Faça agora o contrário, de Fahrenheit para Celsius.


print ('Conversor de °F para °C')
a = float(input('Insira a temperatura em °F: '))
print (f'Agora em Celsius: {(a - 32) * (5 / 9)} °C')       
x = input()

#---EXERCICIO 9----
#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

print ('Locadora de veículos :)')
a = float(input("Quantos km's foram percorridos?: "))
b = float(input("Por quantos dias o automovel foi alugado?: "))
print (f'Preço a pagar: R${(a * 0.15) + (b * 60)}')
x = input ()
          
#---EXERCICIO 10----
#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

a = int(input('Quantos cigarros voce fuma por dia?: '))
b = float(input('A quantos anos voce fuma?: '))
c = (a * 365)
d = (b * c)
e = (d * 10)
f = (e / 60) / 24
g = input(f'Voce ja perdeu {f: .0f} dias de vida :D')
x = input ()

#---EXERCICIO 11----
#Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um 10 mil.

a = len (str(2 ** 10000))
print (f'Dois elevado a dez mil tem {a} caracteres.')
x = input ()