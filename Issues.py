import psycopg2

def issues(connection, id):
    try:
        issuesList = list()
        cursor = connection.cursor()
        print("Searching for assignees in issues database...")

        query = 'SELECT assignees FROM "dv8fromtheworld/jda".issues'
        cursor.execute(query, (id,))
        data = cursor.fetchall()

        #Filter the Nones from the list of tuples
        users = list(filter(lambda x: x[0] is not None, data))

        if users.__str__().__contains__(id):
            print("User is a assignee!\n")
            issuesList.append(True)
        else:
            print("User is not a assignee!\n")
            issuesList.append(False)

        print("Searching for author of issue...")
        query = 'SELECT * FROM "dv8fromtheworld/jda".issues WHERE "author" = %s;'
        cursor.execute(query, (id,))
        data = cursor.fetchall()

        if len(data) != 0:
            print("User is author of issue!\n")
            issuesList.append(True)
        else:
            print("User is not author of issue!\n")
            issuesList.append(False)

        print("Searching for editor of issue...")
        query = 'SELECT * FROM "dv8fromtheworld/jda".issues WHERE "editor" = %s;'
        cursor.execute(query, (id,))
        data = cursor.fetchall()

        if len(data) != 0:
            print("User is editor of issue!\n")
            issuesList.append(True)
        else:
            print("User is not editor of issue!\n")
            issuesList.append(False)

        print("Searching for participants in issues database...")

        query = 'SELECT participants FROM "dv8fromtheworld/jda".issues'
        cursor.execute(query, (id,))
        data = cursor.fetchall()

        if data.__str__().__contains__(id):
            print("User is participant of this issue!\n")
            issuesList.append(True)
        else:
            print("User is not a participant of this issue!\n")
            issuesList.append(False)

        cursor.close()
        return issuesList
    except(Exception, psycopg2.DatabaseError) as error:
         print(error)
