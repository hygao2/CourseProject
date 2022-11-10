import requests
from bs4 import BeautifulSoup
import pandas as pd

TitleName=[] 
Year=[] 
Rating=[]

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
r = requests.get(url).content
soup = BeautifulSoup(r, "html.parser") 
list = soup.find("tbody", {"class":"lister-list"}).find_all("tr")
x = 1
for i in list:
    title = i.find("td",{"class":"titleColumn"})
    year = i.find("span",{"class":"secondaryInfo"})
    rating = i.find("td",{"class":"ratingColumn"})

    title_text = title.text.strip()[5::]
    title_text = title_text.strip()
    title_text = title_text[:-6]
    title_text = title_text.strip()
    TitleName.append(title_text) 
    Year.append(year.text)
    Rating.append(rating.text)


df=pd.DataFrame({'Title' : TitleName,'year':Year,'Rating':Rating})
df.to_csv('IMDbRating.csv', index=False, encoding='utf-8')