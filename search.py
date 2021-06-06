from google_play_scraper import app
import play_scraper
import pandas as pd

results=[]
app_ids=[]
titles=[]
icons=[]
urls=[]
scores=[]
details=[]
installs=[]
ratings=[]
genres=[]
des=[]
reviews=[]
containAds=[]

def Search(query):

    #similar apps from first page of gplay store 
    results.append(play_scraper.search(query,page=1))

    
    for result in results[0]:
        app_ids.append(result['app_id'])
        titles.append(result['title'])
        icons.append(result['icon'])
        urls.append(result['url'])
        scores.append(result['score'])


    #get more details
    for id in app_ids:
        details.append(app(id, lang='en', country='us'))

    
    for detail in details:
        installs.append(detail['minInstalls'])
        ratings.append(detail['ratings'])
        genres.append(detail['genre'])
        des.append(detail['descriptionHTML'])
        reviews.append(detail['reviews'])
        containAds.append(detail['containsAds'])

    #make a dataframe
    data=pd.DataFrame()
    data['id']=app_ids
    data['title']=titles
    data['icon']=icons
    data['url']=urls
    data['score']=scores
    data['no_of_install']=installs
    data['rating']=ratings
    data['genre']=genres
    data['description']=des
    data['review']=reviews
    data['containAd']=containAds

    #display it as html table
    data=data.to_html()
    return data

