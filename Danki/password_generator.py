# Maiúsculas e Minúsculas
# Símbolos e Espaços

"""
Security = chave
5ecur1ty = senha
"""

key = input("Digite a palavra base da sua senha: ")
senha = ""
alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
decimal = "0123456789"
symbols = "!@#$%&"

for letra in key:
    for  letra in alphabet: senha += "1"
    elif letra in "Bb": senha += "@"
    elif letra in "Cc": senha += "2"
    elif letra in "Dd": senha += "3"
    elif letra in "Ee": senha += "4"
    elif letra in "Ff": senha += "5"
    elif letra in "Rr": senha += "#"
    elif letra in "Ss": senha += "%"
    elif letra in "Ff": senha += "$"
    elif letra in "Mm": senha += "$"
    elif letra in "Gg": senha += "&"
    else: senha += letra
print(senha)
