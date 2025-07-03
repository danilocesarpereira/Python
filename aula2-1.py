nome = "Carlos"
idade = 30
saldo_conta = 1250.75
# Jeito antigo
print("O usuário", nome, "tem", idade, "anos e saldo de", saldo_conta)
# Com f-string (muito melhor!)
print(f"O usuário {nome} tem {idade} anos e saldo de R${saldo_conta:.2f}")


frase = " bem-vindo ao curso de Python! "
print(f"Original: '{frase}'")
print(f"Maiúsculas: '{frase.upper()}'")
print(f"Minúsculas: '{frase.lower()}'")
print(f"Capitalizada: '{frase.strip().capitalize()}'")
print(f"Troca: '{frase.replace('Python', 'Django')}'")