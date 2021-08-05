import mysql.connector
from mysql.connector import Error
from sqlalchemy.exc import SQLAlchemyError
import csv
from dataFetcherService.annualIncomeStatementBuilder import *

connection_params_dic = {
    "host": "localhost",
    "user": "root",
    "passwd": "0595",
    "database": "stockanalyzerproject",

}


# Defining the connect function to establish connection to the server
def connect(connection_params_dic):
    conn = None
    try:
        print('Connecting to the MySQL.......')
        conn = mysql.connect(**connection_params_dic)
        print("Connection Successfully........")
    except Error as err:
        print("Error while connecting to MySQL", err)
        # set the connection to 'None' in case of error
        conn = None
    return conn

# Change to alchemy method?


# Using CSV
# datafrm = y5df
#
# def using_csv_reader(engine, datafrm, table_name):
#     try:
#         datafrm.to_csv('annualIncomeStatement.csv', index= False)
#         cols = ','.join(list(datafrm.columns))
#         sql = "INSERT INTO %s(%s) VALUES(%%s, %%s, %%s, %%s)" % (table_name, cols)
#         sql = sql.format(table_name)
#         with open('tempname.csv') as fh:
#             #sub_sample = [next(fh) for x in range(records)]
#             reader = csv.reader(fh)
#             next(reader) #skips the first line (headers)
#             data = list(reader)
#         engine.execute(sql, data)
#         print("Data inserted using Using_csv_reader() Sucessfully...")
#     except Error as err:
#         print("Error while inserting to MySQL", err)



