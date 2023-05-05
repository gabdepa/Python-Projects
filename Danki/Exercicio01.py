"""
Exercícios - Python 

Observação: Todos os exercícios devem utilizar a função input,
de forma que o usuário possa determinar os dados de entrada.

plataformas para treinar sua lógica: site - uri

01 - área de um retângulo
02 - área de um quadrado
03 - Se o produto que você quer avaliar custa (??) reais qual 
será o valor do mesmo com desconto de (??)%.
04 - área de um círculo - pi = 3,141592
05 - conversão de reais para dolar
06 -  conversão de dolar para reais
"""

# Exercício 01 - área do retângulo

print("Calcule a area de um retangulo")

base = input("Qual o tamanho da base do seu retangulo? ")
altura = input("Qual o tamanho da altura do seu retangulo? ")
area = float(base) * float(altura)

print(f'O seu retangulo possui area: {area} unidades de medida\n')

# Exercício 02 - área do quadrado

print("Calcule a area de um quadrado")

lado = input("Qual o tamanho do lado do seu quadrado? ")
area = float(lado) * float(lado)

print(f'O seu quadrado possui area: {area} unidades de medida\n')

# Exercício 03 - Se o produto que vc quer avaliar custa (..) reais qual será o valor do mesmo com desconto de (..)%
print("Calcule o valor de desconto de um produto")

value = input("Qual o valor do seu produto? ")
percentage = input("Qual a procentagem de desconto? ")
final_value = float(value) - (float(value)*(1/100*float(percentage)))

print(f'O seu produto terá um valor final de: {final_value} unidades de moeda para {percentage}% de desconto\n')

# Exercício 04 - área do círculo

print("Calcule a area de um cícrulo")

raio = input("Qual o tamanho do raio do seu círculo? ")
pi = 3.141592
area = pi * float(raio) ** 2

print(f'O seu cícrculo possui area: {area} unidades de medida\n')

# Exercício 04 - conversão R$ para $

print("Calcule a conversão de Reais para Dólar")

reais = input("Qual o seu valor em Reais? ")
dólar = input("Qual a cotação do Dólar atualmente? ")
valor = float(reais) / float(dólar)

print(f'O seu valor total de R${reais} se torna ${valor} em dólares\n')

# Exercício 05 - conversão $ para R$

print("Calcule a conversão de Dólar para Reais")

reais = input("Qual o seu valor em Dólares? ")
dólar = input("Qual a cotação do Dólar atualmente? ")
valor = float(reais) * float(dólar)

print(f'O seu valor total de ${reais} se torna R${valor} em Reais')
