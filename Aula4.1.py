#%% 1
x = float(input("Leia x: "))
if x > 5:
    print("Maior que 5")
print("Fim")
#%% 2
n = int(input("Leia n: "))
cont = 0
while n > cont:
    cont += 1
    print(cont)
print("Fim")
#%% 3
n1 = float(input("Leia n1: "))
n2 = float(input("Leia n2: "))
n3 = float(input("Leia n3: "))
m = (n1 + n2 + n3) / 3

if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")
print("Fim")
#%% 4
n = int(input("Leia n: "))
maior = 0
while n > 0:
    x = float(input("Leia x: "))
    if x > maior:
        maior = x
    n -= 1
print("O maior valor é:", maior)
#%% 5
N = int(input("Digite a quantidade de respondentes: "))
idades = []
for i in range(N):
    idade = int(input(f"Digite a idade do respondente {i+1}: "))
    idades.append(idade)
if N > 0:
    media = sum(idades) / N
else:
    media = 0
print(f"A média das idades dos respondentes é: {media:.2f}")
#%% 6
N = int(input())

total_cobaias = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0

for _ in range(N):
    quantidade, tipo = input().split()
    quantidade = int(quantidade)
    total_cobaias += quantidade
    
    if tipo == 'C':
        total_coelhos += quantidade
    elif tipo == 'R':
        total_ratos += quantidade
    elif tipo == 'S':
        total_sapos += quantidade

percentual_coelhos = (total_coelhos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_ratos = (total_ratos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_sapos = (total_sapos / total_cobaias) * 100 if total_cobaias > 0 else 0

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
