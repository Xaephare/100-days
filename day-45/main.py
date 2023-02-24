from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag(name="a")[0].getText()
    article_texts.append(text)
    link = article_tag(name="a")[0].get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]

largest_upvote = article_upvotes.index(max(article_upvotes))

print(article_texts[largest_upvote])
print(article_links[largest_upvote])
print(article_upvotes[largest_upvote])


# # import lxml

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print (soup.p)

# all_anchor_tags = soup.find_all(name="a")

# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading.get_text())

# h3_heading = soup.find(name="h3", class_="heading")
# print(h3_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))

# headings = soup.select(selector=".heading")
# print(headings)