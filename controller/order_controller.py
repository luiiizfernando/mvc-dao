from dao.order_dao_psycopg import insert_order_safe, insert_order_unsafe
# from dao.order_dao_sqlalchemy import insert_order_sqlalchemy
from dao.order_dao_sqlalchemy import insert_order_sqlalchemy_completo

from view.form import get_order_data
import datetime

def add_order(driver="safe"):
    #customer_id, employee_id = get_order_data()
    nome_cliente, nome_funcionario, data_pedido, frete, id_transportadora, itens = get_order_data()

    try:
        if driver == "unsafe":
            insert_order_unsafe(
                nome_cliente,
                nome_funcionario,
                data_pedido,
                frete,
                id_transportadora,
                itens
            )
            print("Pedido inserido com sucesso! (modo UNSAFE)")
        elif driver == "safe":
            insert_order_safe(
                nome_cliente,
                nome_funcionario,
                data_pedido,
                frete,
                id_transportadora,
                itens
            )
            print("Pedido inserido com sucesso! (modo SAFE)")
        elif driver == "orm":
            insert_order_sqlalchemy_completo(
                nome_cliente,
                nome_funcionario,
                data_pedido,
                frete,
                id_transportadora,
                itens
            )
            print("Pedido inserido com sucesso! (modo ORM)")
        else:
            print(f"Modo '{driver}' não reconhecido.")
    except Exception as e:
        print("Erro durante a inserção do pedido:", e)
