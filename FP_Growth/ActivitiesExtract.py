import psycopg2

from DB import Connect
from Export import FileWrite


def data_pattern():
    try:
        connection = Connect.connect()
        cursor = connection.cursor()

        # Get all users from database for extract the activities
        query = 'SELECT distinct user_id from "dv8fromtheworld/jda".standard'
        cursor.execute(query)
        users = cursor.fetchall()

        # Get all activities from a user and make a list
        activity_list = []  # Global list to store all activities made by users
        for userid in users:
            query = 'SELECT activity from "dv8fromtheworld/jda".standard WHERE "user_id" = %s;'
            cursor.execute(query, (userid,))
            activity = cursor.fetchall()

            user_activity = []  # Local list to store only one user activities
            for i in range(len(activity)):
                # Check for duplicates to not overflow the algorithm
                if not user_activity.__contains__(activity[i][0]):
                    user_activity.append(activity[i][0])
            activity_list.append(user_activity)  # Append to global list

        # Returns the sum of activities extracted for analysis in FPGrowth
        taggers_sum = sum(activities.count("Taggers") for activities in activity_list)
        merged_sum = sum(activities.count("Merged") for activities in activity_list)
        editorissue_sum = sum(activities.count("EditorIssue") for activities in activity_list)
        starred_sum = sum(activities.count("Starred") for activities in activity_list)
        editorpullrequest_sum = sum(activities.count("EditorPullRequest") for activities in activity_list)
        authorissue_sum = sum(activities.count("AuthorIssue") for activities in activity_list)
        releases_sum = sum(activities.count("Releases") for activities in activity_list)
        authorpullrequest_sum = sum(activities.count("AuthorPullRequest") for activities in activity_list)
        reactions_sum = sum(activities.count("Reactions") for activities in activity_list)

        total_sum = (taggers_sum +
                     merged_sum +
                     editorissue_sum +
                     starred_sum +
                     editorpullrequest_sum +
                     authorissue_sum +
                     releases_sum +
                     authorpullrequest_sum +
                     reactions_sum)

        # Write to a file a sum of all activities and the respective percentages
        FileWrite.write_percentage("Taggers", taggers_sum, total_sum)
        FileWrite.write_percentage("Merged", merged_sum, total_sum)
        FileWrite.write_percentage("EditorIssue", editorissue_sum, total_sum)
        FileWrite.write_percentage("Starred", starred_sum, total_sum)
        FileWrite.write_percentage("EditorPullRequest", editorpullrequest_sum, total_sum)
        FileWrite.write_percentage("AuthorIssue", authorissue_sum, total_sum)
        FileWrite.write_percentage("Releases", releases_sum, total_sum)
        FileWrite.write_percentage("AuthorPullRequest", authorpullrequest_sum, total_sum)
        FileWrite.write_percentage("Reactions", reactions_sum, total_sum)
        FileWrite.write_total_activities(total_sum)

        return activity_list
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
