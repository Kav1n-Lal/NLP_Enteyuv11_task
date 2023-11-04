import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
import re

url_id=[]
link_list=[]
title_list=[]
text_list=[]
df = pd.read_excel('C:/Users/DELL/Desktop/nlp_assignment/Input.xlsx')
#print(df.iloc[:,1][0])
for j in range(1,len(df)):
    url_id.append(df.iloc[:,0][j])
    link_list.append(df.iloc[:,1][j])
    
    source=requests.get(f'{df.iloc[:,1][j]}').text
    soup=BeautifulSoup(source,'lxml')

    article=soup.find('article')
    #print(article.prettify())
    #print(j)
    try:
        title=article.find('h1',class_="entry-title").text
        title_list.append(title)
    except AttributeError:
        title_list.append('page_not_found')


    try:
        for para in article.find_all('div',class_="td-post-content tagdiv-type"):
            text_list.append(para.text)
    except AttributeError:
            text_list.append('page_not_found')
    df1=pd.read_csv('scrape.csv')
    df_out=pd.DataFrame({'url_id':df.iloc[:,0][j],'link':df.iloc[:,1][j],"title":title_list[-1],"article":text_list[-1]},index=[j])
    a=pd.concat([df1,df_out])
    a.to_csv('scrape.csv')


print(len(url_id))
print(len(link_list))
print(len(title_list))
print(len(text_list))

print(url_id)
print(link_list)
print(title_list)
print(text_list)


