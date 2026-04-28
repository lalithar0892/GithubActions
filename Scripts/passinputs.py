import sys
import requests
num = int(sys.argv[1])

a=[]
j=0
for i in range(num):
    a.append(j)
    j+=1
print(f"The Array : {a}")

response = requests.get("https://api.github.com")
print(response.status_code)