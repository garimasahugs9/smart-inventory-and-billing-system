from Database import conn


class SaleItem:

    def create_table(self):
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS sale_items (
                id SERIAL PRIMARY KEY,
                sale_id INTEGER REFERENCES sales(id) ON DELETE CASCADE,
                product_id INTEGER REFERENCES products(id),
                quantity INTEGER NOT NULL
            )
        """)

        conn.commit()
        cur.close()

        print("Sale Items table created!")

    def add_item(self, sale_id, product_id, quantity):
        cur = conn.cursor()

        cur.execute("""
            SELECT id
            FROM products
            WHERE id = %s
        """, (product_id,))

        product = cur.fetchone()

        if not product:
            print("Product not found!")
            cur.close()
            return False

        cur.execute("""
            INSERT INTO sale_items
            (sale_id, product_id, quantity)
            VALUES (%s, %s, %s)
        """, (
            sale_id,
            product_id,
            quantity
        ))

        conn.commit()
        cur.close()

        print("Product added to sale!")

        return True

    def get_items_by_sale(self, sale_id):
        cur = conn.cursor()

        cur.execute("""
            SELECT
                si.id,
                si.sale_id,
                si.product_id,
                p.name,
                si.quantity,
                p.price,
                (si.quantity * p.price) AS subtotal
            FROM sale_items si
            JOIN products p
                ON si.product_id = p.id
            WHERE si.sale_id = %s
        """, (sale_id,))

        items = cur.fetchall()

        cur.close()

        return items

    def view_sale_items(self, sale_id):
        items = self.get_items_by_sale(sale_id)

        if not items:
            print("No items found for this sale.")
            return

        print("\n===== SALE ITEMS =====")

        for item in items:
            print(
                "Item ID:",
                item[0],
                "| Product:",
                item[3],
                "| Quantity:",
                item[4],
                "| Price:",
                item[5],
                "| Subtotal:",
                item[6]
            )

    def sale_item_menu(self):

        while True:

            print("\n===== SALE ITEM MANAGEMENT =====")
            print("1. Create Sale Items Table")
            print("2. Add Item")
            print("3. View Sale Items")
            print("0. Exit")

            choice = input("Enter choice: ")

            if choice == "1":

                self.create_table()

            elif choice == "2":

                sale_id = int(
                    input("Enter sale ID: ")
                )

                product_id = int(
                    input("Enter product ID: ")
                )

                quantity = int(
                    input("Enter quantity: ")
                )

                self.add_item(
                    sale_id,
                    product_id,
                    quantity
                )

            elif choice == "3":

                sale_id = int(
                    input("Enter sale ID: ")
                )

                self.view_sale_items(sale_id)

            elif choice == "0":

                print("Exiting Sale Item Management...")
                break

            else:

                print("Invalid choice. Please try again.")


if __name__ == "__main__":

    sale_item = SaleItem()
    sale_item.sale_item_menu()