from cgitb import html
from sqlite3 import Cursor
import requests
from bs4 import BeautifulSoup as Soup
import pandas as pd
import smtplib
from email.message import EmailMessage
import pymysql

webpage_response = requests.get('http://www.herbsbar.com/live-music-calendar-1')

webpage = (webpage_response.content)
parser = Soup(webpage, 'html.parser')
herbs_dict = {"Name":[], "Date":[], "Time":[]}

for herbs_music in parser.find_all("article", {"class": "eventlist-event eventlist-event--upcoming eventlist-event--multiday"}):

    herbs_band_names = herbs_music.find_all('a', {'class':'eventlist-title-link'})
    herbs_band_names_text = herbs_band_names[0].text.strip()
    herbs_dict['Name'].append(herbs_band_names_text)

    herbs_dates = herbs_music.find_all('time', {'class':'event-date'})
    herbs_dates_text = herbs_dates[0].text.strip()
    herbs_dict['Date'].append(herbs_dates_text)

    herbs_times = herbs_music.find_all('time', {'class':'event-time-12hr'})
    herbs_times_text = herbs_times[0].text.strip()
    herbs_dict['Time'].append(herbs_times_text)

endpoint = 'mysql-bandscrape.cpzuexvbklch.us-east-1.rds.amazonaws.com'
username = 'admin'
password = 'nayrryan123'
database_name = 'test'
connection = pymysql.connect(host=endpoint, user=username, password=password, database=database_name)
cursor = connection.cursor()
insertquery = """INSERT INTO BandInfo(Artist, Date, Time) VALUES (%s, %s, %s)"""
records_to_insert = ([(name, date, time) for name, date, time in zip(herbs_dict['Name'], herbs_dict['Date'], herbs_dict['Time'])])
cursor.executemany(insertquery, records_to_insert)
connection.commit()




# cursor.execute("""INSERT INTO BandInfo(Artist, Date, Time)
#     VALUES (%s, %s, %s)""", (herbs_band_names_text, herbs_times_text, herbs_dates_text))



# for names in herbs_dict['Name']:
#     print (names)

# print herbs_dict['Time']

cursor.execute('select * from BandInfo')
output = cursor.fetchall()
for i in output:
    print(i)
    


# df = pd.DataFrame(herbs_dict)
# dfhtml = ("<html><body>" + df.to_html() + "</body></html>")

# msg = EmailMessage()
# msg['Subject'] = 'Band Scrape'
# msg['From'] = "ryanf.test.email@gmail.com"
# msg['To'] = "ryanfadden@gmail.com"
# msg.set_content(df.to_string())
# msg.add_alternative(dfhtml, subtype='html')

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

#     smtp.login('ryanf.test.email@gmail.com', 'nheppwbkqnrjakuf')
#     smtp.send_message(msg)