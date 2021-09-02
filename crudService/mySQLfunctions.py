import mysql.connector
from mysql.connector import Error
from sqlalchemy.exc import SQLAlchemyError
import csv
from dbpass import db_password

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=db_password,
    database="securitiesmaster"

)

mycursor = db.cursor()


mycursor.execute("SELECT distinct ticker FROM securitiesmaster.ohlc;")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# mycursor.execute(
#     "CREATE TABLE spohlc (id INT AUTO_INCREMENT PRIMARY KEY, open VARCHAR(50), high VARCHAR(50), low VARCHAR(50), close VARCHAR(50), volume bigint, timestamp TIMESTAMP(6), ticker VARCHAR(10))"
#
# )

#ohlc_db_entry = "INSERT INTO ohlc (id, open, high, low, close, volume, datetime, ticker) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

#ohlc_data = ()