import requests
import csv
from bs4 import BeautifulSoup


#Ana cecilia Lopez castillo
#1996528

url= "https://quotes.toscrape.com/"

response= requests.get(url)

html= BeautifulSoup(response.text, 'html.parser')

quotes_html= html.find_all('span', class_= "text")
authors_html= html.find_all('small', class_= "author")

quotes = list()

for quote in quotes_html:
	quotes.append(quote.text)

authors= list()

for author in authors_html:
	authors.append(author.text)


for t in zip(quotes, authors):
	print(t)


with open('./citas_1996528.csv', 'w') as csv_file:
	csv_writer= csv.writer(csv_file, dialect='excel')
	csv_writer.writerows(zip(quotes, authors))
