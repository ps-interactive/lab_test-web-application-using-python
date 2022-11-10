import requests

address = 'http://localhost/DVWA-master'

dictionary = open("dictionary.txt","r")
for line in dictionaryfile:
  addresstotest = address + "/" + line.strip()
  print('Testing: '+addresstotest)
  pageresponse = requests.get(addresstotest)
  if pageresponse:
    print('Found a folder: '+addresstotest)


