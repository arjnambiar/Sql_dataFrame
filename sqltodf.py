import MySQLdb
import pandas as pd
import numpy as np


fd_returns = open('C:\\Users\\usr\\Desktop\\customers.sql', 'r')


def sqlDataframe(file_obj):
    sqlFile_returns = file_obj.read()
    file_obj.close()
    sqlCommands = sqlFile_returns.split(';')
    for command in sqlCommands:
        try:
            cursor.execute(command)
        except OperationalError, msg:
            print "Command skipped: ", msg
    data = cursor.fetchall()
    data = pd.DataFrame(list(data))
    return data
    
 transactions = sqlDataframe(fd_returns)
 print transactions
