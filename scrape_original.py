import requests
from bs4 import BeautifulSoup
url="https://www.osmania.ac.in/res07/20201251.jsp"

headers={
	'url':'https://www.osmania.ac.in/res07/20201251.jsp',
	'Connection': 'close',
	'Content-Type': 'text/html;charset=ISO-8859-1',
	'Server': 'Apache/2.2.15 (CentOS)',
	'Transfer-Encoding': 'chunked'
}

c=requests.Session()
rollno= 160616735019 
number = int(rollno)
rollno = str(number)
data={'mbstatus':'SEARCH','htno':rollno,'Submit.x':'32','Submit.y':'14'}
res=c.post(url,data=data)
s = BeautifulSoup(res.content, 'html.parser')
name = s.body.find('table', attrs={'id':'AutoNumber4'})
some = name.find_all('td')
#print(len(some))
rel=[]
for x in range(2,len(some),5):
	rel.append(some[x].text)
for x in rel:
	print(x)