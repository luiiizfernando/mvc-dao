import psycopg2
from datetime import datetime, date
from db_config import get_psycopg_connection


def listar_transportadoras():
    conn = get_psycopg_connection()
    cur = conn.cursor()
    cur.execute("SELECT shipperid, companyname FROM northwind.shippers;")
    shippers = cur.fetchall()
    cur.close()
    conn.close()
    return shippers


def get_order_data():
    print("==== Cadastro de Pedido ====")
    nome_cliente = input("Nome do cliente: ")
    nome_funcionario = input("Nome do vendedor: ")

    # Lê a data do pedido com fallback para data atual
    while True:
        entrada_data = input("Data do pedido (YYYY-MM-DD) [pressione Enter para hoje]: ").strip()
        if entrada_data == "":
            data_pedido = datetime.now()
            break
        try:
            data_pedido = datetime.strptime(entrada_data, "%Y-%m-%d %H:%M:%S").date()
            break
        except ValueError:
            print("Data inválida! Use o formato YYYY-MM-DD.")

    frete = float(input("Valor do frete: "))

    # Transportadora
    print("\nTransportadoras disponíveis:")
    for shipper in listar_transportadoras():
        print(f"{shipper[0]} - {shipper[1]}")
    shipper_id = int(input("Digite o ID da transportadora: "))

    # Itens do pedido
    itens = []
    while True:
        print("\nAdicione um item ao pedido:")
        produto_id = int(input("ID do produto: "))
        preco_unitario = float(input("Preço unitário: "))
        quantidade = int(input("Quantidade: "))
        itens.append({
            'product_id': produto_id,
            'unit_price': preco_unitario,
            'quantity': quantidade
        })

        continuar = input("Deseja adicionar mais um item? (s/n): ").lower()
        if continuar != 's':
            break

    return nome_cliente, nome_funcionario, data_pedido, frete, shipper_id, itens

