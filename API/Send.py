import requests
data={'document':'''
 Venkatesh Ratnaparkhe Developer Problem Solver venkateshr3011@gmail.com +91 7666169577 https://www.linkedin.com/in /venkatesh-ratnaparkhe-23 354a198 EDUCATION
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
English,Marathi,Hindi''','category':'Resume'}
# r=requests.post('https://httpbin.org/post',data=data)
r=requests.post('http://127.0.0.1:5000/',data=data)
r_js=r.json()
print(r_js['name'])