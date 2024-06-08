#%% 1
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))
podem_entrar = idade_juliana > 17 and idade_cris > 17
print(podem_entrar)
#%% 2
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))
podem_entrar = idade_juliana > 17 or idade_cris > 17
print(podem_entrar)
#%% 3
idade = int(input("Digite sua idade: "))
jogou_3_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ")
jogou_3_jogos = jogou_3_jogos.strip().capitalize() == 'True'
jogos_vencidos = int(input("Quantos jogos já venceu? "))
apto_para_ingressar = 16 <= idade <= 18 and jogou_3_jogos and jogos_vencidos > 0
print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto_para_ingressar}")
#%% 4
classe_personagem = input("Escolha a classe (guerreiro, mago ou arqueiro): ").lower()
pontos_forca = int(input("Digite os pontos de força (de 1 a 20): "))
pontos_magia = int(input("Digite os pontos de magia (de 1 a 20): "))
if classe_personagem == 'guerreiro':
    consistentes = pontos_forca >= 15 and pontos_magia <= 10
elif classe_personagem == 'mago':
    consistentes = pontos_forca <= 10 and pontos_magia >= 15
elif classe_personagem == 'arqueiro':
    consistentes = 5 < pontos_forca < 15 and 5 < pontos_magia < 15
else:
    consistentes = False
print(f"Pontos de atributo consistentes com a classe escolhida: {consistentes}")
#%% 5
genero = input("Digite seu gênero (M ou F): ").upper()
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))
pode_se_aposentar = (genero == 'F' and (idade > 60 or tempo_servico >= 30 or (idade == 60 and tempo_servico >= 25))) or \
                    (genero == 'M' and (idade > 65 or tempo_servico >= 30 or (idade == 65 and tempo_servico >= 25)))
print(pode_se_aposentar)