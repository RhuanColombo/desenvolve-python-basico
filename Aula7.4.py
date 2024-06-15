#Nota: Estou sobrecarregado no tempo para a entrega dos exercícios (deixei python para o final, estou fora da ordem cronologica de cursos), tenho o trabalho de Projetos para fazer e coisas de faculdade para resolver. Cortei alguns caminhos para fazer os códigos mais eficientemente; especialmente nos exercícios 4, 5 e 6. Por "cortar caminho", quero dizer que haverá apenas código em Python, apesar dos exercícios me direcionarem para diversos cantos da internet
#%% 1
import os
def salvar_frase():
    frase = input("Digite uma frase: ")
    caminho_arquivo = os.path.join(os.getcwd(), "frase.txt")
    with open(caminho_arquivo, "w") as file:
        file.write(frase)
    print(f"Frase salva em {caminho_arquivo}")
salvar_frase()
#%% 2
import re
def processar_frase():
    caminho_frase = os.path.join(os.getcwd(), "frase.txt")
    caminho_palavras = os.path.join(os.getcwd(), "palavras.txt")
    with open(caminho_frase, "r") as file:
        frase = file.read()
    palavras = re.findall(r'\b\w+\b', frase)
    with open(caminho_palavras, "w") as file:
        for palavra in palavras:
            file.write(palavra + '\n')
    with open(caminho_palavras, "r") as file:
        print(file.read())
processar_frase()
#%% 3
def analisar_estomago():
    caminho_arquivo = os.path.join(os.getcwd(), "estomago.txt")
    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        linhas = file.readlines()
    #Imprimir as primeiras 25 linhas
    print("Primeiras 25 linhas do texto:")
    for linha in linhas[:25]:
        print(linha.strip())
    #Número de linhas do arquivo
    numero_de_linhas = len(linhas)
    print(f"\nNúmero de linhas do arquivo: {numero_de_linhas}")
    #Linha com maior número de caracteres
    linha_mais_longa = max(linhas, key=len)
    print(f"\nLinha com maior número de caracteres:\n{linha_mais_longa.strip()}")
    #Número de menções aos personagens "Nonato" e "Íria"
    mencoes_nonato = sum(linha.lower().count("nonato") for linha in linhas)
    mencoes_iria = sum(re.findall(r'\bÍria\b|\bíria\b', linha, re.IGNORECASE) for linha in linhas)
    print(f"\nNúmero de menções ao personagem 'Nonato': {mencoes_nonato}")
    print(f"Número de menções ao personagem 'Íria': {mencoes_iria}")

analisar_estomago()
#%% 4

#gabarito_forca.txt
#python
#java
#ruby
#javascript
#html
#css
#django
#flask
#react
#angular

#gabarito_enforcado.txt
#  |---|
#      |
#      |
#      |
#=========
 
#  |---|
#  O   |
#      |
#      |
#=========
 
#  |---|
#  O   |
#  |   |
#      |
#=========
 
#  |---|
#  O   |
# /|   |
#      |
#=========
 
#  |---|
#  O   |
# /|\  |
#      |
#=========
 
#  |---|
#  O   |
# /|\  |
# /    |
#=========
 
#  |---|
#  O   |
# /|\  |
# / \  |
#=========

import random
import os

def carregar_palavra():
    with open("gabarito_forca.txt", "r") as file:
        palavras = file.read().splitlines()
    return random.choice(palavras)

def carregar_enforcado():
    with open("gabarito_enforcado.txt", "r") as file:
        estagios = file.read().split("\n\n")
    return estagios

def imprime_enforcado(estagios, erros):
    print(estagios[erros])

