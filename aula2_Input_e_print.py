#%% 1
área=250
preço=512490.50
print("preço total")
print(área*preço)
#%% 2
fah=30
print (f"{fah} graus fahrenheit são")
print(f"{(fah-32)*(5/9)} graus celsius")
#%% 3
nome1 = input("Digite o nome do produto 1:")
preco_unitario1 = float(input("Digite o preço unitário do produto 1:"))
quantidade1 = int(input("Digite a quantidade do produto 1:"))
nome2 = input("Digite o nome do produto 2: ")
preco_unitario2 = float(input("Digite o preço unitário do produto 2:"))
quantidade2 = int(input("Digite a quantidade do produto 2:"))
nome3 = input("Digite o nome do produto 3:")
preco_unitario3 = float(input("Digite o preço unitário do produto 3:"))
quantidade3 = int(input("Digite a quantidade do produto 3:"))
total=(preco_unitario1*quantidade1)+(preco_unitario2*quantidade2)+(preco_unitario3*quantidade3)
print(f"Total: R${total:,.2f}")
#%% 4
valor = int(input("Digite um valor inteiro em reais:"))

notas_100 = valor // 100
valor %= 100
notas_50 = valor // 50
valor %= 50
notas_20 = valor // 20
valor %= 20
notas_10 = valor // 10
valor %= 10
notas_5 = valor // 5
valor %= 5
notas_2 = valor // 2
valor %= 2
notas_1 = valor // 1
valor %= 1

print(f"{notas_100} nota(s) de R$100,00")
print(f"{notas_50} nota(s) de R$50,00")
print(f"{notas_20} nota(s) de R$20,00")
print(f"{notas_10} nota(s) de R$10,00")
print(f"{notas_5} nota(s) de R$5,00")
print(f"{notas_2} nota(s) de R$2,00")
print(f"{notas_1} nota(s) de R$1,00")
