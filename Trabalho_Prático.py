import csv

# Estruturas de dados para carregar informações
usuarios = []
produtos = []

# Função para carregar dados de usuários
def carregar_usuarios():
    with open('usuarios.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            usuarios.append(row)

# Função para carregar dados de produtos
def carregar_produtos():
    with open('produtos.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            produtos.append(row)

# Função de login
def login():
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    
    for usuario in usuarios:
        if usuario['nome'] == nome and usuario['senha'] == senha:
            print(f"Bem-vindo {nome}!")
            return usuario['permissao']
    
    print("Nome de usuário ou senha incorretos.")
    return None

# Funções CRUD para usuários
def adicionar_usuario():
    id = input("ID: ")
    nome = input("Nome: ")
    senha = input("Senha: ")
    permissao = input("Permissão: ")
    
    novo_usuario = {"id": id, "nome": nome, "senha": senha, "permissao": permissao}
    usuarios.append(novo_usuario)
    salvar_usuarios()

def listar_usuarios():
    for usuario in usuarios:
        print(usuario)

def atualizar_usuario():
    id = input("ID do usuário a ser atualizado: ")
    for usuario in usuarios:
        if usuario['id'] == id:
            usuario['nome'] = input("Novo nome: ")
            usuario['senha'] = input("Nova senha: ")
            usuario['permissao'] = input("Nova permissão: ")
            salvar_usuarios()
            return
    print("Usuário não encontrado.")

def remover_usuario():
    id = input("ID do usuário a ser removido: ")
    for usuario in usuarios:
        if usuario['id'] == id:
            usuarios.remove(usuario)
            salvar_usuarios()
            return
    print("Usuário não encontrado.")

# Funções CRUD para produtos
def adicionar_produto():
    id = input("ID: ")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    
    novo_produto = {"id": id, "nome": nome, "preco": preco, "quantidade": quantidade}
    produtos.append(novo_produto)
    salvar_produtos()

def listar_produtos():
    for produto in produtos:
        print(produto)

def atualizar_produto():
    id = input("ID do produto a ser atualizado: ")
    for produto in produtos:
        if produto['id'] == id:
            produto['nome'] = input("Novo nome: ")
            produto['preco'] = float(input("Novo preço: "))
            produto['quantidade'] = int(input("Nova quantidade: "))
            salvar_produtos()
            return
    print("Produto não encontrado.")

def remover_produto():
    id = input("ID do produto a ser removido: ")
    for produto in produtos:
        if produto['id'] == id:
            produtos.remove(produto)
            salvar_produtos()
            return
    print("Produto não encontrado.")

# Função para salvar usuários em arquivo
def salvar_usuarios():
    with open('usuarios.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'nome', 'senha', 'permissao']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for usuario in usuarios:
            writer.writerow(usuario)

# Função para salvar produtos em arquivo
def salvar_produtos():
    with open('produtos.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'nome', 'preco', 'quantidade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)

# Função principal
def main():
    carregar_usuarios()
    carregar_produtos()
    
    permissao = login()
    if permissao:
        while True:
            print("\nMenu:")
            if permissao == 'dono':
                print("1. Adicionar usuário")
                print("2. Listar usuários")
                print("3. Atualizar usuário")
                print("4. Remover usuário")
            if permissao in ['dono', 'estagiario', 'cliente']:
                print("5. Listar produtos")
            if permissao in ['dono', 'estagiario']:
                print("6. Atualizar produto")
            if permissao == 'dono':
                print("7. Adicionar produto")
                print("8. Remover produto")
            print("9. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1' and permissao == 'dono':
                adicionar_usuario()
            elif opcao == '2' and permissao == 'dono':
                listar_usuarios()
            elif opcao == '3' and permissao == 'dono':
                atualizar_usuario()
            elif opcao == '4' and permissao == 'dono':
                remover_usuario()
            elif opcao == '5' and permissao in ['dono', 'estagiario', 'cliente']:
                listar_produtos()
            elif opcao == '6' and permissao in ['dono', 'estagiario']:
                atualizar_produto()
            elif opcao == '7' and permissao == 'dono':
                adicionar_produto()
            elif opcao == '8' and permissao == 'dono':
                remover_produto()
            elif opcao == '9':
                break
            else:
                print("Opção inválida ou permissão insuficiente.")
    
if __name__ == "__main__":
    main()
