import psycopg2

def watching(connection, user):
    try:
        cursor = connection.cursor()
        print("Searching if user is watching a repository...")

        cursor.execute('SELECT * FROM "dv8fromtheworld/jda".watchers WHERE "user" = %s;', (user,))

        data = cursor.fetchall()

        if len(data) != 0:
            print("User is watching the repository.\n")
            cursor.close()
            return True
        else:
            print("User is not watching the repository.\n")
            cursor.close()
            return False
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
