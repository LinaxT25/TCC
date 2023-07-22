import psycopg2
import itertools


def pull_requests(connection, userid):
    try:
        cursor = connection.cursor()

        # Assignees
        print("Searching for assignees in pull_requests database...")
        query = 'SELECT assignees FROM "dv8fromtheworld/jda".pull_requests'
        cursor.execute(query)
        data = cursor.fetchall()  # returns a list of tuples
        users = list(filter(lambda x: x[0] is not None, data))

        # Don't have data to return only true or false
        if users.__str__().__contains__(userid):
            print("User is a assignee!\n")
            assignee_tuple = tuple(("AssigneePullRequest", True))
        else:
            print("User is not a assignee!\n")
            assignee_tuple = tuple(("AssigneePullRequest", False))

        # Author
        print("Searching for author of pull request...")
        query = 'SELECT created_at FROM "dv8fromtheworld/jda".pull_requests WHERE "author" = %s;'
        cursor.execute(query, (userid,))
        data = cursor.fetchall()  # returns a list of tuples

        # Catch the creation data of the pull request(published_at and created_at have same data)
        if len(data) != 0:
            print("User is author of pull request!\n")
            extracted_data = []
            for tuples in data:
                extracted_data.append(tuples[0])
            author_tuple = tuple(("AuthorPullRequest", tuple(extracted_data)))
        else:
            print("User is not author of pull request!\n")
            author_tuple = tuple(("AuthorPullRequest", None))

        # Editor
        print("Searching for editor of pull request...")
        query = 'SELECT last_edited_at FROM "dv8fromtheworld/jda".pull_requests WHERE "editor" = %s;'
        cursor.execute(query, (userid,))
        data = cursor.fetchall()  # returns a list of tuples

        # Catch the data with last edit of pull request
        if len(data) != 0:
            print("User is editor of pull request!\n")
            extracted_data = []
            for tuples in data:
                extracted_data.append(tuples[0])
            editor_tuple = tuple(("EditorPullRequest", tuple(extracted_data)))
        else:
            print("User is not editor of pull request!\n")
            editor_tuple = tuple(("EditorPullRequest", None))

        # Participants
        print("Searching for participants in pull_requests database...")
        query = 'SELECT participants FROM "dv8fromtheworld/jda".pull_requests'
        cursor.execute(query)
        data = cursor.fetchall()  # returns a list of tuples

        # Don't have any data to catch
        if data.__str__().__contains__(userid):
            print("User is participant of this pull request!\n")
            participant_tuple = tuple(("ParticipantPullRequest", True))
        else:
            print("User is not a participant of this pull request!\n")
            participant_tuple = tuple(("ParticipantPullRequest", False))

        # Author of merge
        print("Searching for author of merge in pull_requests database...")
        query = 'SELECT merged_at FROM "dv8fromtheworld/jda".pull_requests WHERE "merged_by" = %s;'
        cursor.execute(query, (userid,))
        data = cursor.fetchall()  # returns a list of tuples

        # Catch the data of merge
        if len(data) != 0:
            print("User is author of merge!\n")
            extracted_data = []
            for tuples in data:
                extracted_data.append(tuples[0])
            merged_tuple = tuple(("Merged", tuple(extracted_data)))
        else:
            print("User is not author of merge!\n")
            merged_tuple = tuple(("Merged", None))

        # Suggested Reviewers
        print("Searching for suggested reviewers in pull_requests database...")
        query = 'SELECT suggested_reviewers FROM "dv8fromtheworld/jda".pull_requests'
        cursor.execute(query)
        data = cursor.fetchall()  # returns a list of tuples
        users = list(filter(lambda x: x[0] is not None, data))

        # Don't have any data to catch
        if users.__str__().__contains__(userid):
            print("User is a suggested reviewer!\n")
            suggested_reviewer_tuple = tuple(("SuggestedReviewer", True))
        else:
            print("User is not a suggested reviewer!\n")
            suggested_reviewer_tuple = tuple(("SuggestedReviewer", False))

        final_tuple = tuple(itertools.chain(
            assignee_tuple, author_tuple, editor_tuple, participant_tuple, merged_tuple, suggested_reviewer_tuple))
        cursor.close()
        return final_tuple
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
