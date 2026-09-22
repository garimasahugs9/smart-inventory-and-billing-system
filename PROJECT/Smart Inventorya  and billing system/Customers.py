import psycopg2

from Database import conn

class Customer:
    def __init__(self,name,contact):
        self.name =name
        self. contact = contact

    def create_table(self):
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS customers(
            is SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
            
            )"""
        )
        conn.commit()
        cur.close()


def insert_customers(self,name ,contact):
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO CUSTOMERS(name ,contact)
            VALUES(%s,%s)
            
            )""",
            (name,contact)
        )
        conn.commit()
        cur.close()

def update_customers(self,customer_id,name = None, contact = None):
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id))
        customer = cur.fetchone()
        if not customer:
            print(">>>>> Customer not found!")
            cur.close()
            return
        update_fields=[]
        if name :
             update_fields.append(f"name='{name}'")
        if contact:
             update_fields.append(f"contact = '{contact}'")
        update_query = f"UPDATE customets SET{','.join(update_fields)} WHERE id = %s"

        cur.execute(update_query,(customer_id,))          
        conn.commit()
        cur.close()



def delet_customers(self,customer_id):
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM customers WHERE id =%s,)",
            (customer_id),
        )
        conn.commit()
        cur.close()

def get_all_customers(self):
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM customers"
        )
        Customers = cur.fetchall()
        
        cur.close()

        return Customer



def customet_menu (self):
    while True:
        print("1. Create table")
        print("1. Insert Customer")
        print("1. Update Customer")
        print("1. Delete Customer")
        print("1. View Customer")
        choice = input("Enter choice:")
        if choice == "1":
              Customer.create_table()


        
    