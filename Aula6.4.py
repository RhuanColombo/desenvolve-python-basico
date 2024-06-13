#%% 1
pares = [x for x in range(20, 51) if x % 2 == 0]
print(pares)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [x**2 for x in numeros]
print(quadrados)

divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]
print(divisiveis_por_7)

paridade = ['par' if x % 2 == 0 else 'ímpar' for x in range(0, 30, 3)]
print(paridade)
#%% 2
frase = input("Digite uma frase: ")
vogais = sorted([char for char in frase if char.lower() in 'aeiou'])
consoantes = [char for char in frase if char.isalpha() and char.lower() not in 'aeiou']
print("Vogais:", vogais)
print("Consoantes:", consoantes)

#%% 3
horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25
pagamentos = [ganho_por_hora * min(hora, 40) + hora_extra * max(0, hora - 40) for hora in horas_trabalhadas]
print(pagamentos)
#%% 4
alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]
print(aprovados)