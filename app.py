import streamlit as st
from datetime import date

from Database import conn
from Customers import Customer
from Products import Product
from Sales import Sale
from Sale_Item import SaleItem


# ---------------------------------------------------------
# Initialize database tables
# ---------------------------------------------------------
def initialize_tables():
    try:
        customer = Customer()
        product = Product()
        sale = Sale()
        sale_item = SaleItem()

        customer.create_table()
        product.create_table()
        sale.create_table()
        sale_item.create_table()

        st.success("Database tables are ready!")

    except Exception as e:
        st.error(f"Error initializing tables: {e}")


# ---------------------------------------------------------
# Helper: refresh Streamlit page
# ---------------------------------------------------------
def refresh():
    st.rerun()


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Smart Inventory and Billing System",
    page_icon="🏪",
    layout="wide"
)

st.title("🏪 Smart Inventory and Billing System")


# ---------------------------------------------------------
# Initialize tables once per Streamlit session
# ---------------------------------------------------------
if "tables_initialized" not in st.session_state:
    initialize_tables()
    st.session_state.tables_initialized = True


# Create class objects
customer = Customer()
product = Product()
sale = Sale()
sale_item = SaleItem()


# ---------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------
st.sidebar.header("Navigation")

menu_option = st.sidebar.selectbox(
    "Choose an option:",
    [
        "Dashboard",
        "Customer Management",
        "Product Management",
        "Sales Management",
        "Analytics & Reports"
    ]
)


# =========================================================
# DASHBOARD
# =========================================================
if menu_option == "Dashboard":

    st.header("📊 Dashboard")
    st.write(
        "Welcome to the Smart Inventory and Billing System!"
    )
    st.write(
        "Use the navigation menu to manage customers, products, "
        "sales, and reports."
    )

    try:
        cur = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM customers")
        customer_count = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM products")
        product_count = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM sales")
        sales_count = cur.fetchone()[0]

        cur.close()

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Customers", customer_count)
        col2.metric("Total Products", product_count)
        col3.metric("Total Sales", sales_count)

    except Exception as e:
        st.warning(f"Database statistics are not available: {e}")


# =========================================================
# CUSTOMER MANAGEMENT
# =========================================================
elif menu_option == "Customer Management":

    st.header("👥 Customer Management")

    customer_action = st.radio(
        "Select Action:",
        [
            "View All Customers",
            "Add New Customer",
            "Update Customer",
            "Delete Customer"
        ]
    )

    # -----------------------------------------------------
    # View customers
    # -----------------------------------------------------
    if customer_action == "View All Customers":

        st.subheader("All Customers")

        try:
            customers = customer.get_all_customers()

            if customers:
                st.table(
                    [
                        {
                            "ID": row[0],
                            "Name": row[1],
                            "Contact": row[2]
                        }
                        for row in customers
                    ]
                )
            else:
                st.info("No customers found.")

        except Exception as e:
            st.error(f"Error retrieving customers: {e}")

    # -----------------------------------------------------
    # Add customer
    # -----------------------------------------------------
    elif customer_action == "Add New Customer":

        st.subheader("Add New Customer")

        with st.form("add_customer_form"):

            name = st.text_input("Customer Name")
            contact = st.text_input("Contact Information")

            submitted = st.form_submit_button("Add Customer")

            if submitted:

                if name.strip() and contact.strip():

                    try:
                        customer.insert_customer(
                            name.strip(),
                            contact.strip()
                        )

                        st.success(
                            f"Customer '{name}' added successfully!"
                        )

                    except Exception as e:
                        st.error(f"Error adding customer: {e}")

                else:
                    st.warning(
                        "Please enter both customer name and contact."
                    )

    # -----------------------------------------------------
    # Update customer
    # -----------------------------------------------------
    elif customer_action == "Update Customer":

        st.subheader("Update Customer")

        try:
            customers = customer.get_all_customers()

            if customers:

                customer_options = {
                    f"{row[1]} (ID: {row[0]})": row[0]
                    for row in customers
                }

                selected = st.selectbox(
                    "Select Customer",
                    list(customer_options.keys())
                )

                selected_id = customer_options[selected]

                current = customer.view_customer_by_id(
                    selected_id
                )

                if current:

                    with st.form("update_customer_form"):

                        name = st.text_input(
                            "Customer Name",
                            value=current[1]
                        )

                        contact = st.text_input(
                            "Contact Information",
                            value=current[2]
                        )

                        submitted = st.form_submit_button(
                            "Update Customer"
                        )

                        if submitted:

                            try:
                                customer.update_customer(
                                    selected_id,
                                    name.strip(),
                                    contact.strip()
                                )

                                st.success(
                                    "Customer updated successfully!"
                                )

                            except Exception as e:
                                st.error(
                                    f"Error updating customer: {e}"
                                )

            else:
                st.info("No customers available to update.")

        except Exception as e:
            st.error(f"Error retrieving customers: {e}")

    # -----------------------------------------------------
    # Delete customer
    # -----------------------------------------------------
    elif customer_action == "Delete Customer":

        st.subheader("Delete Customer")

        try:
            customers = customer.get_all_customers()

            if customers:

                customer_options = {
                    f"{row[1]} (ID: {row[0]})": row[0]
                    for row in customers
                }

                selected = st.selectbox(
                    "Select Customer",
                    list(customer_options.keys())
                )

                if st.button("Delete Customer"):

                    customer_id = customer_options[selected]

                    try:
                        customer.delete_customer(customer_id)

                        st.success(
                            "Customer deleted successfully!"
                        )

                    except Exception as e:
                        st.error(
                            f"Error deleting customer: {e}"
                        )

            else:
                st.info("No customers available to delete.")

        except Exception as e:
            st.error(f"Error retrieving customers: {e}")


