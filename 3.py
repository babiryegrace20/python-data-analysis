# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:15:00 2019

@author: GRACE
"""

#ACCESSING WEB DATA
import requests 
from bs4 import BeautifulSoup
#the target we want to open 
url='https://www.monitor.co.ug/' 
#open with GET method
resp=requests.get(url)
print ("i am here")
print (resp)

#http_response 200 means OK status
if resp.status_code==200:
    print("successfully opened the web page")
    print("The news are as follow :- ")
    
#we need a parser, python built_in HTML parser is enough.
    soup = Beautifulsong(resp.text,'html.parser')
    
#1 is the list which contains all the text i.e news
    1=soup.find("div",{"class":"five-eight column"})
    print(results) 
    
#now we want to print only the text part of the anchor
    #print(1,"hello")
    for i in l.findAll("p"):
        print(i.text)
    #for i in 1.findAll("a")
      #print(i.text)
    else:
        print("error")
        
        
        
#Handling Exceptions
try:
    print(x)
except:
    print("something went wrong")
else:
    print("Nothing went wrong")
    
    

    