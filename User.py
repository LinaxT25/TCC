import psycopg2

def retrieveActors(connection, id):
    try:
        cursor = connection.cursor()
        print("Searching for a user in database...")

        cursor.execute('SELECT * FROM "dv8fromtheworld/jda".actors WHERE "id" = %s;', (id,))

        data = cursor.fetchall()

        if len(data) != 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)