import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url="https://www.osmania.ac.in/res07/20190318.jsp"

headers={
	# 'url':'https://www.osmania.ac.in/res07/20190318.jsp',
	'Connection': 'close',
	'Content-Type': 'text/html;charset=ISO-8859-1',
	'Date': 'Mon, 24 Jun 2019 07:04:43 GMT',
	'Server': 'Apache/2.2.15 (CentOS)',
	'Transfer-Encoding': 'chunked'
}

c=requests.Session()


rollno="245318737090"
data={'mbstatus':'SEARCH','htno':rollno,'Submit.x':'32','Submit.y':'14'}
res=c.post(url,data=data)
s = BeautifulSoup(res.content, 'html.parser')
#title=s.find_all('title')[0].get_text()
#print(title)
#subtitle=s.find_all('p')[0].get_text()
#print(subtitle)
#date=s.find_all('p')[1].get_text()
#print(date)
#subtitle2=s.find_all('td')[2].get_text()
#print(subtitle2)
#from array import *
#subject=array('i',[1,2,3,4,5])


#subject[i]=int(s.find_all('table')[1].find_all('tr')[8].find_all('td')[0].get_text())#typecasting subject to int from unicode for comparison
#print(type(subject))
#print(subject) 
#title=s.find_all('table')[1].find_all('tr')[7].find_all('td')[0].get_text()
#print(title)

enter=input("enter the code no:")
name=s.find_all('table')[1].find_all('tr')[8].find_all('td')[1].get_text()
name=name.replace(u'\xa0', ' ').encode('utf-8')
name=name.strip()
title=[enter, name]
for x in range(len(title)):
	print title[x],