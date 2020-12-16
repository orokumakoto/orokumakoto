#==========================氣象局===========================================
import requests 
import pandas as pd
import re
import numpy as np
from bs4 import BeautifulSoup
from datetime import datetime

url="https://www.cwb.gov.tw/Data/js/Observe/Observe_Home.js"
doc=requests.get(url)
data=doc.text
data=data.replace("'", "")
data=data.replace(":", "")
data=data.replace("{", "")    
data=data.replace("}", "")
CountyName=re.findall(r"CountyNameC(\w+),.*TemperatureC(\w+.\w*),.*Humidity(\w+)", data)
dt5=pd.DataFrame(CountyName)
dt5.insert(1,3,dt5[0]+"市")
dt5.replace(["田中市","日月潭市","澎湖市","馬祖市","恆春市","東沙島市","南沙島市"],\
            ["田中","日月潭","澎湖","馬祖","恆春","東沙島","南沙島"],inplace=True)
dt5.columns = ["測站","縣市","溫度C","濕度%"]

ur3=pd.read_html("https://app.cwb.gov.tw/web/WindSpeed/WindSpeed_All.html")
label=ur3[0].tail(2)
c=ur3[0].shape
txt1=ur3[0][0:(c[0]-1)]
dt1=label.append(txt1,ignore_index=True).T   

label2=dt1.iloc[:2,:(c[0])]          
txt2=dt1[3:]
txt3=txt2[txt2.index%3==0]                      
txt3=txt3.reset_index(drop=True)

d=txt3.shape                         
txt4=txt3.iloc[:,2:(d[1]-1)]         
dt6=np.array(txt4)
s=dt6.shape

data1=[]
for i in range(s[0]):
    for j in range(s[1]):
        tmp=str(dt6[i][j][1:])
        data1.append(tmp)
dr=np.array(data1).reshape(s[0],s[1])
txt5=pd.DataFrame(dr).T
txt6=txt3.iloc[:,0:2].T
txt7=txt6.append(txt5,ignore_index=True).T

dt2=label2.append(txt7,ignore_index=True).T
dt3=dt2.iloc[0:,[0,1,2,26]]
d=dt3.loc[0,2]
dt3.columns = ["縣市","測站",d+"風速","今日最大風速"]
dt4=dt3.drop(index=[0,1,567])

dt=pd.merge(dt4,dt5,on="縣市",how="left")   
dt.drop(axis=1, columns="測站_y", inplace=True)   
print(dt)
