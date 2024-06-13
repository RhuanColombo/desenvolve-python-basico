#%% 1
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
diferenca_absoluta = round(abs(num1 - num2), 2)
print(f"A diferença absoluta entre os números é: {diferenca_absoluta}")
#%% 2
import random
import math
n = int(input("Digite o valor de n: "))
valores = [random.randint(0, 100) for _ in range(n)]
soma = sum(valores)
raiz_quadrada = math.sqrt(soma)
print(f"A raiz quadrada da soma dos {n} valores aleatórios é: {raiz_quadrada:.2f}")
#%% 3
import random
numero_secreto = random.randint(1, 10)
while True:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite > numero_secreto:
        print("Muito alto, tente novamente!")
    elif palpite < numero_secreto:
        print("Muito baixo, tente novamente!")
    else:
        print(f"Correto! O número é {numero_secreto}.")
        break
#%% 4
from datetime import datetime
agora = datetime.now()
data_formatada = agora.strftime("Data: %d/%m/%Y")
hora_formatada = agora.strftime("Hora: %H:%M")
print(data_formatada)
print(hora_formatada)