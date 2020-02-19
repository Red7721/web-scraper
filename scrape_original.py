import requests
from bs4 import BeautifulSoup
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
rollno=input("enter roll no: ")
enter = int(input('enter subject code: '))
x=0
while(x < 4):    
    number = int(rollno)
    #number = number + 1
    rollno = str(number)
    data={'mbstatus':'SEARCH','htno':rollno,'Submit.x':'32','Submit.y':'14'}
    res=c.post(url,data=data)
    s = BeautifulSoup(res.content, 'html.parser')
    name = s.find_all('table')[0].find_all('tr')[6].find_all('td')[1].get_text()
    z=8
    while(z < 13):
        subject = s.find_all('table')[1].find_all('tr')[z].find_all('td')[0].get_text()
        if int(subject) == enter:
         grade = s.find_all('table')[1].find_all('tr')[z].find_all('td')[3].get_text()
         gradez = s.find_all('table')[1].find_all('tr')[z].find_all('td')[4].get_text()
         sbname = s.find_all('table')[1].find_all('tr')[z].find_all('td')[1].get_text()
         credit =s.find_all('table')[1].find_all('tr')[z].find_all('td')[2].get_text()
         print(rollno)
         print(name)
         print(subject)
         print(sbname)
         print(credit)
         print(int(grade))
         print(gradez)
         z = z + 1   
        else:
         z = z + 1
    x = x + 1
    rollno = number + 1 