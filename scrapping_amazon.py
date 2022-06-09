from requests_html import HTMLSession
import csv
import datetime
import sqlite3

# connect to database
conn = sqlite3.connect('amztracker.db')
cur = conn.cursor()
# cur.execute("""
#     CREATE TABLE prices(
#     date DATE, asin TEXT,
#     price FLOAT,
#     title TEXT)""")

# Start session
s = HTMLSession()
asins = []

# Read CSV to list
with open('asins.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        # print(row)
        asins.append(row[0])


# Scrape Data
# url = "https://www.amazon.com/Cyber-Acoustics-Headphones-Cancelling-Microphone/dp/B074JLB1XP"
for asin in asins:
    r = s.get(f"https://www.amazon.com//dp/{asin}")
    r.html.render(sleep=40)

    price = r.html.find(".a-offscreen")[0].text.replace("$","").strip()
    print(price)

    title = r.html.find("#productTitle")[0].text.strip()
    print(title)
    # print(title, price)
    asin = asin
    date = datetime.datetime.today()
    # print(asin, price, date)
    cur.execute("""INSERT INTO prices VALUES(?,?,?,?)""",(date, asin, price, title))
    print(f'added data for{asin}, {price} ')

conn.commit()
print("commited new Entries to database")



