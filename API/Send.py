import requests
data={
'subjects':{'documents':['hello world!','Bye People'],'categories':['greeting','exit greetings']},
'forms':{'documents':['a','b'],'categories':['a','b']}
}

# r=requests.post('https://httpbin.org/post',data=data)
r=requests.post('http://127.0.0.1:5000/',json=data)
# r_js=r.json()
