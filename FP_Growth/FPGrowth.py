import psycopg2
import pyfpgrowth

from BD import Connect


def data_pattern():
    try:
        connection = Connect.connect()
        cursor = connection.cursor()

        # Activity
        query = 'SELECT activity, activity_date from "dv8fromtheworld/jda".standard'
        cursor.execute(query)
        data = cursor.fetchall()

        # Converting date and output in list
        for i in range(len(data)):
            data[i] = list(data[i])
            data[i][1] = str(data[i][1])

        patterns_raw = pyfpgrowth.find_frequent_patterns(data, 1)
        # rules = pyfpgrowth.generate_association_rules(patterns, 2)
        patterns = dict()

        # Filtering keys < 2
        for x in patterns_raw.keys():
            if x.__len__().__eq__(2):
                patterns.update({x: patterns_raw.get(x)})

        patterns = sorted(patterns)
        print(patterns)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
