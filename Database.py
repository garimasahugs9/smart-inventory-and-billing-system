import psycopg2


def connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="ecommerce",
            user="postgres",
            password="12345",
            port="5432"
        )

        print(">>>>>>> Connection Established!")
        return conn

    except psycopg2.Error as e:
        print(">>>>>>> Database connection failed!")
        print("Error:", e)
        return None


conn = connection()