import requests
from bs4 import BeautifulSoup
import re

url = 'https://datosmacro.expansion.com'
subdomain = '/energia/precios-gasolina-diesel-calefaccion'
r = requests.get(url + subdomain)

#print(r.url)

content = r.content

soup = BeautifulSoup(content, features= "html.parser")

table = soup.find('table', {'id': 'tb1_1314'})
#print(table)

# Columns of the table
tds = soup.findAll('td')
# Empty list to store the output
country_links = []

# For loop that iterates over all the <td>tags
for td in tds:

    # Looking for the anchor tag inside the <td>tag
    a = td.find('a')
    try:
        if 'href' in a.attrs:
            # storing the value of href in a separate variable
            href = a.get('href')
            # appending the url to the output list
            country_links.append(href)
    except:
        pass

#print(country_links)
 # For each country, extract the data

for country in country_links:
    html = requests.get(url + country)
    data = html.text
    bs = BeautifulSoup(data, 'html.parser')
    for tr in bs.findAll('tr'):
        stack =[]
        for td in tr.findAll('td'):
            stack.append(td)
print(stack)
