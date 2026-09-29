from Database import conn


class Product:

    def create_table(self):
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT,
                price NUMERIC(10, 2) NOT NULL,
                quantity INTEGER NOT NULL
            )
        """)

        conn.commit()
        cur.close()

        print("Product table created!")

    def insert_product(self, name, description, price, quantity):
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO products (name, description, price, quantity)
            VALUES (%s, %s, %s, %s)
        """, (name, description, price, quantity))

        conn.commit()
        cur.close()

        print("Product inserted!")

    def update_product(
        self,
        product_id,
        name=None,
        description=None,
        price=None,
        quantity=None
    ):
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM products WHERE id = %s",
            (product_id,)
        )

        product = cur.fetchone()

        if not product:
            print("Product not found!")
            cur.close()
            return

        if name is not None:
            cur.execute("""
                UPDATE products
                SET name = %s
                WHERE id = %s
            """, (name, product_id))

        if description is not None:
            cur.execute("""
                UPDATE products
                SET description = %s
                WHERE id = %s
            """, (description, product_id))

        if price is not None:
            cur.execute("""
                UPDATE products
                SET price = %s
                WHERE id = %s
            """, (price, product_id))

        if quantity is not None:
            cur.execute("""
                UPDATE products
                SET quantity = %s
                WHERE id = %s
            """, (quantity, product_id))

        conn.commit()
        cur.close()

        print("Product updated!")

    def delete_product(self, product_id):
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM products WHERE id = %s",
            (product_id,)
        )

        conn.commit()
        cur.close()

        print("Product deleted!")

    def view_products(self):
        cur = conn.cursor()

        cur.execute("SELECT * FROM products")

        products = cur.fetchall()

        cur.close()

        return products

    def view_product_by_id(self, product_id):
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM products WHERE id = %s",
            (product_id,)
        )

        product = cur.fetchone()

        cur.close()

        return product

    def product_menu(self):

        while True:

            print("\n===== PRODUCT MANAGEMENT =====")
            print("1. Create Table")
            print("2. Insert Product")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. View Products")
            print("6. View Product by ID")
            print("0. Exit")

            choice = input("Enter choice: ")

            if choice == "1":

                self.create_table()

            elif choice == "2":

                name = input("Enter product name: ")
                description = input("Enter product description: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))

                self.insert_product(
                    name,
                    description,
                    price,
                    quantity
                )

            elif choice == "3":

                product_id = int(input("Enter product ID: "))

                name = input(
                    "Enter new name (press Enter to keep old): "
                )

                description = input(
                    "Enter new description (press Enter to keep old): "
                )

                price = input(
                    "Enter new price (press Enter to keep old): "
                )

                quantity = input(
                    "Enter new quantity (press Enter to keep old): "
                )

                name = name if name else None
                description = description if description else None
                price = float(price) if price else None
                quantity = int(quantity) if quantity else None

                self.update_product(
                    product_id,
                    name,
                    description,
                    price,
                    quantity
                )

            elif choice == "4":

                product_id = int(
                    input("Enter product ID: ")
                )

                self.delete_product(product_id)

            elif choice == "5":

                products = self.view_products()

                if not products:
                    print("No products found.")

                else:
                    print("\n===== PRODUCTS =====")

                    for product in products:
                        print(product)

            elif choice == "6":

                product_id = int(
                    input("Enter product ID: ")
                )

                product = self.view_product_by_id(product_id)

                if product:
                    print(product)

                else:
                    print("Product not found!")

            elif choice == "0":

                print("Exiting Product Management...")
                break

            else:

                print("Invalid choice. Please try again.")


if __name__ == "__main__":

    product = Product()
    product.product_menu()