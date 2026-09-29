from Customers import Customer
from Products import Product
from Sales import Sale


def main_menu():

    customer = Customer()
    product = Product()
    sale = Sale()

    while True:

        print("\n===================================")
        print("     E-COMMERCE MANAGEMENT SYSTEM")
        print("===================================")

        print("1. Customer Management")
        print("2. Product Management")
        print("3. Sales Management")
        print("4. Exit Application")

        choice = input("Enter choice: ")

        if choice == "1":

            customer.customer_menu()

        elif choice == "2":

            product.product_menu()

        elif choice == "3":

            sale.sales_menu()

        elif choice == "4":

            print("Exiting Application...")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":

    main_menu()