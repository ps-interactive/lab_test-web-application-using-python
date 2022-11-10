import requests
address = 'http://localhost'
useragentstring = {'User-Agent':'Bad_Actor_UserAgentString_v1'}
pageresponse = requests.get(address, headers=useragentstring)
print(pageresponse.content)

