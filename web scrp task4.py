

import requests
import json
from bs4 import BeautifulSoup
rel=requests.get("https://www.imdb.com/title/tt0066763/")
soup=BeautifulSoup(rel.content,"html.parser")
con=soup.find('script',type='application/ld+json').text
a=json.loads(con)
dic={}
# print(a)
for i in a:
    dic['name']=a['name']
    dic['director']=[a['director'][0]['name']]
    dic['image']=a['image']
    dic['description']=a['description']
    dic["language"]=a['review']['inLanguage']
    dic['genre']=a['genre']
    dic['country']='india'
    # print(dic)
        

with open("4_task.json","w") as f:
    json.dump(dic,f,indent=8)