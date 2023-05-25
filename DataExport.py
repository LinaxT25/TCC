from datetime import date,datetime
import csv
import sys
import json
import os

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
    cursor = connect.cursor()

    cursor.execute('select exists(select * from "dv8fromtheworld/jda".tables where table_name=%s)', ('standard',))

    if cursor.fetchone()[0] is False:
        create = 'CREATE TABLE "dv8fromtheworld/jda".standard (user_id text,activity text,activity_date date);'
        cursor.execute(create)

