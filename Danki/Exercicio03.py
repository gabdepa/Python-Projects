# Exercício 01
print(15 * "-", "Ex 01", 15 * "-")

numero = int(input(f"Entre com o número na posição {0}: "))
maior = menor = numero

for i in range(1,5):
    numero = int(input(f"Entre com o número na posição {i}: "))
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    else:
        continue
print(f"O maior número da sequência é: {maior} e o menor número é: {menor}")

print(15 * "-", "Ex 01", 15 * "-", "\n") 

# Exercicio 02
print(15 * "-", "Ex 02", 15 * "-")

print("Calculando a soma: 480/21 + 475/22 + 470/23 + 465/24 + 460/25 + ... para os 20 primeiros termos")
numerador = 480
denominador = 21
total = 0

for i in range(20):
  print(f"Realizando operação {numerador}/{denominador}..")
  total += numerador / denominador
  numerador -= 5
  denominador += 1
print(f"Resultado da soma: {total}")

print(15 * "-", "Ex 02", 15 * "-")
