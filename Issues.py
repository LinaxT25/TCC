import itertools
import psycopg2


def issues(connection, userid):
    try:
        cursor = connection.cursor()

        # Assignees
        print("Searching for assignees in issues database...")
        query = 'SELECT assignees FROM "dv8fromtheworld/jda".issues'
        cursor.execute(query)
        data = cursor.fetchall()  # returns a list of tuples
        users = list(filter(lambda x: x[0] is not None, data))

        # Don't have data to return only true or false
        if users.__str__().__contains__(userid):
            print("User is a assignee!\n")
            assignee_tuple = tuple(("AssigneeIssues", True))
        else:
            print("User is not a assignee!\n")
            assignee_tuple = tuple(("AssigneeIssues", False))

        # Author
        print("Searching for author of issue...")
        query = 'SELECT created_at FROM "dv8fromtheworld/jda".issues WHERE "author" = %s;'
        cursor.execute(query, (userid,))
        data = cursor.fetchall()  # returns a list of tuples

        # Catch the creation data of the issue(published_at and created_at have same data)
        if len(data) != 0:
            print("User is author of issue!\n")
            extracted_data = []
            for tuples in data:
                extracted_data.append(tuples[0])
            author_tuple = tuple(("AuthorIssue", tuple(extracted_data)))
        else:
            print("User is not author of issue!\n")
            author_tuple = tuple(("AuthorIssue", None))

        # Editor
        print("Searching for editor of issue...")
        query = 'SELECT last_edited_at FROM "dv8fromtheworld/jda".issues WHERE "editor" = %s;'
        cursor.execute(query, (userid,))
        data = cursor.fetchall()  # returns a list of tuples

        # Catch the data with last edit of issue
        if len(data) != 0:
            print("User is editor of issue!\n")
            extracted_data = []
            for tuples in data:
                extracted_data.append(tuples[0])
            editor_tuple = tuple(("EditorIssue", tuple(extracted_data)))
        else:
            print("User is not editor of issue!\n")
            editor_tuple = tuple(("EditorIssue", None))

        # Participants
        print("Searching for participants in issues database...")
        query = 'SELECT participants FROM "dv8fromtheworld/jda".issues'
        cursor.execute(query)
        data = cursor.fetchall()  # returns a list of tuples

        # Don't have any data to catch
        if data.__str__().__contains__(userid):
            print("User is participant of this issue!\n")
            participant_tuple = tuple(("ParticipantIssue", True))
        else:
            print("User is not a participant of this issue!\n")
            participant_tuple = tuple(("ParticipantIssue", False))

        final_tuple = tuple(itertools.chain(assignee_tuple, author_tuple, editor_tuple, participant_tuple))
        cursor.close()
        return final_tuple
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
