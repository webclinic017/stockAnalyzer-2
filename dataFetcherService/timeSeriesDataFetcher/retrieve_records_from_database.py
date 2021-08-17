import finnhub
from finnhubAPIkey import FINNHUB_API_KEY
import mysql
import mysql.connector



# Connect to mySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="0595",
    database="securitiesmaster"
)
mycursor = db.cursor()


query = "SELECT distinct ticker FROM securitiesmaster.ohlc"
mycursor.execute(query)
records = mycursor.fetchall()
records_organizes = records.drop_duplicates()
print(records_organizes)

for i in records:
    print(records)