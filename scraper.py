# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:44:55 2021

@author: Yumna
"""
#Python program to scrape website 
import requests
from bs4 import BeautifulSoup
#import pygsheets
import pandas as pd
import urllib.request

#gc = pygsheets.authorize(service_file=r"C:\Users\Yumna\.spyder-py3\tcscompetitors.json")
#https://www.airliftexpress.com/product-category/new-arrivals-new-arrivals-i596
'''cosmetics beverages 13'''

#URL = "https://www.naheed.pk/health-beauty/personal-care?p=6&product_list_limit=40"
URL = input("Please enter a URL:\n")
r = requests.get(URL)
soup = BeautifulSoup(r.content,'html5lib')   
data=[]
imgExt = ".jpg"
imgNames = []
table = soup.find('div', attrs = {'class':'category-products clearfix products wrapper grid products-grid'}) 

imgFolder = input("Enter folder URL")
SheetPath = input("Enter Sheet URL")

for row in table.findAll('div', attrs = {'class':'product-item-info per-product category-products-grid'}):
    imageURL = row.img['src']
    breakURL = imageURL.split("/")[-4:]
    url = breakURL[0]
    string_tobeReplace = "49dcd5d85f0fa4d590e132d0368d8132"
    imgURL = imageURL.replace(url,string_tobeReplace)
    print("imggg-url",imgURL)
    
    imageNo = breakURL[3]
    img_list = list(imageNo)
    
    imgName = row.img['alt'].split(" #")[0]
    imageName =  imgName.replace("\n","").replace("-","").replace("+","").replace("%","").replace("*","").replace("/","").replace("\t","").replace(",","").replace(".","").replace("%r","")
    print("iName->",imageName)
    items = row.img['alt'].split(" #")[0],imgURL
    data.append(items)
 #directory = r"C:\Users\Yumna\Documents\NaheedImages\Test\%s%s" % (imageName,imgExt)
    directory = imgFolder+"\%s%s" % (imageName,imgExt)
 #print("path ->", directory)
       
    urllib.request.urlretrieve(imgURL,directory)
      
print('data',data)

df = pd.DataFrame(data, columns=['ProductName','Image'])
df.to_csv(SheetPath, index = False, header=True)
#C:\Users\Yumna\Documents\NaheedImages\test.csv
print (df)
#sh = gc.open('Data2')
#wks = sh[11]
#wks.set_dataframe(df,(1,1))
