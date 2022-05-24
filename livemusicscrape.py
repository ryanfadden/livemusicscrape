from gettext import find
import requests
from bs4 import BeautifulSoup as Soup
import pandas as pd

webpage_response = requests.get('http://www.herbsbar.com/live-music-calendar-1')

webpage = (webpage_response.content)
parser = Soup(webpage, 'html.parser')

# for herbs_music in parser.find_all("article", {"class": "eventlist-event eventlist-event--upcoming eventlist-event--multiday"}):

#     herbs_band_names = herbs_music.find_all('a', {'class':'eventlist-title-link'})
#     herbs_band_names_text = herbs_band_names[0].text.strip()

#     herbs_dates = herbs_music.find_all('time', {'class':'event-date'})
#     herbs_dates_text = herbs_dates[0].text.strip()

#     herbs_times = herbs_music.find_all('time', {'class':'event-time-12hr'})
#     herbs_times_text = herbs_times[0].text.strip()

#     herbs_info = {'Band Name': [herbs_band_names_text], 'Date': [herbs_dates_text], 'Time': [herbs_times_text]}
#   

rows = []
for i in range(3):
    rows.append([i, i + 1])
print (rows)

df = pd.DataFrame(rows, columns=["a", "b"])
print (df)

    #
    # 
    #  df = pd.DataFrame(herbs_info, columns=('Band Name', 'Date', 'Time'))
    # print (df)



    # herbs_info = {'Band Name': [herbs_band_names_text], 'Date': [herbs_dates_text], 'Time': [herbs_times_text]}
    # df = pd.DataFrame(herbs_info, columns=('Band Name', 'Date', 'Time'))
    # print (df)

    # print (herbs_band_names_text)
    # print (herbs_dates_text)
    # print (herbs_times_text)

# carl = ('carl')

# data = {'Name': ['Ankit', herbs_band_names_text, 'Aishwarya', 'Priyanka'],
#                 'Age': [21, 19, 20, 18],
#                 'Stream': ['Math', 'Commerce', 'Arts', 'Biology'],
#                 'Percentage': [88, 92, 95, 70]}

# musicinfo = {'debbie kills dallas', '5/20', '5:30pm'}

# df = pd.DataFrame(data, columns=('Name', 'Age', 'Stream'))
# print (df)


# herbsinfo = parser.find_all("div", {"class": "eventlist eventlist--upcoming"})
# herbsinfotext = herbsinfo[0].text
# print (herbsinfotext)


# finding = soup.find('a')

# printing = parser.form.div.a
# print (printing)

#####Gives 5 of the same results 
# for gear in parser:
#     findingitall = parser.find_all("div", {"class": "name"})
#     print (findingitall[0].text)

#     price = parser.find_all("div", {"class": "price"})
#     print (price[0].text)

#####Shows the everyting in the "a" tags that contain the name class, but it isnt just text
# geartitles = parser.find_all("div", {"class": "name"})

#####This works! but there are 3 linebreaks between each gear name and I dont think
#####its possible to include the price into the loop 
# for gear in parser.find_all("div", {"class": "name"}):
#     print (gear.text)

# filename = "gear.csv"
# f = open(filename, "w")

# headers = "Gear, Price"
# f.write(headers)

#####Welp, this works, but there are too many line breaks
# for gear in parser.find_all("div", {"class": "details"}):
    
#     gearname = gear.find_all("div", {"class": "name"}, "a")
#     gearnametext = gearname[0].text.
    
#     gearprice = gear.find_all("div", {"class": "price"}, "a")
#     gearpricetext = gearprice[0].text

#     print (gearnametext)
#     print (gearpricetext)

#     f.write(gearnametext + "," + gearpricetext)

##### Working as intended!
# filename = "gear1.csv"
# headers = "Gear,Price\n"


# with open(filename, 'w') as f:
#     f.write(headers)
    
#     for gear in parser.find_all("div", {"class": "details"}):

#         gearname = gear.find_all("div", {"class": "name"})
#         gearnametext = gearname[0].text.strip()
        
#         gearprice = gear.find_all("div", {"class": "price"})
#         gearpricetext = gearprice[0].text.strip()

#         print (gearnametext)
#         print (gearpricetext)

#         f.write(gearnametext + "," + gearpricetext + "\n")


# print (findingitall)

#for gear in parser.find_all("body"):
#     print (gear.a.text)


# herbs_bandnames = parser.find_all('a', {'class':'eventlist-title-link'})


# for herbs_bandnames_text in herbs_bandnames:
#     print (herbs_bandnames_text)

# for scrape in parser:
#     herbsabandnames = parser.find_all('a', {'class':'eventlist-title-link'})
#     print (herbsabandnames.string)
#     dates = parser.find_all('time', {'class':'event-date'})
#     print (dates.string)
#     herbsdates = parser.find_all('time', {'class':'event-time-12hr'})
#     print (herbsdates.string)






# for herbs_music in parser:
#     band_names = herbs_music.find_all('a', {'class':'eventlist-title-link'})
#     print (band_names)
    # dates = herbs_music.find_all('time', {'class':'event-date'})
    # time = herbs_music.find_all('time', {'class':'event-time-12hr'})




# band_names = parser.find_all('a', {'class':'eventlist-title-link'})
# print (band_names)

# showbandname = parser.find_all('a', {'class':'eventlist-title-link'})

# for bandname in showbandname:
#     print ()
#     print (bandname)


# groupofwords = ["cat", "dog", "pig", "cow"]
# print (groupofwords)
# print (groupofwords[2])

# for word in groupofwords:
#     print (word)

# print (groupofwords)