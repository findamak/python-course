from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
content = response.text

soup = BeautifulSoup(content, "html.parser")
article_texts = []
article_links = []

articles = soup.find_all("span", class_="titleline")
for tag in articles:
    article_texts.append(tag.a.getText())
    article_links.append(tag.a.get("href"))

scores = soup.find_all("span", class_="score")
# Using list comprehension, we create a new list of just the score by splitting each score as such
# i.e "48 points" -> [48,points]. Then we get just the index 0 and convert it to an integer.
article_scores = [int(score.getText().split()[0]) for score in scores]

print(article_texts)
print(article_links)
print(article_scores)

# Print article with most votes
largest_num = max(article_scores)
index = article_scores.index(largest_num)
print(article_texts[index])
print(article_links[index])
print(article_scores[index])

