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
        writer = csv.writer(file)
        try:
            writer.writerows(finaltuple)
        except csv.Error as e:
            sys.exit(e)

def exportToJson(finaltuple, userid):
    # Creating a new directory for data to be exported
    dirPath = os.getcwd()
    newDir = os.path.join(dirPath, "Data_Output") # Joined paths to be compatible with more OS

    if not os.path.exists(newDir):
        os.makedirs(newDir)

    filename = userid + ".json"
    with open(os.path.join(newDir,filename), 'w', encoding='utf-8') as file:
        try:
            # Default receive the function convertData to convert the datatime object in ISO
            json.dump(finaltuple, file, ensure_ascii=False, default=convertData, indent=4, sort_keys=True)
        except json.JSONDecodeError as e:
            sys.exit(e)

def convertData(tuples):
    if isinstance(tuples, (datetime, date)):
        return tuples.isoformat()