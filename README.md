# InstaGram-Login-API
Best Private Api For Login Instagram Account Using Python #InstagramAPI #InstagramLogin #InstagramModule

Install This Module
pip install NamasteiG

from NamasteiG import Instagram
UserName=""
PassWord=""
Data=Instagram.Login(UserName,PassWord)['Response'].text #PRINT DATA IN TEXT
print(Data)

Data=Instagram.Login(UserName,PassWord)['Response'].headers #PRINT DATA IN HEADERS
print(Data)

Data=Instagram.Login(UserName,PassWord) #PRINT ALL DATA
print(Data)
