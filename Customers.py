from Database import conn


class Customer:

    def create_table(self):
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                contact VARCHAR(100) NOT NULL
            )
        """)

        conn.commit()
        cur.close()

        print("Customer table created!")


    def insert_customer(self, name, contact):
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO customers (name, contact)
            VALUES (%s, %s)
        """, (name, contact))

        conn.commit()
        cur.close()

        print("Customer inserted!")


    def update_customer(self, customer_id, name=None, contact=None):
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM customers WHERE id = %s",
            (customer_id,)
        )

        customer = cur.fetchone()

        if not customer:
            print("Customer not found!")
            cur.close()
            return

        if name is not None and contact is not None:

            cur.execute("""
                UPDATE customers
                SET name = %s, contact = %s
                WHERE id = %s
            """, (name, contact, customer_id))

        elif name is not None:

            cur.execute("""
                UPDATE customers
                SET name = %s
                WHERE id = %s
            """, (name, customer_id))

        elif contact is not None:

            cur.execute("""
                UPDATE customers
                SET contact = %s
                WHERE id = %s
            """, (contact, customer_id))

        conn.commit()
        cur.close()

        print("Customer updated!")


    def delete_customer(self, customer_id):
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM customers WHERE id = %s",
            (customer_id,)
        )

        conn.commit()
        cur.close()

        print("Customer deleted!")


    def get_all_customers(self):
        cur = conn.cursor()

        cur.execute("SELECT * FROM customers")

        customers = cur.fetchall()

        cur.close()

        return customers


    def view_customer_by_id(self, customer_id):
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM customers WHERE id = %s",
            (customer_id,)
        )

        customer = cur.fetchone()

        cur.close()

        return customer


    def customer_menu(self):

        while True:

            print("\n===== CUSTOMER MANAGEMENT =====")
            print("1. Create Table")
            print("2. Insert Customer")
            print("3. Update Customer")
            print("4. Delete Customer")
            print("5. View Customers")
            print("6. View Customer by ID")
            print("0. Exit")

            choice = input("Enter choice: ")

            if choice == "1":

                self.create_table()

            elif choice == "2":

                name = input("Enter customer name: ")
                contact = input("Enter customer contact: ")

                self.insert_customer(name, contact)

            elif choice == "3":

                customer_id = int(input("Enter customer ID: "))

                name = input(
                    "Enter new customer name (press Enter to keep old): "
                )

                contact = input(
                    "Enter new customer contact (press Enter to keep old): "
                )

                name = name if name else None
                contact = contact if contact else None

                self.update_customer(
                    customer_id,
                    name,
                    contact
                )

            elif choice == "4":

                customer_id = int(
                    input("Enter customer ID: ")
                )

                self.delete_customer(customer_id)

            elif choice == "5":

                customers = self.get_all_customers()

                if not customers:
                    print("No customers found.")

                else:
                    print("\n===== CUSTOMERS =====")

                    for customer in customers:
                        print(customer)

            elif choice == "6":

                customer_id = int(
                    input("Enter customer ID: ")
                )

                customer = self.view_customer_by_id(
                    customer_id
                )

                if customer:
                    print(customer)
                else:
                    print("Customer not found!")

            elif choice == "0":

                print("Exiting Customer Management...")
                break

            else:

                print("Invalid choice. Please try again.")


if __name__ == "__main__":

    customer = Customer()
    customer.customer_menu()