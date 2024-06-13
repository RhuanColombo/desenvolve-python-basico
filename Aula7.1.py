#%% 1
def escada_nome():
    nome = input("Digite seu nome: ")
    for i in range(1, len(nome) + 1):
        print(nome[:i])
#%% 2
def boas_vindas():
    primeiro_nome = input("Digite seu primeiro nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    nome_completo = primeiro_nome + " " + sobrenome
    print(f"Bem-vinda, {nome_completo}!")
#%% 3
def contar_espacos():
    frase = input("Digite a frase: ")
    espacos = frase.count(' ')
    print(f"Espaços em branco: {espacos}")
#%% 4
def formatar_numero():
    numero = input("Digite o número: ")
    if len(numero) == 8:
        numero = '9' + numero
    if len(numero) == 9 and numero[0] == '9':
        numero_formatado = f"{numero[:5]}-{numero[5:]}"
        print(f"Número completo: {numero_formatado}")
    else:
        print("Número inválido")