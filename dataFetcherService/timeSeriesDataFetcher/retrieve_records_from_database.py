import finnhub
from finnhubAPIkey import FINNHUB_API_KEY
import mysql
import mysql.connector
from dbpass import db_password
import psycopg2


# # Connect to mySQL Database
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd=db_password,
#     database="securitiesmaster"
# )

# Connect to Postgre Database
db_name = 'securitiesmaster'
db_user = 'postgres'
db_pass = db_password
db_host = 'localhost'


conn = psycopg2.connect(dbname= db_name, user= db_user, paddword= db_pass, host= db_host )
mycursor = conn.cursor()

query = "SELECT distinct ticker FROM securitiesmaster.ohlc"
mycursor.execute(query)
records = mycursor.fetchall()



for i in records:
    print(records)