# =========================================================
# PRODUCT MANAGEMENT
# =========================================================
elif menu_option == "Product Management":

    st.header("📦 Product Management")

    product_action = st.radio(
        "Select Action:",
        [
            "View All Products",
            "Add New Product",
            "Update Product",
            "Delete Product"
        ]
    )

    # -----------------------------------------------------
    # View products
    # -----------------------------------------------------
    if product_action == "View All Products":

        st.subheader("All Products")

        try:
            products = product.view_products()

            if products:

                st.table(
                    [
                        {
                            "ID": row[0],
                            "Name": row[1],
                            "Description": row[2],
                            "Price": float(row[3]),
                            "Quantity": row[4]
                        }
                        for row in products
                    ]
                )

            else:
                st.info("No products found.")

        except Exception as e:
            st.error(f"Error retrieving products: {e}")

    # -----------------------------------------------------
    # Add product
    # -----------------------------------------------------
    elif product_action == "Add New Product":

        st.subheader("Add New Product")

        with st.form("add_product_form"):

            name = st.text_input("Product Name")
            description = st.text_area("Description")
            price = st.number_input(
                "Price",
                min_value=0.0,
                step=0.01
            )
            quantity = st.number_input(
                "Quantity",
                min_value=0,
                step=1
            )

            submitted = st.form_submit_button("Add Product")

            if submitted:

                if name.strip():

                    try:
                        product.insert_product(
                            name.strip(),
                            description.strip(),
                            price,
                            quantity
                        )

                        st.success(
                            f"Product '{name}' added successfully!"
                        )

                    except Exception as e:
                        st.error(f"Error adding product: {e}")

                else:
                    st.warning("Please enter a product name.")

    # -----------------------------------------------------
    # Update product
    # -----------------------------------------------------
    elif product_action == "Update Product":

        st.subheader("Update Product")

        try:
            products = product.view_products()

            if products:

                product_options = {
                    f"{row[1]} (ID: {row[0]})": row[0]
                    for row in products
                }

                selected = st.selectbox(
                    "Select Product",
                    list(product_options.keys())
                )

                selected_id = product_options[selected]

                current = product.view_product_by_id(
                    selected_id
                )

                if current:

                    with st.form("update_product_form"):

                        name = st.text_input(
                            "Product Name",
                            value=current[1]
                        )

                        description = st.text_area(
                            "Description",
                            value=current[2] or ""
                        )

                        price = st.number_input(
                            "Price",
                            min_value=0.0,
                            value=float(current[3]),
                            step=0.01
                        )

                        quantity = st.number_input(
                            "Quantity",
                            min_value=0,
                            value=int(current[4]),
                            step=1
                        )

                        submitted = st.form_submit_button(
                            "Update Product"
                        )

                        if submitted:

                            try:
                                product.update_product(
                                    selected_id,
                                    name.strip(),
                                    description.strip(),
                                    price,
                                    quantity
                                )

                                st.success(
                                    "Product updated successfully!"
                                )

                            except Exception as e:
                                st.error(
                                    f"Error updating product: {e}"
                                )

            else:
                st.info("No products available to update.")

        except Exception as e:
            st.error(f"Error retrieving products: {e}")

    # -----------------------------------------------------
    # Delete product
    # -----------------------------------------------------
    elif product_action == "Delete Product":

        st.subheader("Delete Product")

        try:
            products = product.view_products()

            if products:

                product_options = {
                    f"{row[1]} (ID: {row[0]})": row[0]
                    for row in products
                }

                selected = st.selectbox(
                    "Select Product",
                    list(product_options.keys())
                )

                if st.button("Delete Product"):

                    product_id = product_options[selected]

                    try:
                        product.delete_product(product_id)

                        st.success(
                            "Product deleted successfully!"
                        )

                    except Exception as e:
                        st.error(
                            f"Error deleting product: {e}"
                        )

            else:
                st.info("No products available to delete.")

        except Exception as e:
            st.error(f"Error retrieving products: {e}")


