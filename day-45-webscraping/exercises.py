from bs4 import BeautifulSoup

# Documentation:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# needed the encoding set to utf-8 to prevent error. "UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in
# position 281: character maps to <undefined>"
with open("website.html", "r", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# print the element name
print(soup.title.name)

# print the string in the element
print(soup.title.string)

# print all anchor tags
print(soup.findAll(name="a"))

# print just the links in the anchor tags
for tag in soup.findAll(name="a"):
    print(tag.get("href"))

# find a h1 element with a specific attribute
heading = soup.find(name="h1", id="name")
print(heading)

# find a h3 element that has a specific attribute named class. Because class is reserved for declaring a python class
# the attribute is called "class_"
heading1 = soup.find(name="h3", class_="heading")
print(heading1)

# select the first a tag that sits with a p tag
company_url = soup.select_one(selector="p a")
print(company_url)

# select the first element with an id of "name"
name = soup.select_one(selector="#name")
print(name)

# select all elements that have a class of "heading"
heading2 = soup.select(selector=".heading")
print(heading2)

