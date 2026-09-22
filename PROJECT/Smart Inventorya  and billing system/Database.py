import psycopg2
def connection ():
    con = psycopg2.connect( 
        host ="localhost", 
        database= "ecommerce",
        user ="postgres",
        password="12345",
        port="5432",
    )
    if con:
        print(">>>>>>> Connection Established!")
    else :
        print(">>>>>>> Connection failed!")
    return con

conn = connection()