# =========================================================
# SALES MANAGEMENT
# =========================================================
elif menu_option == "Sales Management":

    st.header("💰 Sales Management")

    sales_action = st.radio(
        "Select Action:",
        [
            "Create New Sale",
            "View All Sales",
            "Generate Bill"
        ]
    )

    # -----------------------------------------------------
    # Create sale
    # -----------------------------------------------------
    if sales_action == "Create New Sale":

        st.subheader("Create New Sale")

        try:
            customers = customer.get_all_customers()

            if not customers:
                st.info(
                    "No customers available. "
                    "Please add a customer first."
                )

            else:

                customer_options = {
                    f"{row[1]} (ID: {row[0]})": row[0]
                    for row in customers
                }

                selected_customer = st.selectbox(
                    "Select Customer",
                    list(customer_options.keys())
                )

                customer_id = customer_options[
                    selected_customer
                ]

                if st.button("Create Sale"):

                    try:
                        sale_id = sale.insert_sale(
                            customer_id
                        )

                        st.session_state.active_sale_id = sale_id

                        st.success(
                            f"Sale created successfully! "
                            f"Sale ID: {sale_id}"
                        )

                    except Exception as e:
                        st.error(
                            f"Error creating sale: {e}"
                        )

                # -----------------------------------------
                # Add products to active sale
                # -----------------------------------------
                if "active_sale_id" in st.session_state:

                    sale_id = st.session_state.active_sale_id

                    st.markdown("---")
                    st.subheader(
                        f"Add Products to Sale #{sale_id}"
                    )

                    products = product.view_products()

                    if not products:

                        st.info(
                            "No products available. "
                            "Please add products first."
                        )

                    else:

                        product_options = {
                            f"{row[1]} "
                            f"(ID: {row[0]}, Stock: {row[4]}, "
                            f"Price: ₹{float(row[3]):.2f})": row[0]
                            for row in products
                            if row[4] > 0
                        }

                        if not product_options:

                            st.warning(
                                "All products are out of stock."
                            )

                        else:

                            selected_product = st.selectbox(
                                "Select Product",
                                list(product_options.keys())
                            )

                            product_id = product_options[
                                selected_product
                            ]

                            product_details = (
                                product.view_product_by_id(
                                    product_id
                                )
                            )

                            available_quantity = int(
                                product_details[4]
                            )

                            quantity = st.number_input(
                                "Quantity",
                                min_value=1,
                                max_value=available_quantity,
                                value=1,
                                step=1
                            )

                            if st.button(
                                "Add Product to Sale"
                            ):

                                try:
                                    added = sale.add_sale_item(
                                        sale_id,
                                        product_id,
                                        quantity
                                    )

                                    if added:
                                        st.success(
                                            "Product added "
                                            "to sale!"
                                        )
                                    else:
                                        st.error(
                                            "Could not add "
                                            "product to sale."
                                        )

                                except Exception as e:
                                    st.error(
                                        f"Error adding item: {e}"
                                    )

                    # -------------------------------------
                    # Show current items
                    # -------------------------------------
                    st.markdown("---")
                    st.subheader("Current Sale")

                    try:
                        items = sale_item.get_items_by_sale(
                            sale_id
                        )

                        if items:

                            st.table(
                                [
                                    {
                                        "Product": row[3],
                                        "Quantity": row[4],
                                        "Price": float(row[5]),
                                        "Subtotal": float(row[6])
                                    }
                                    for row in items
                                ]
                            )

                            total = sum(
                                float(row[6])
                                for row in items
                            )

                            st.metric(
                                "Current Total",
                                f"₹{total:.2f}"
                            )

                        else:
                            st.info(
                                "No products have been added yet."
                            )

                    except Exception as e:
                        st.error(
                            f"Error displaying sale items: {e}"
                        )

                    if st.button("Finish Sale"):

                        try:
                            sale.update_sale_total(
                                sale_id
                            )

                            st.success(
                                f"Sale #{sale_id} completed!"
                            )

                            del st.session_state.active_sale_id

                        except Exception as e:
                            st.error(
                                f"Error finishing sale: {e}"
                            )

        except Exception as e:
            st.error(
                f"Error retrieving sales information: {e}"
            )

    # -----------------------------------------------------
    # View all sales
    # -----------------------------------------------------
    elif sales_action == "View All Sales":

        st.subheader("All Sales")

        try:
            sales = sale.view_sales()

            if sales:

                st.table(
                    [
                        {
                            "Sale ID": row[0],
                            "Customer ID": row[1],
                            "Sale Date": str(row[2]),
                            "Total Amount": float(row[3])
                        }
                        for row in sales
                    ]
                )

            else:
                st.info("No sales found.")

        except Exception as e:
            st.error(
                f"Error retrieving sales: {e}"
            )

    # -----------------------------------------------------
    # Generate bill
    # -----------------------------------------------------
    elif sales_action == "Generate Bill":

        st.subheader("Generate Bill")

        try:
            sales = sale.view_sales()

            if not sales:

                st.info("No sales available.")

            else:

                sale_options = {
                    f"Sale #{row[0]} - "
                    f"Customer ID: {row[1]} - "
                    f"₹{float(row[3]):.2f}": row[0]
                    for row in sales
                }

                selected = st.selectbox(
                    "Select Sale",
                    list(sale_options.keys())
                )

                selected_sale_id = sale_options[selected]

                if st.button("Generate Bill"):

                    sale_details = sale.view_sale_by_id(
                        selected_sale_id
                    )

                    if sale_details:

                        items = (
                            sale_item.get_items_by_sale(
                                selected_sale_id
                            )
                        )

                        st.markdown("---")
                        st.subheader("🧾 BILL")

                        st.write(
                            f"**Sale ID:** {sale_details[0]}"
                        )
                        st.write(
                            f"**Customer ID:** "
                            f"{sale_details[1]}"
                        )
                        st.write(
                            f"**Sale Date:** "
                            f"{sale_details[2]}"
                        )

                        st.markdown("---")

                        if items:

                            st.table(
                                [
                                    {
                                        "Product": row[3],
                                        "Quantity": row[4],
                                        "Price": float(row[5]),
                                        "Subtotal": float(row[6])
                                    }
                                    for row in items
                                ]
                            )

                        st.markdown("---")

                        st.metric(
                            "TOTAL AMOUNT",
                            f"₹{float(sale_details[3]):.2f}"
                        )

        except Exception as e:
            st.error(
                f"Error generating bill: {e}"
            )


