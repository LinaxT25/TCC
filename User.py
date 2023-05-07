import psycopg2

def retrieveActor(connection, userid):
    try:
        cursor = connection.cursor()

        print("Searching for a user in database...")
        cursor.execute('SELECT * FROM "dv8fromtheworld/jda".actors WHERE "id" = %s;', (userid,))
        data = cursor.fetchall()

        if len(data) != 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


def retrieveActors(connection):
    try:
        cursor = connection.cursor()

        print("Searching for all users in database...")
        cursor.execute('SELECT id FROM "dv8fromtheworld/jda".actors;')
        data = cursor.fetchall()

        if len(data) != 0:
            cursor.close()
            return data
        else:
            cursor.close()
            return False
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)