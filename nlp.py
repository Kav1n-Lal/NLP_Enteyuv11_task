import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
import re

title_list=[]
text_list=[]
df = pd.read_excel('C:/Users/DELL/Desktop/nlp_assignment/Input.xlsx')
#print(df.iloc[:,1][0])
source=requests.get(f'{df.iloc[:,1][0]}').text
soup=BeautifulSoup(source,'lxml')

article=soup.find('article')
#print(article.prettify())
title=article.find('h1',class_="tdb-title-text").text
title_list.append(title)


for para in article.find_all('div',class_="tdb-block-inner td-fix-index")[7:-4]:
    try:
        text_list.append(para.text)
    except AttributeError:
        pass

df_out=pd.DataFrame({'url_id':df.iloc[:,0][0],'link':df.iloc[:,1][0],"title":title_list[0],"article":text_list[0]},index=[0])
df_out.to_csv('scrape_1.csv')


