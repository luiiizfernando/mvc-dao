from controller.order_controller import add_order
from controller.report_controller import get_order_details, get_employee_ranking
from view.reports import get_order_id_input, get_date_range

def main():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Inserir pedido (vulnerável)")
        print("2. Inserir pedido (seguro)")
        print("3. Inserir pedido (ORM - SQLAlchemy)")
        print("4. Consultar detalhes de pedido")
        print("5. Consultar ranking de funcionários")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            add_order(driver="unsafe")
        elif opcao == "2":
            add_order(driver="safe")
        elif opcao == "3":
            add_order(driver="orm")
        elif opcao == "4":
            order_id = get_order_id_input()
            get_order_details(order_id)
        elif opcao == "5":
            start, end = get_date_range()
            get_employee_ranking(start, end)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
