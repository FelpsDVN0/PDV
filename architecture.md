# Arquitetura do Sistema PDV para Raspberry Pi Zero

O sistema será construído em Python 3, utilizando a biblioteca **Tkinter** para a interface gráfica, devido à sua leveza e baixo consumo de recursos, o que é essencial para o hardware limitado do Raspberry Pi Zero. O armazenamento de dados será feito através do **SQLite3**, garantindo persistência e facilidade de manutenção sem a necessidade de um servidor de banco de dados complexo.

## Estrutura de Arquivos

A organização do projeto seguirá uma estrutura modular para facilitar a manutenção e expansão futura:

| Arquivo | Descrição |
| :--- | :--- |
| `main.py` | Ponto de entrada do aplicativo, inicializa a GUI e o loop principal. |
| `database.py` | Gerenciamento do banco de dados SQLite (criação de tabelas, CRUD de produtos). |
| `gui.py` | Definição das telas e componentes da interface gráfica (Tkinter). |
| `logic.py` | Lógica de negócio: processamento de vendas, cálculo de totais e integração com o leitor. |
| `products.db` | Arquivo do banco de dados SQLite (gerado automaticamente). |
| `requirements.txt` | Lista de dependências do Python (principalmente bibliotecas padrão). |

## Fluxo de Operação

1.  **Inicialização:** O sistema carrega o banco de dados e abre a interface de vendas em tela cheia.
2.  **Entrada de Dados:** O leitor de código de barras (emulando um teclado) envia os dígitos do código seguidos de um `Enter`.
3.  **Processamento:** O sistema intercepta o evento de `Enter`, busca o código no banco de dados e adiciona o item à lista de compras atual.
4.  **Cálculo:** O total é atualizado em tempo real a cada item adicionado.
5.  **Finalização:** O operador confirma o pagamento e a venda é registrada (opcionalmente limpando a tela para a próxima compra).

## Requisitos de Interface

A interface será projetada para ser simples e de alto contraste, facilitando a leitura em monitores pequenos que costumam ser usados com o Raspberry Pi Zero.

-   **Área Superior:** Exibição do nome do mercado e relógio.
-   **Área Central:** Lista de itens (Nome, Quantidade, Preço Unitário, Subtotal).
-   **Área Inferior:** Campo de entrada (invisível ou focado) para o barcode e o valor total em destaque.
