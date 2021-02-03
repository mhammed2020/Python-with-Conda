from bs4 import BeautifulSoup
import requests
import csv

with open ('index.html') as html_file :
    soup = BeautifulSoup(html_file,'lxml')

# article = soup.find('div',class_='article')


# for loop
for article in soup.find_all('div',class_='article') :

    line = article.h2.a.text
    print(line)

    summ = article.p.text
    print(summ)
    print("*"*20)