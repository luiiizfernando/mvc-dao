from db_config import get_psycopg_connection
import psycopg2
from psycopg2 import sql

def insert_customer(customer_id, company_name, contact_name):
    conn = get_psycopg_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO northwind.customers (customerid, companyname, contactname)
        VALUES (%s, %s, %s);
    """, (customer_id[:5], company_name, contact_name))
    conn.commit()
    cur.close()
    conn.close()

def insert_employee(employee_id, first_name, last_name):
    conn = get_psycopg_connection()
    cur = conn.cursor()
    
    cur.execute("""
        INSERT INTO northwind.employees (employeeid, firstname, lastname)
        VALUES (%s, %s, %s);
    """, (employee_id, first_name[:10], last_name[:10]))
    conn.commit()
    cur.close()
    conn.close()

def insert_order_sqlalchemy_completo(customer_name, employee_name, order_date, freight, shipper_id, items):
    # Estabelecendo a conexão com o banco de dados
    conn = get_psycopg_connection()
    if conn is None:
        print("Não foi possível estabelecer a conexão com o banco de dados.")
        return

    try:
        # Iniciando a transação
        cur = conn.cursor()

        customer_id = customer_name[:5].upper()

        # Verificando e inserindo o cliente se necessário
        cur.execute("SELECT 1 FROM northwind.customers WHERE customerid = %s;", (customer_id,))
        if not cur.fetchone():
            print(f"Inserindo cliente '{customer_name}'...")
            cur.close()
            conn.close()
            insert_customer(customer_id, customer_name, customer_name) # contact name = company name
            conn = get_psycopg_connection()
            cur = conn.cursor()

        employee_id = abs(hash(employee_name)) % 10000

        # Verifica e insere funcionário, se necessário
        cur.execute("SELECT 1 FROM northwind.employees WHERE employeeid = %s;", (employee_id,))
        if not cur.fetchone():
            print(f"Inserindo funcionário '{employee_name}'...")
            cur.close()
            conn.close()
            if len(employee_name.split()) >= 2:
                insert_employee(employee_id, employee_name.split()[0], employee_name.split()[1])
            else:
                insert_employee(employee_id, employee_name, "") # last name = ""
            conn = get_psycopg_connection()
            cur = conn.cursor()

        # Inserindo o pedido
        cur.execute(
            """
            INSERT INTO northwind.orders (customerid, employeeid, orderdate, freight, shipperid) 
            VALUES (%s, %s, %s, %s, %s) RETURNING orderid
            """,
            (customer_id, employee_id, order_date, freight, shipper_id)
        )
        order_id = cur.fetchone()[0]

        # Inserindo os itens do pedido
        for item in items:
            cur.execute(
                """
                INSERT INTO northwind.order_details (orderid, productid, unitprice, quantity)
                VALUES (%s, %s, %s, %s)
                """,
                (order_id, item['product_id'], item['unit_price'], item['quantity'])
            )

        # Commit da transação
        conn.commit()
        print(f"Pedido {order_id} inserido com sucesso!")

    except Exception as e:
        print(f"Erro ao inserir pedido: {e}")
        conn.rollback()

    finally:
        if 'cur' in locals() and cur is not None:
            cur.close()
        if 'conn' in locals() and conn is not None:
            conn.close()