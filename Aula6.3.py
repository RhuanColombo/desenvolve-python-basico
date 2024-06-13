#%% 1
numeros = []
print("Digite pelo menos 4 números inteiros (digite 'sair' para finalizar):")
while len(numeros) < 4:
    entrada = input(f"Número {len(numeros) + 1}: ")
    if entrada.lower() == 'sair' and len(numeros) >= 4:
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número inteiro.")

print("Lista original:", numeros)
print("Os 3 primeiros elementos:", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])
#%% 2
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominios = [url[4:-4] for url in urls]
print("URLs:", urls)
print("Domínios:", dominios)
#%% 3
import random
lista = [random.randint(-10, 10) for _ in range(20)]
max_negativos = 0
intervalo_inicio = 0
intervalo_fim = 0

for i in range(len(lista)):
    for j in range(i+1, len(lista)+1):
        sub_lista = lista[i:j]
        num_negativos = sum(1 for num in sub_lista if num < 0)
        if num_negativos > max_negativos:
            max_negativos = num_negativos
            intervalo_inicio, intervalo_fim = i, j

print("Original:", lista)
del lista[intervalo_inicio:intervalo_fim]
print("Editada:", lista)