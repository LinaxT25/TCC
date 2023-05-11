import itertools
import psycopg2
def issues(connection, userid):
    try:
        cursor = connection.cursor()

        # Assignees
        print("Searching for assignees in issues database...")
        query = 'SELECT assignees FROM "dv8fromtheworld/jda".issues'
        cursor.execute(query)
        data = cursor.fetchall() #returns a list of tuples
        users = list(filter(lambda x: x[0] is not None, data))

        # Don't have data to return only true or false
        if users.__str__().__contains__(userid):
            print("User is a assignee!\n")
            assigneeTuple = tuple(("AssigneeIssues", True))
        else:
            print("User is not a assignee!\n")
            assigneeTuple = tuple(("AssigneeIssues", False))

        # Author
        print("Searching for author of issue...")
        query = 'SELECT created_at FROM "dv8fromtheworld/jda".issues WHERE "author" = %s;'
        cursor.execute(query, (userid,))
        data = cursor.fetchall() #returns a list of tuples

        # Catch the creation data of the issue(published_at and created_at have same data)
        if len(data) != 0:
            print("User is author of issue!\n")
            extractedData = []
            for tuples in data:
                extractedData.append(tuples[0])
            authorTuple = tuple(("AuthorIssue", tuple(extractedData)))
        else:
            print("User is not author of issue!\n")
            authorTuple = tuple(("AuthorIssue", None))

        # Editor
        print("Searching for editor of issue...")
        query = 'SELECT last_edited_at FROM "dv8fromtheworld/jda".issues WHERE "editor" = %s;'
        cursor.execute(query, (userid,))
        data = cursor.fetchall() #returns a list of tuples

        # Catch the data with last edit of issue
        if len(data) != 0:
            print("User is editor of issue!\n")
            extractedData = []
            for tuples in data:
                extractedData.append(tuples[0])
            editorTuple = tuple(("EditorIssue", tuple(extractedData)))
        else:
            print("User is not editor of issue!\n")
            editorTuple = tuple(("EditorIssue", None))

        # Participants
        print("Searching for participants in issues database...")
        query = 'SELECT participants FROM "dv8fromtheworld/jda".issues'
        cursor.execute(query)
        data = cursor.fetchall() #returns a list of tuples

        # Don't have any data to catch
        if data.__str__().__contains__(userid):
            print("User is participant of this issue!\n")
            participantTuple = tuple(("ParticipantIssue", True))
        else:
            print("User is not a participant of this issue!\n")
            participantTuple = tuple(("ParticipantIssue", False))

        finalTuple = tuple(itertools.chain(assigneeTuple, authorTuple, editorTuple, participantTuple))
        cursor.close()
        return finalTuple
    except(Exception, psycopg2.DatabaseError) as error:
         print(error)
