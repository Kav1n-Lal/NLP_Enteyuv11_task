import pandas as pd
df1=pd.read_csv('scrape_1.csv',usecols=['url_id','link',"title","article"])
df2=pd.read_csv('scrape.csv',usecols=['url_id','link',"title","article"])

print(df2.head())