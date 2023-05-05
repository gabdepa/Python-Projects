# Exercício 01 - Idades

print("Exercício 01 ::")
idade = int(input("Qual a sua idade? "))

if idade < 16:
    print(f"Como você possui {idade} anos você é considerado DE MENOR\n")
elif idade >= 16 and idade <= 18:
    print(f"Como você possui {idade} anos você é considerado EMANCIPADO\n")
elif idade > 18:
    print(f"Como você possui {idade} anos você é considerado DE MAIOR\n")

# Exercício 02 - Idade Nadador

print("Exercício 02 ::")
age = int(input("Qual a sua idade? "))

if age >= 5 and age <= 7:
    print(f"Idade: {age} - Categoria: Infantil A")
elif age >= 8 and age <= 10:
    print(f"Idade: {age} - Categoria: Infantil B")
elif age >= 11 and age <= 13:
    print(f"Idade: {age} - Categoria: Juvenil A")
elif age >= 14 and age <= 17:
    print(f"Idade: {age} - Categoria: Juvenil B")
else:
    print(f"Idade: {age} - Categoria: INDEFINIDA")