# Northwind Orders App

## Descrição
Este projeto tem como objetivo implementar uma aplicação para inserção de pedidos no banco de dados **Northwind** utilizando Python, com foco em segurança (SQL Injection) e mapeamento objeto-relacional (ORM). A aplicação segue o padrão de arquitetura **MVC** e **DAO**, com duas formas de conexão ao banco de dados: **psycopg2** e **SQLAlchemy**.

### Funcionalidades
- Inserção de pedidos no banco de dados.
- Implementação de segurança com **SQL Injection**.
- Relatórios:
  - Detalhes de pedidos: número, data, nome do cliente, nome do vendedor, itens do pedido.
  - Ranking dos funcionários: nome, total de pedidos, soma dos valores vendidos.

### Tecnologias
- Python
- psycopg2 (driver de conexão com PostgreSQL)
- SQLAlchemy (ORM)
- Banco de dados PostgreSQL

### Como Rodar o Projeto
1. Clone o repositório:

git clone https://github.com/seu-usuario/northwind-orders-app.git

2. Instale as dependências:

pip install -r requirements.txt

3. Execute o projeto:

Pode usar o play de executar arquivos do visual studio ou python main.py




