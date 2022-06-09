import sqlite3
import pandas as pd

# connect to database
conn = sqlite3.connect('amztracker.db')
cur = conn.cursor()

df = pd.read_sql_query("""SELECT * FROM prices""", conn)

print(df.sort_values(by ='date'))