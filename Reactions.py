import psycopg2

def reactedUser(connection, user):
    try:
        cursor = connection.cursor()
        print("Searching if user reacted a repository...")

        cursor.execute('SELECT created_at FROM "dv8fromtheworld/jda".reactions WHERE "user" = %s;', (user,))

        data = cursor.fetchall()
        #print(data)

        if len(data) != 0:
            print("User reacted the repository.\n")
            cursor.close()
            return tuple(["Reactions", data])
        else:
            print("User not reacted the repository.\n")
            cursor.close()
            return None
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
