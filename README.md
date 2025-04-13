# Northwind Orders App

## Descrição
Este projeto tem como objetivo implementar uma aplicação para inserção de pedidos no banco de dados **Northwind**, utilizando Python e os padrões de arquitetura **MVC** e **DAO**. O foco está na prática de segurança contra SQL Injection, uso de driver de conexão e mapeamento objeto-relacional com ORM (SQLAlchemy).

> Atividade prática 2 da disciplina **SPAD02 - Banco de Dados 2**.

## Funcionalidades
- Inserção de pedidos no banco de dados de três formas:
  - SQL Inseguro (com SQL Injection proposital)
  - SQL Seguro (com parâmetros - `psycopg2`)
  - ORM (usando SQLAlchemy)
- Verificação e inserção automática de clientes e funcionários, se não existirem.
- Relatórios:
  - 📄 **Detalhes de um pedido**: número, data, cliente, vendedor, itens com produto, quantidade e preço.
  - 🏆 **Ranking de funcionários**: total de pedidos e valor vendido por período.

## Tecnologias Utilizadas
- Python 3.12+
- PostgreSQL
- psycopg2
- SQLAlchemy
- Sqlacodegen (para gerar modelos)
- Jupyter / Visual Studio Code (opcional para execução)


## Como Executar
1. **Clone o repositório**:
```bash
git clone https://github.com/luiiizfernando/mvc-dao.git
cd mvc-dao

2. Instale as dependências:

pip install -r requirements.txt

3. Configure a conexão com o banco no db_config.py: Preencha os dados da sua conexão PostgreSQL.

4. Execute a aplicação:

python main.py

Você também pode executar diretamente pelo Visual Studio Code ou outro editor de sua preferência.