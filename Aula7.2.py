#%% 1
def data_nascimento_extenso(data):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    dia, mes, ano = data.split('/')
    mes_extenso = meses[int(mes) - 1]
    return f"Você nasceu em {dia} de {mes_extenso} de {ano}."
data = input("Digite uma data de nascimento (dd/mm/aaaa): ")
print(data_nascimento_extenso(data))
#%% 2
def substituir_vogais(frase):
    vogais = "aeiouAEIOU"
    frase_modificada = ''.join(['*' if char in vogais else char for char in frase])
    return frase_modificada
frase = input("Digite uma frase: ")
print("Frase modificada:", substituir_vogais(frase))
#%% 3
def eh_palindromo(frase):
    frase = ''.join([char.lower() for char in frase if char.isalnum()])
    return frase == frase[::-1]
while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == "fim":
        break
    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
#%% 4
import re
def validador_senha(senha):
    if len(senha) < 8:
        return False
    if not re.search(r"[A-Z]", senha):
        return False
    if not re.search(r"[a-z]", senha):
        return False
    if not re.search(r"[0-9]", senha):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return False
    return True
#Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))  #Saída esperada: True
print(validador_senha(senha2))  #Saída esperada: False
print(validador_senha(senha3))  #Saída esperada: False
#%% 5
import random
def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra) <= 3:
            return palavra
        meio = list(palavra[1:-1])
        random.shuffle(meio)
        return palavra[0] + ''.join(meio) + palavra[-1]

    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras]
    return ' '.join(palavras_embaralhadas)
#Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
#Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"