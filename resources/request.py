from io import TextIOWrapper
import requests

fp: TextIOWrapper = open("response.txt", "w")
print = fp.write

# GET example.com
res = requests.get("https://example.com")


print("Headers:\n" + str(res.headers))

print("\n\nURL:" + res.url)

print("\n\nStatus Code:" + str(res.status_code))

# Content of the response, in unicode.
print("\n" + res.text)


fp.close()
