# Exercício 1
# Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.
import random
a = random.sample(range(100),10)
maior = menor = a[0]
for x in a[1:]:
    if x > maior: maior = x
    if x < menor: menor = x
print (a)
print (f'Maior: {maior}')
print (f'Menor: {menor}')

# Exercício 2
# Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.
import random
a = random.sample(range(100),20)
pares = []
impares = []
a.sort()
for x in a:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
pares.sort()
impares.sort()
print (a)
print (f'Pares: {pares}')
print (f'Impares: {impares}')

# Exercício 3
# Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.
from random import randint
V1 = []
V2 = []
V3 = []
for x in range(10):
    x = randint(1, 100)
    V1.append(x)
    V3.append(x)
    x = randint(1, 100)
    V2.append(x)
    V3.append(x)
print('1º Vetor: ', V1)
print('2º Vetor: ', V2)
print('3º Vetor: ', V3)

# Exercício 4
# Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais e cuidar do caso de maiúsculas e minúsculas.
texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''.lower()
import string
for x in string.punctuation:
    texto = texto.replace(x, ' ')
    
resp = []
for p in texto.split():
    if p[0] in 'python' or p[-1] in 'python':
        resp.append(p)

print(resp)

# Exercício 5
# Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.
texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''.lower()
import string
for x in string.punctuation:
    texto = texto.replace(x, ' ')

def pitonica(palavra):
    for letra in palavra:
        if letra in 'python':
            return True
    return False
    
resp = []
for p in texto.split():
    if pitonica(p) and len(p) > 4:
        resp.append(p)
print (resp)
print(len(resp))
