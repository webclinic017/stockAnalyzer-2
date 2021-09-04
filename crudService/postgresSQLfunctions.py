from dbpass import db_password
import psycopg2


db_name = 'securitiesmaster'
db_user = 'postgres'
db_pass = db_password
db_host = 'localhost'


conn = psycopg2.connect(dbname= db_name, user= db_user, password= db_pass, host= db_host )
mycursor = conn.cursor()


# Create the ohlc tables in your database
# mycursor.execute(
#     "CREATE TABLE ohlc (id serial PRIMARY KEY, open VARCHAR(50), high VARCHAR(50), low VARCHAR(50), close VARCHAR(50), volume bigint, timestamp TIMESTAMP(6), ticker VARCHAR(10))"
#
# )

#Create the ohlc tables in your database
mycursor.execute(
    "CREATE TABLE cryptoohlc (id serial PRIMARY KEY, open VARCHAR(50), high VARCHAR(50), low VARCHAR(50), close VARCHAR(50), volume bigint, timestamp TIMESTAMP(6), ticker VARCHAR(10))"

)

conn.commit()
mycursor.close()
conn.close()