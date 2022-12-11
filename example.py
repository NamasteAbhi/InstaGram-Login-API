from NamasteiG import Instagram
UserName=""
PassWord=""
Data=Instagram.Login(UserName,PassWord)['Response'].text #PRINT DATA IN TEXT
print(Data)

Data=Instagram.Login(UserName,PassWord)['Response'].headers #PRINT DATA IN HEADERS
print(Data)

Data=Instagram.Login(UserName,PassWord) #PRINT ALL DATA
print(Data)
