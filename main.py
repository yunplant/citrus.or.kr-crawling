import pandas as pd
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

data = {
        '날짜' : [1],
        '가격' : [1]
    }
df = pd.DataFrame(data)

for i in range(770):
    now = datetime(2020,1,1)
    after = now + timedelta(days=i)
    y = after.year
    m = after.month
    d = after.day


    
    webpage = requests.get("http://citrus.or.kr/price/sub11_01.php?year=%d&month=%d&day=%d&pcode=1" %(y,m,d))
    soup = BeautifulSoup(webpage.content, "html.parser")

    a = []
    for child in soup.find('table',{'class':'dtable'}).descendants :
        a.append(child.text)


    print(after,a[34])


    df.loc[len(df)] = [after,a[34]]

df.to_csv("C:/Users/YS/Desktop/data.csv")
