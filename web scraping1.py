import requests 
from bs4 import BeautifulSoup
req = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
# print(req)
soup=BeautifulSoup(req.content,'html.parser')
# print(soup.prettify())
  
scraped_movies=soup.find_all('td', class_='titleColumn')
scraped_rantings=soup.find_all('td',class_='titleColumn')
# scraped_movies
# parse movie name
movies=[]
for movie in scraped_movies:
    movie=movie.get_text().replace("\n","")
    # movie=movie
    movies.append(movie)  
    #  print(movies)
  
# scraping rating for movies
scraped_ratings=soup.find_all('td',class_='ratingcolum imdbrating')
# scraped_ratings

# # parse ratings
ratings=[]
for rating in scraped_ratings:
    rating=rating.get_text().replace("\n",'')
    ratings.append(rating)
    # print(ratings)
i=0
while i<len(movies):
    print(movies[i])
    i=i+1
    
    
    
    




    
    
    



# prettyfile

# images
# img1=[]
# image =soup.findAll('div', class_="imageWrapper")
# print(image)
# for i in image:
#     j=i.image['src']
#     print(j)
#     img1.append[i]
# print(img1)

#links
# links=[]
# link=soup.findAll('div', class_="bike descwrapped")
# print(link)
# for i in link:
#     j=i.a['href']
#     links.append(j)
# print(links)

# # # #using csr we have to store the data

# with open ('il.json',"w") as f:
#     write =json.writer (f)
#     write.writerow(image)
#     for i in image:
#         j=i.image["src"]
#         img1.append(j)
#     write.writerow(img1)
    