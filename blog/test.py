import requests # 오류가있으면“pip install requests”
HOST= 'http://127.0.0.1:8000'
res= requests.post(HOST+ '/api-token-auth/',{
  'username': 'siwoo',
  'password': '0312',
  })
res.raise_for_status()
token= res.json()['token']
print(token)
# 인증이필요한요청에아래의headers를붙임
headers= {'Authorization': 'JWT '+ token, 'Accept': 'application/json'}
# Post Create
data= {
  'title': '제목by code', 
  'text': 'API내용by code',
  'created_date': '2024-06-03T18:34:00+09:00',
  'published_date': '2024-06-03T18:34:00+09:00',
  'author': 1
  }
file= {'image': open(r'c:\Users\sieup\OneDrive\Desktop\mobile\web_blog\몽.jpg', 'rb')}
res= requests.post(HOST+ '/api_root/Post/', data=data, files=file, headers=headers)
print(res)
print(res.json())