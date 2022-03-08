# Send file is a file primarily for testing purpose
# It is to check how well API is working!
import requests

# API Format
'''
#{'metafield1':{'documents':[...],'categories':[...]},
#'metafield2':{'documents':[...],'categories':[...]},
....}'''

data={
'type':{'documents':['''Yash Sapre           
LINKEDIN: LINKEDIN.COM/IN/YASH-SAPRE-16AB411B9 
GITHUB: https://github.com/Yash-Sapre  
Education: 
10 th  standard:  86%, 12 th  standard: 76.92%, CET rank: 96.45 percentile 
MMCOE Pune (Computer Engineering) 
First Year: 7.9, Second Year: 9.18 
 
Technologies: 
Python, JavaScript, Bootstrap, SQL, CSS 
Python modules: Django, Keras, Flask, Web3, Numpy, Pandas, Matplotlib, Django Rest Framework, 
Yahoo Finance, Regex, Sklearn, BS4, Requests 
 
Experience: 
Created Django and Deep Learning Projects and uploaded to GitHub. 
Participated in 2 hackathons. 
 
Certificates: 
DJANGO FOR EVERYBODY SPECIALIZATION (COURSERA), PYTHON 101 COURSE (COGNITIVE CLASS), 
FUNDAMENTALS OF SCALABLE DATA SCIENCE(COURSERA),DEEPLEARNING.AI COURSE 1 
PYTHON(BASIC) HACKERRANK '''
,'''letter
The Headmistress

St. Francis Anglo Indian Girls High School

Noida – 110096

25th November, 2021

Subject: Seeking Permission to Attend a Family Function

Respected Ma’am,

I am writing to seek your permission for me to attend a family function on the 29th of November at Bangalore. I would require a leave of three days (from 28.11.2021 to 30.11.2021). I have taken permission from my Class Teacher, and I will ensure that I keep myself informed about the daily lessons and complete everything up-to-date when I am back. Kindly consider my request and grant me permission.

Thanking you

Yours sincerely,

Saajan Jose

Class IX C

Roll No. 36
''','''
Rahul Agrawal
Developer , Problem Solver
Sinhgad Road , Pune - 411041
+91 9404164086
rahul.biz.2002@gmail.com
rahul-agrawal.me
linkedin.com/rahulagrawal99
github.com/rahul-agrawal-99
EDUCATION
MM’s College of Engineering , Pune — B.E.
July 2019 - 2023
Exploring fields in computer technology
CGPA : 9.66 (as of third year)
BK chavan highschool, Pune— 12th hsc
2017 - 2019
Passed hsc in science field with 82%
Scored 97 percentile in MH-CET
PROJECTS
Document Image Analysis — NLP
identify key element related to identity from documents like Adhar , pan
Online mini shop— Web Development
Web application using Flask and SQLite with python
Cryptocurrency Price Prediction-Deep Learning
Flask based web app used to predict cryptocurrency price using LSTM
Insta Messege bomber-software testing
selenium based script used send infinite message on instagram
SKILLS
Machine Learning,Data
Science , Deep learning ,
computer vision , NLP
DBMS , SQL
C++, Python, Java
Data Structure
Problem Solving
HTML,CSS,Javascript
Flask , FastAPI
DevOps with git , maven ,
jenkins , docker, kubernetes
AWS cloud
AWARDS
Hack-Sprint hackathon
runner up
LANGUAGES
English , Hindi , Marathi
'''
],





'categories':['resume','letter','resume']}
}
data2 = {'type':{'document':['''
Venkatesh Ratnaparkhe
Developer Problem Solver
venkateshr3011@gmail.com
+91 7666169577
https://www.linkedin.com/in
/venkatesh-ratnaparkhe-23
354a198
EDUCATION
Marathwada Mirta Mandal’s College Of
Engineering, Pune - B.E Computer Engineering
2019-2023
CGPA-9.66
->Honors in Data Science
PROJECTS
Food Ordering System — Web Development
Web application using Flask and SQL with python
Quiz Platform – web Development
Web application using django,Bootstrap,HTML,css
Resume Uploader-web Development
Web app to keep track of resume record using django,
Bootstrap,HTML,css
Cryptocurrency Price Prediction-Deep Learning
Flask based web app used to predict cryptocurrency price
Campus Placement Prediction-Machine Learning
Flask based web app using ML algorithms to predict
Campus placement
SKILLS
Data Structure,Problem
Solving,DBMS
C++,Python,Java,SQL
HTML,CSS,Javascript,
Bootstrap
Django,Flask
Machine Learning,Data
Science
AWARDS
Participated in Hacksprint
Hackathon
LANGUAGES
English,Marathi,Hindi

'''
]}}
# r=requests.post('https://httpbin.org/post',data=data)
# r=requests.post('http://127.0.0.1:5000/create',json=data)
r=requests.post('http://127.0.0.1:5000/predict',json=data2)
print(r.text)
# r_js=r.json()
