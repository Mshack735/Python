from bs4 import BeautifulSoup
import requests 
url = 'http://www.fox23.com/weather'
r = requests.get(url)
r_hdml = r.text
#class_="temp-high"
soup = BeautifulSoup(r_hdml,"lxml")

# this will fetch all of the links on a webpage
for story in soup.find_all(class_='forecast'):
    print(story.text.replace("\n", " ").strip())
