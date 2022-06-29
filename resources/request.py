fp=open("requests_output.txt","w")
print=fp.write

import requests
res=requests.get("https://example.com")


print("Headers:\n"+str(res.headers))
print("\n\nURL:"+res.url)
print("\n\nStatus Code:"+str(res.status_code))
print("\n"+res.text) #Content of the response, in unicode.


fp.close()