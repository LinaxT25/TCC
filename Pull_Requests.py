import psycopg2

def pullRequests(connection, id):
    try:
        pullRequestsList = list()
        cursor = connection.cursor()
        print("Searching for assignees in pull_requests database...")

        query = 'SELECT assignees FROM "dv8fromtheworld/jda".pull_requests'
        cursor.execute(query, (id,))
        data = cursor.fetchall()

        #Filter the Nones from the list of tuples
        users = list(filter(lambda x: x[0] is not None, data))

        if users.__str__().__contains__(id):
            print("User is a assignee!\n")
            pullRequestsList.append(True)
        else:
            print("User is not a assignee!\n")
            pullRequestsList.append(False)

        print("Searching for author of pull request...")
        query = 'SELECT * FROM "dv8fromtheworld/jda".pull_requests WHERE "author" = %s;'
        cursor.execute(query, (id,))
        data = cursor.fetchall()

        if len(data) != 0:
            print("User is author of pull request!\n")
            pullRequestsList.append(True)
        else:
            print("User is not author of pull request!\n")
            pullRequestsList.append(False)

        print("Searching for editor of pull request...")
        query = 'SELECT * FROM "dv8fromtheworld/jda".pull_requests WHERE "editor" = %s;'
        cursor.execute(query, (id,))
        data = cursor.fetchall()

        if len(data) != 0:
            print("User is editor of pull request!\n")
            pullRequestsList.append(True)
        else:
            print("User is not editor of pull request!\n")
            pullRequestsList.append(False)

        print("Searching for participants in pull_requests database...")

        query = 'SELECT participants FROM "dv8fromtheworld/jda".pull_requests'
        cursor.execute(query, (id,))
        data = cursor.fetchall()

        if data.__str__().__contains__(id):
            print("User is participant of this pull request!\n")
            pullRequestsList.append(True)
        else:
            print("User is not a participant of this pull request!\n")
            pullRequestsList.append(False)

        print("Searching for author of merge in pull_requests database...")

        query = 'SELECT * FROM "dv8fromtheworld/jda".pull_requests WHERE "merged_by" = %s;'
        cursor.execute(query, (id,))
        data = cursor.fetchall()

        if len(data) != 0:
            print("User is author of merge!\n")
            pullRequestsList.append(True)
        else:
            print("User is not author of merge!\n")
            pullRequestsList.append(False)

        print("Searching for suggested reviewers in pull_requests database...")

        query = 'SELECT suggested_reviewers FROM "dv8fromtheworld/jda".pull_requests'
        cursor.execute(query, (id,))
        data = cursor.fetchall()

        # Filter the Nones from the list of tuples
        users = list(filter(lambda x: x[0] is not None, data))

        if users.__str__().__contains__(id):
            print("User is a suggested reviewer!\n")
            pullRequestsList.append(True)
        else:
            print("User is not a suggested reviewer!\n")
            pullRequestsList.append(False)

        cursor.close()
        return pullRequestsList
    except(Exception, psycopg2.DatabaseError) as error:
         print(error)
