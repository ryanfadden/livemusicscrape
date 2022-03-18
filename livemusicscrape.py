import requests
from bs4 import BeautifulSoup as Soup

webpage_response = requests.get('http://www.herbsbar.com/live-music-calendar-1')

webpage = (webpage_response.content)
parser = Soup(webpage, 'html.parser')


# for herbs_music in parser:
#     band_names = herbs_music.find_all('a', {'class':'eventlist-title-link'})
#     print (band_names)
    # dates = herbs_music.find_all('time', {'class':'event-date'})
    # time = herbs_music.find_all('time', {'class':'event-time-12hr'})

band_names = parser.find_all('a', {'class':'eventlist-title-link'})
print (band_names)

# showbandname = parser.find_all('a', {'class':'eventlist-title-link'})

# for bandname in showbandname:
#     print ()
#     print (bandname)


# groupofwords = ["cat", "dog", "pig", "cow"]
# # print (groupofwords)
# # print (groupofwords[2])

# # for word in groupofwords:
# #     print (word)

# print (groupofwords)