# =========================================================
# ANALYTICS & REPORTS
# =========================================================
elif menu_option == "Analytics & Reports":

    st.header("📈 Analytics & Reports")

    analytics_action = st.radio(
        "Select Report:",
        [
            "Sales Summary",
            "Sales by Date Range",
            "Top Selling Products",
            "Low Stock Alert",
            "Customer Purchase History"
        ]
    )

    # -----------------------------------------------------
    # Sales summary
    # -----------------------------------------------------
    if analytics_action == "Sales Summary":

        st.subheader("Sales Summary")

        try:
            cur = conn.cursor()

            cur.execute(
                """
                SELECT
                    COUNT(*),
                    COALESCE(SUM(total_amount), 0)
                FROM sales
                """
            )

            result = cur.fetchone()

            total_sales = result[0]
            total_revenue = float(result[1])

            col1, col2 = st.columns(2)

            col1.metric(
                "Total Sales",
                total_sales
            )

            col2.metric(
                "Total Revenue",
                f"₹{total_revenue:.2f}"
            )

            cur.execute(
                """
                SELECT
                    DATE(sale_date),
                    SUM(total_amount)
                FROM sales
                GROUP BY DATE(sale_date)
                ORDER BY DATE(sale_date)
                """
            )

            sales_data = cur.fetchall()

            cur.close()

            if sales_data:

                chart_data = {
                    str(row[0]): float(row[1])
                    for row in sales_data
                }

                st.subheader("Daily Sales Trend")
                st.line_chart(chart_data)

            else:
                st.info(
                    "No sales data available."
                )

        except Exception as e:
            st.error(
                f"Error generating sales summary: {e}"
            )

    # -----------------------------------------------------
    # Sales by date range
    # -----------------------------------------------------
    elif analytics_action == "Sales by Date Range":

        st.subheader("Sales by Date Range")

        col1, col2 = st.columns(2)

        with col1:
            start_date = st.date_input(
                "Start Date",
                date.today()
            )

        with col2:
            end_date = st.date_input(
                "End Date",
                date.today()
            )

        if st.button("Get Sales Report"):

            if start_date > end_date:

                st.warning(
                    "End date must be after or equal "
                    "to start date."
                )

            else:

                try:
                    cur = conn.cursor()

                    cur.execute(
                        """
                        SELECT
                            s.id,
                            s.customer_id,
                            s.sale_date,
                            s.total_amount
                        FROM sales s
                        WHERE DATE(s.sale_date)
                            BETWEEN %s AND %s
                        ORDER BY s.sale_date DESC
                        """,
                        (start_date, end_date)
                    )

                    sales_data = cur.fetchall()

                    cur.close()

                    if sales_data:

                        st.table(
                            [
                                {
                                    "Sale ID": row[0],
                                    "Customer ID": row[1],
                                    "Date": str(row[2]),
                                    "Amount": float(row[3])
                                }
                                for row in sales_data
                            ]
                        )

                        total_amount = sum(
                            float(row[3])
                            for row in sales_data
                        )

                        col1, col2 = st.columns(2)

                        col1.metric(
                            "Total Sales",
                            len(sales_data)
                        )

                        col2.metric(
                            "Total Revenue",
                            f"₹{total_amount:.2f}"
                        )

                    else:
                        st.info(
                            "No sales found for the "
                            "selected date range."
                        )

                except Exception as e:
                    st.error(
                        f"Error retrieving sales data: {e}"
                    )

    # -----------------------------------------------------
    # Top selling products
    # -----------------------------------------------------
    elif analytics_action == "Top Selling Products":

        st.subheader("Top Selling Products")

        try:
            cur = conn.cursor()

            cur.execute(
                """
                SELECT
                    p.name,
                    SUM(si.quantity) AS total_quantity
                FROM sale_items si
                JOIN products p
                    ON si.product_id = p.id
                GROUP BY p.id, p.name
                ORDER BY total_quantity DESC
                LIMIT 10
                """
            )

            top_products = cur.fetchall()

            cur.close()

            if top_products:

                st.table(
                    [
                        {
                            "Product": row[0],
                            "Units Sold": int(row[1])
                        }
                        for row in top_products
                    ]
                )

                product_names = [
                    row[0]
                    for row in top_products
                ]

                quantities = [
                    int(row[1])
                    for row in top_products
                ]

                st.bar_chart(
                    dict(
                        zip(
                            product_names,
                            quantities
                        )
                    )
                )

            else:
                st.info(
                    "No sales data available."
                )

        except Exception as e:
            st.error(
                f"Error retrieving top selling products: {e}"
            )

    # -----------------------------------------------------
    # Low stock
    # -----------------------------------------------------
    elif analytics_action == "Low Stock Alert":

        st.subheader("Low Stock Alert")

        try:
            cur = conn.cursor()

            cur.execute(
                """
                SELECT name, quantity
                FROM products
                WHERE quantity < 10
                ORDER BY quantity ASC
                """
            )

            low_stock = cur.fetchall()

            cur.close()

            if low_stock:

                st.table(
                    [
                        {
                            "Product": row[0],
                            "Remaining Quantity": row[1]
                        }
                        for row in low_stock
                    ]
                )

            else:
                st.success(
                    "No low-stock products!"
                )

        except Exception as e:
            st.error(
                f"Error retrieving low-stock products: {e}"
            )

    # -----------------------------------------------------
    # Customer purchase history
    # -----------------------------------------------------
    elif analytics_action == "Customer Purchase History":

        st.subheader("Customer Purchase History")

        try:
            customers = customer.get_all_customers()

            if not customers:

                st.info(
                    "No customers available."
                )

            else:

                customer_options = {
                    f"{row[1]} (ID: {row[0]})": row[0]
                    for row in customers
                }

                selected = st.selectbox(
                    "Select Customer",
                    list(customer_options.keys()),
                    key="analytics_customer"
                )

                customer_id = customer_options[selected]

                cur = conn.cursor()

                cur.execute(
                    """
                    SELECT
                        id,
                        sale_date,
                        total_amount
                    FROM sales
                    WHERE customer_id = %s
                    ORDER BY sale_date DESC
                    """,
                    (customer_id,)
                )

                customer_sales = cur.fetchall()

                cur.close()

                if customer_sales:

                    st.table(
                        [
                            {
                                "Sale ID": row[0],
                                "Date": str(row[1]),
                                "Amount": float(row[2])
                            }
                            for row in customer_sales
                        ]
                    )

                    total_purchases = sum(
                        float(row[2])
                        for row in customer_sales
                    )

                    st.metric(
                        "Total Purchases",
                        f"₹{total_purchases:.2f}"
                    )

                else:

                    st.info(
                        "This customer has no purchase history."
                    )

        except Exception as e:
            st.error(
                f"Error retrieving customer purchase history: {e}"
            )
