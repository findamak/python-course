import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
# We will scrape the above website and create a text file with a list of the movies

response = requests.get(URL)
content = response.text
movies = []
soup = BeautifulSoup(content, "html.parser")
tags = soup.find_all("h3", class_="title")

for tag in tags:
    movies.append(tag.getText())

movies.reverse()
# another way to reverse a list
# movies_reversed = movies[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for n in movies:
        file.write(f"{n}\n")
