> Introdução

Este sistema foi desenvolvido para uma empresa fictícia que gerencia usuários e produtos.
Existem diferentes tipos de usuários com diferentes níveis de permissão: dono, estagiário e cliente.
A empresa vende produtos como pão, água, bolo e biscoito, cujas informações, como preço e quantidade, são gerenciadas pelo sistema.

> Implementação

Usuários
    Estrutura de Dados: Lista de dicionários.
    Arquivo de Registro: usuarios.csv com colunas id, nome, senha, permissao.
    Funcionalidades:
        Create: Adicionar novos usuários (dono).
        Read: Listar todos os usuários (dono).
        Update: Atualizar informações dos usuários existentes (dono).
        Delete: Remover usuários do sistema (dono).

Produtos/Serviços
    Estrutura de Dados: Lista de dicionários.
    Arquivo de Registro: produtos.csv com colunas id, nome, preco, quantidade.
    Funcionalidades:
        Create: Adicionar novos produtos (dono).
        Read: Listar todos os produtos (todos).
        Update: Atualizar informações dos produtos existentes (dono, estagiário).
        Delete: Remover produtos do sistema (dono).

> Conclusão

Durante a implementação, garantir que os diferentes níveis de permissão fossem respeitados foi um desafio,
mas creio que consegui organizar o código de forma que as funções apropriadas sejam acessíveis apenas para os usuários
com permissões adequadas. A estrutura de dados escolhida (lista de dicionários) facilitou a manipulação dos registros,
e o uso de arquivos CSV garantiu a persistência dos dados. Para futuras melhorias, poderíamos implementar a busca por
produtos e a ordenação por preço ou nome diretamente na listagem de produtos. Não está perfeito, custou para fazer, mas
foi um bom desafio...