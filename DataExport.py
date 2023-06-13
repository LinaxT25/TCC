from datetime import date,datetime
import csv
import sys
import os

import psycopg2


def exportToCsv(finaltuple, userid):
    # Creating a new directory for data to be exported
    dirPath = os.getcwd()
    newDir = os.path.join(dirPath, "Data_Output") # Joined paths to be compatible with more OS

    if not os.path.exists(newDir):
        os.makedirs(newDir)

    filename = userid + ".csv"
    with open(os.path.join(newDir,filename), 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL, doublequote=True,)
        try:
            for i in range(len(finaltuple)):
                writer.writerow((i + 1, finaltuple[i][0], finaltuple[i][1]))
        except csv.Error as e:
            sys.exit(e)

def exportToDB(finaltuple, userid, connect):
    try:
        cursor = connect.cursor()

        cursor.execute('select exists(select * from information_schema.tables where table_name=%s)',
                       ('standard',))

        if cursor.fetchone()[0] is False:
            create = 'CREATE TABLE "dv8fromtheworld/jda".standard (user_id text,activity text,activity_date date);'
            cursor.execute(create)
            connect.commit()

        filteredtuple = list(filter(lambda x: x[1] is not None, finaltuple))

        # Remove the 6 values boolean with has been appended in the end of tuple
        for i in range(len(filteredtuple) - 6):
            insert = 'INSERT INTO "dv8fromtheworld/jda".standard VALUES(%s, %s, %s);'
            cursor.execute(insert, (userid, filteredtuple[i][0], filteredtuple[i][1]))

        connect.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)