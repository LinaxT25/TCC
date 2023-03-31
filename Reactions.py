import psycopg2

def reactedUser(connection, user):
    try:
        cursor = connection.cursor()
        print("Searching if user reacted a repository...")

        cursor.execute('SELECT * FROM "dv8fromtheworld/jda".reactions WHERE "user" = %s;', (user,))

        data = cursor.fetchall()

        if len(data) != 0:
            print("User reacted the repository.\n")
            cursor.close()
            return True
        else:
            print("User not reacted the repository.\n")
            cursor.close()
            return False
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
