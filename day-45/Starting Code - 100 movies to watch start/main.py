import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")
titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]

titles.reverse()

with open("movies.txt", "w") as file:
    for title in titles:
        file.write(f"{title}\n")
