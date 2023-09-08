import os

import psycopg2

from DB import Connect


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

        # Returns all activities extracted and the respective percent in total to analysis in FPGrowth
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

        # Creating a new directory for data to be exported
        dir_path = os.getcwd()
        new_dir = os.path.join(dir_path, "Pattern_Output")  # Joined paths to be compatible with more OS

        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        # Writing to a file patterns output
        f = open("./Pattern_Output/activities_percentage.txt", "wt")

        f.write("Taggers: " + str(taggers_sum) + "\n")
        f.write("Percentage: " + str(taggers_sum / total_sum) + "\n\n")

        f.write("Merged: " + str(merged_sum) + "\n")
        f.write("Percentage: " + str(merged_sum / total_sum) + "\n\n")

        f.write("EditorIssue: " + str(editorissue_sum) + "\n")
        f.write("Percentage: " + str(editorissue_sum / total_sum) + "\n\n")

        f.write("EditorPullRequest: " + str(editorpullrequest_sum) + "\n")
        f.write("Percentage: " + str(editorpullrequest_sum / total_sum) + "\n\n")

        f.write("AuthorIssue: " + str(authorissue_sum) + "\n")
        f.write("Percentage: " + str(authorissue_sum / total_sum) + "\n\n")

        f.write("Releases: " + str(releases_sum) + "\n")
        f.write("Percentage: " + str(releases_sum / total_sum) + "\n\n")

        f.write("AuthorPullRequest: " + str(authorpullrequest_sum) + "\n")
        f.write("Percentage: " + str(authorpullrequest_sum / total_sum) + "\n\n")

        f.write("Reactions: " + str(reactions_sum) + "\n")
        f.write("Percentage: " + str(reactions_sum / total_sum) + "\n\n")

        f.write("Total Activities: " + str(total_sum) + "\n\n")
        f.close()

        return activity_list
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
