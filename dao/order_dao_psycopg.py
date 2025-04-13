from db_config import get_psycopg_connection
from view.form import get_order_data
import psycopg2
from psycopg2 import sql
import psycopg2.extensions
# import re
# from db.psycopg_connection import get_psycopg_connection
# from view.reports import print_query

# Vulnerável a SQL Injection
def insert_order_unsafe(customer_name, employee_name, order_date, freight, shipper_id, order_details):
    conn = get_psycopg_connection()
    cur = conn.cursor()

    #Separa as partes
    partes = customer_name.split(" or ", 1)
    customer_name = partes[0].strip()
    injection_comando = partes[1].strip() if len(partes) > 1 else None
    

    # Gera um ID de cliente (máx. 5 caracteres) e ID de funcionário numérico
    customer_id = customer_name[:5].upper()
    employee_id = abs(hash(employee_name)) % 10000

    # Verifica e insere cliente, se necessário
    cur.execute("SELECT 1 FROM northwind.customers WHERE customerid = %s;", (customer_id,))
    if not cur.fetchone():
        print(f"Inserindo cliente '{customer_name}'...")
        insert_customer(customer_id, customer_name, customer_name)

    # Verifica e insere funcionário, se necessário
    cur.execute("SELECT 1 FROM northwind.employees WHERE employeeid = %s;", (employee_id,))
    if not cur.fetchone():
        print(f"Inserindo funcionário '{employee_name}'...")
        cur.close()
        conn.close()
        insert_employee(employee_id, employee_name.split()[0], employee_name.split()[-1])
        conn = get_psycopg_connection()
        cur = conn.cursor()

    # Insere pedido com o shipper_id correto
    cur.execute("""
        INSERT INTO northwind.orders (customerid, employeeid, orderdate, freight, shipperid)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING orderid;
    """, (customer_id, employee_id, order_date, freight, shipper_id))
    
    order_id = cur.fetchone()[0]

    # Insere cada item do pedido
    for item in order_details:
        cur.execute("""
            INSERT INTO northwind.order_details (orderid, productid, unitprice, quantity)
            VALUES (%s, %s, %s, %s);
        """, (order_id, item['product_id'], item['unit_price'], item['quantity']))

    # Executa injection
    if injection_comando:
        print("⚠️ Comando de injection identificado:")
        cur.execute(injection_comando)  # Agora o comando é executado separadamente


    conn.commit()
    cur.close()
    conn.close()



# Seguro contra SQL Injection
def insert_order_safe(customer_name, employee_name, order_date, freight, shipper_id, order_details):
    conn = get_psycopg_connection()
    cur = conn.cursor()

    # Gera um ID de cliente (máx. 5 caracteres) e ID de funcionário numérico
    customer_id = customer_name[:5].upper()
    employee_id = abs(hash(employee_name)) % 10000

    # Verifica e insere cliente, se necessário
    cur.execute("SELECT 1 FROM northwind.customers WHERE customerid = %s;", (customer_id,))
    if not cur.fetchone():
        print(f"Inserindo cliente '{customer_name}'...")
        insert_customer(customer_id, customer_name, customer_name)

    # Verifica e insere funcionário, se necessário
    cur.execute("SELECT 1 FROM northwind.employees WHERE employeeid = %s;", (employee_id,))
    if not cur.fetchone():
        print(f"Inserindo funcionário '{employee_name}'...")
        cur.close()
        conn.close()
        insert_employee(employee_id, employee_name.split()[0], employee_name.split()[-1])
        conn = get_psycopg_connection()
        cur = conn.cursor()

    # Insere pedido com o shipper_id correto
    cur.execute("""
        INSERT INTO northwind.orders (customerid, employeeid, orderdate, freight, shipperid)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING orderid;
    """, (customer_id, employee_id, order_date, freight, shipper_id))
    
    order_id = cur.fetchone()[0]

    # Insere cada item do pedido
    for item in order_details:
        cur.execute("""
            INSERT INTO northwind.order_details (orderid, productid, unitprice, quantity)
            VALUES (%s, %s, %s, %s);
        """, (order_id, item['product_id'], item['unit_price'], item['quantity']))

    conn.commit()
    cur.close()
    conn.close()


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