def jogo_da_forca():
    palavra = carregar_palavra()
    estagios = carregar_enforcado()
    letras_adivinhadas = ["_" for _ in palavra]
    tentativas = 6
    erros = 0
    letras_erradas = []

    print("Bem-vindo ao jogo da forca!")
    print(" ".join(letras_adivinhadas))

    while erros < tentativas and "_" in letras_adivinhadas:
        letra = input("Digite uma letra: ").lower()
        
        if letra in palavra:
            for i, char in enumerate(palavra):
                if char == letra:
                    letras_adivinhadas[i] = letra
            print(" ".join(letras_adivinhadas))
        else:
            if letra not in letras_erradas:
                letras_erradas.append(letra)
                erros += 1
            imprime_enforcado(estagios, erros)
            print("Letras erradas: ", " ".join(letras_erradas))
            print(" ".join(letras_adivinhadas))
    
    if "_" not in letras_adivinhadas:
        print("Parabéns! Você adivinhou a palavra:", palavra)
    else:
        print("Você perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    jogo_da_forca()
#%% 5
import csv
def criar_arquivo_csv():
    livros = [
        {"Título": "O Senhor dos Anéis", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1954, "Número de páginas": 1216},
        {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
        {"Título": "O Apanhador no Campo de Centeio", "Autor": "J.D. Salinger", "Ano de publicação": 1951, "Número de páginas": 277},
        {"Título": "O Grande Gatsby", "Autor": "F. Scott Fitzgerald", "Ano de publicação": 1925, "Número de páginas": 180},
        {"Título": "Moby Dick", "Autor": "Herman Melville", "Ano de publicação": 1851, "Número de páginas": 635},
        {"Título": "Guerra e Paz", "Autor": "Liev Tolstói", "Ano de publicação": 1869, "Número de páginas": 1225},
        {"Título": "Crime e Castigo", "Autor": "Fiódor Dostoiévski", "Ano de publicação": 1866, "Número de páginas": 671},
        {"Título": "Dom Quixote", "Autor": "Miguel de Cervantes", "Ano de publicação": 1605, "Número de páginas": 1072},
        {"Título": "Cem Anos de Solidão", "Autor": "Gabriel Garcia Marquez", "Ano de publicação": 1967, "Número de páginas": 417},
        {"Título": "Orgulho e Preconceito", "Autor": "Jane Austen", "Ano de publicação": 1813, "Número de páginas": 432}
    ]
    with open('meus_livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Título", "Autor", "Ano de publicação", "Número de páginas"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for livro in livros:
            writer.writerow(livro)
criar_arquivo_csv()
#%% 6
import csv
def is_valid_line(row):
    try:
        int(row[2])  # artist_count deve ser inteiro
        int(row[3])  # released_year deve ser inteiro
        int(row[8])  # streams deve ser inteiro
        return True
    except ValueError:
        return False
def process_csv(file_path):
    top_songs = {}
    # Abre o CSV para leitura com 'latin-1'
    with open(file_path, mode='r', encoding='latin-1') as file:
        reader = csv.reader(file)
        next(reader)  # Pula linha de cabeçalho
        for row in reader:
            # Verifica se a linha tem 10 colunas e se é válida
            if len(row) != 10 or not is_valid_line(row):
                continue  # Ignora linhas inválidas
            # Extrai informações necessárias das colunas
            track_name = row[0]
            artists = row[1]
            artist_count = int(row[2])
            released_year = int(row[3])
            streams = int(row[8])
            # Verifica se o ano de lançamento está no intervalo de 2012-2022
            if 2012 <= released_year <= 2022:
                # Atualiza a música mais popular do ano se tiver mais streams
                if released_year not in top_songs or streams > top_songs[released_year][3]:
                    top_songs[released_year] = [track_name, artists, released_year, streams]
    # Gera a lista final de músicas mais populares por ano
    top_songs_list = [top_songs[year] for year in range(2012, 2023) if year in top_songs]
    return top_songs_list
if __name__ == "__main__":
    file_path = 'spotify-2023.csv'
    top_songs_list = process_csv(file_path)
    for song in top_songs_list:
        print(song)