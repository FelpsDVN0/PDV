## Estrutura de Arquivos

| Arquivo | Descrição |
| :--- | :--- |
| `main.py` | Ponto de entrada do aplicativo. Inicializa o banco de dados e a interface gráfica. |
| `gui.py` | Contém a classe `POSApp`, responsável por toda a interface do usuário (Tkinter) e lógica de interação. |
| `database.py` | Gerencia a conexão com o SQLite, criação de tabelas e funções CRUD para os produtos. |
| `products.db` | Arquivo do banco de dados (criado automaticamente na primeira execução). |
| `install.sh` | Script bash para automatizar a instalação das dependências no Raspberry Pi. |
| `requirements.txt` | Lista de dependências Python. |

## Como Funciona

1.  **Inicialização:** Ao executar `main.py`, o sistema verifica se o banco de dados `products.db` existe. Se não, ele o cria e insere alguns produtos de exemplo.
2.  **Interface:** A tela principal exibe uma lista vazia (carrinho de compras), um campo para o código de barras e o valor total.
3.  **Leitura:** Quando o operador "bipa" um produto com o leitor de código de barras, o leitor digita o código no campo de entrada e simula a tecla `Enter`.
4.  **Processamento:** O sistema captura o evento `Enter`, busca o código no banco de dados. Se encontrado, adiciona o item à lista e atualiza o total. Se não, exibe um aviso.
5.  **Ações:**
    *   **F1:** Inicia uma nova venda (limpa o carrinho e o total).
    *   **Delete:** Remove o item selecionado da lista e subtrai seu valor do total.

## Instalação no Raspberry Pi Zero

Para instalar e configurar o sistema no seu Raspberry Pi Zero, siga os passos abaixo:

1.  Transfira os arquivos do projeto para o seu Raspberry Pi (por exemplo, via SSH/SCP ou pendrive).
2.  Abra o terminal e navegue até a pasta onde os arquivos foram salvos.
3.  Dê permissão de execução ao script de instalação:
    ```bash
    chmod +x install.sh
    ```
4.  Execute o script de instalação:
    ```bash
    ./install.sh
    ```
    Este script irá atualizar o sistema, instalar o Python3, o Tkinter e configurar o ambiente.

## Execução

Após a instalação, você pode iniciar o sistema executando:

```bash
python3 main.py
```

**Dica:** Para uma experiência de "caixa de supermercado" real, você pode configurar o Raspberry Pi para iniciar o script `main.py` automaticamente em tela cheia (descomentando as linhas relevantes no `main.py`) logo após o boot do sistema operacional.

## Adicionando Novos Produtos

Atualmente, o banco de dados é inicializado com alguns produtos de exemplo. Para adicionar novos produtos, você pode criar um script Python simples que utilize a função `add_product` do arquivo `database.py`:

```python
from database import add_product

# Exemplo: Adicionando um novo produto
add_product('1234567890123', 'Novo Produto Teste', 15.99)
print("Produto adicionado!")
```

Ou, você pode abrir o arquivo `products.db` usando um gerenciador de banco de dados SQLite (como o DB Browser for SQLite) para gerenciar o inventário visualmente.
