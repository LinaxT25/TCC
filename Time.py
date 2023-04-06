from datetime import datetime

def timeCheck(connection):
    dateString = '2000-01-01'
    date = datetime.strptime(dateString, '%Y-%m-%d')

    print(date)