import psycopg2

#connecting to database to extract some data
def connect():
    try:
        print("Connecting to the PostgreSQL database...")
        connection = psycopg2.connect("dbname=TCC user=postgres password=postgres")

        cursor = connection.cursor()
        print("PostgreSQL database version:")
        cursor.execute("SELECT version()")

        db_version = cursor.fetchone()
        print(db_version, "\n")

        cursor.close()
        return connection
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)