import os

import psycopg2
import pyfpgrowth

from BD import Connect


def data_pattern():
    try:
        connection = Connect.connect()
        cursor = connection.cursor()

        # Get all users from database for extract the activities
        query = 'SELECT user_id from "dv8fromtheworld/jda".standard'
        cursor.execute(query)
        users = cursor.fetchall()

        # Get all activities from a user and make a list
        activity_list = []  # Global list to store a list of activities
        for userid in users:
            query = 'SELECT activity from "dv8fromtheworld/jda".standard WHERE "user_id" = %s;'
            cursor.execute(query, (userid,))
            activity = cursor.fetchall()

            user_activity = []  # Local list to store only one user activities
            for i in range(len(activity)):
                # Check for duplicates to not overflow the algorithm
                if user_activity.__contains__(activity[i][0]):
                    continue
                else:
                    user_activity.append(activity[i][0])
            activity_list.append(user_activity)  # Append to global list

        patterns = pyfpgrowth.find_frequent_patterns(activity_list, 1)
        print(patterns)
        rules = pyfpgrowth.generate_association_rules(patterns, 0.7)
        print(rules)

        # Creating a new directory for data to be exported
        dir_path = os.getcwd()
        new_dir = os.path.join(dir_path, "Pattern_Output")  # Joined paths to be compatible with more OS

        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        # Writing to a file patterns output
        f = open("./Pattern_Output/pattern_output.txt", "wt")
        for items in patterns.items():
            f.write(items.__str__() + "\n")
        f.close()

        # Write to a file patterns that are associated with another
        f = open("./Pattern_Output/rules_output.txt", "wt")
        for items in rules.items():
            f.write(items.__str__() + "\n")
        f.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
