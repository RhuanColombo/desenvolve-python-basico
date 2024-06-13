#%% 1
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
    
soma = num1 + num2
    
if soma % 2 == 0:
    print("A soma é par.")
else:
    print("A soma é ímpar.")
#%% 2

avaliacao = int(input("Insira a avaliação do filme (1 a 5): "))
    
if avaliacao == 5:
    print("Excelente!")
elif avaliacao == 4:
    print("Muito Bom!")
elif avaliacao == 3:
    print("Bom!")
elif avaliacao == 2:
    print("Regular.")
elif avaliacao == 1:
    print("Ruim.")
else:
    print("Avaliação inválida. Por favor, insira um valor entre 1 e 5.")
#%% 3
ano = int(input("Insira um ano: "))
    
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não Bissexto")
#%% 4
distancia = float(input("Digite a distância da entrega em km: "))
peso = float(input("Digite o peso do pacote em kg: "))
    
if distancia <= 100:
    custo_frete = 1 * peso
elif distancia <= 300:
    custo_frete = 1.5 * peso
else:
    custo_frete = 2 * peso
    
if peso > 10:
    custo_frete += 10
    
print(f"O valor do frete é: R${custo_frete:.2f}")