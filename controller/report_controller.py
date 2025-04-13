from db_config import get_psycopg_connection

def get_order_details(order_id):
    conn = get_psycopg_connection()
    cur = conn.cursor()

    query = """
    SELECT 
        o.orderid,
        o.orderdate,
        c.companyname AS cliente,
        e.firstname || ' ' || e.lastname AS funcionario,
        p.productname,
        od.unitprice,
        od.quantity,
        od.discount
    FROM northwind.orders o
    JOIN northwind.customers c ON o.customerid = c.customerid
    JOIN northwind.employees e ON o.employeeid = e.employeeid
    JOIN northwind.order_details od ON o.orderid = od.orderid
    JOIN northwind.products p ON od.productid = p.productid
    WHERE o.orderid = %s;
    """

    cur.execute(query, (order_id,))
    rows = cur.fetchall()

    if rows:
        print(f"\nPedido ID: {rows[0][0]}")
        print(f"Data: {rows[0][1]}")
        print(f"Cliente: {rows[0][2]}")
        print(f"Funcionário: {rows[0][3]}")
        print("\nItens do Pedido:")
        for row in rows:
            print(f"- {row[4]} | Preço: {row[5]} | Quantidade: {row[6]} | Desconto: {row[7]}")
    else:
        print("Pedido não encontrado.")

    cur.close()
    conn.close()


def get_employee_ranking(start_date, end_date):
    conn = get_psycopg_connection()
    cur = conn.cursor()

    query = """
    SELECT 
        e.firstname || ' ' || e.lastname AS funcionario,
        COUNT(o.orderid) AS total_pedidos
    FROM northwind.orders o
    JOIN northwind.employees e ON o.employeeid = e.employeeid
    WHERE o.orderdate BETWEEN %s AND %s
    GROUP BY funcionario
    ORDER BY total_pedidos DESC;
    """

    cur.execute(query, (start_date, end_date))
    rows = cur.fetchall()

    print(f"\nRanking de funcionários ({start_date} a {end_date}):\n")
    for row in rows:
        print(f"{row[0]} - {row[1]} pedidos")

    cur.close()
    conn.close()
