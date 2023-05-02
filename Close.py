import psycopg2
def closeConnection(connection):
    try:
        print("Trying to close the connection to database...")
        connection.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print("Connection closed.")
