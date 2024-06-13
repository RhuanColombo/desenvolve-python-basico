#%% 1
import random
lista = [random.randint(-100, 100) for _ in range(20)]
lista_ordenada = sorted(lista)
indice_maior = lista.index(max(lista))
indice_menor = lista.index(min(lista))

print("Lista ordenada:", lista_ordenada)
print("Lista original:", lista)
print("Índice do maior valor da lista:", indice_maior)
print("Índice do menor valor da lista:", indice_menor)
#%% 2
import random
num_elementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for _ in range(num_elementos)]
soma_valores = sum(elementos)
media_valores = soma_valores / len(elementos)

print("Lista elementos:", elementos)
print("Soma dos valores da lista:", soma_valores)
print("Média dos valores da lista:", media_valores)
#%% 3
import random
from collections import Counter
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]
interseccao = list(set(lista1) & set(lista2))
interseccao_ordenada = sorted(interseccao)
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseccao ordenada:", interseccao_ordenada)
print("Contagem:")
for elemento in interseccao_ordenada:
    print(f"{elemento}: (lista1={contagem_lista1[elemento]}, lista2={contagem_lista2[elemento]})")
#%% 4
lista1 = []
lista2 = []
quantidade_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {quantidade_lista1} elementos da lista 1:")
for _ in range(quantidade_lista1):
    lista1.append(int(input()))
quantidade_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {quantidade_lista2} elementos da lista 2:")
for _ in range(quantidade_lista2):
    lista2.append(int(input()))
lista_intercalada = []
len1, len2 = len(lista1), len(lista2)
min_len = min(len1, len2)
for i in range(min_len):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])
if len1 > len2:
    lista_intercalada.extend(lista1[min_len:])
else:
    lista_intercalada.extend(lista2[min_len:])
print("Lista intercalada:", lista_intercalada)