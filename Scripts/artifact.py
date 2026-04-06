import sys
import requests
import urllib.parse

name = sys.argv[1] if len(sys.argv) > 1 else "cat"

search_url = f"https://en.wikipedia.org/wiki/{urllib.parse.quote(name)}"

response = requests.get(search_url)

with open("file1.txt", "w", encoding="utf-8") as f:

    f.write(f"Search Query: {name}\n")
    f.write(f"Search URL: {search_url}\n\n")

    api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{name}"
    api_response = requests.get(api_url)

    if api_response.status_code == 200:
        data = api_response.json()

        title = data.get("title", "No Title")
        extract = data.get("extract", "No Info Found")

        f.write(f"Topic: {title}\n\n")
        f.write(f"Info: {extract}\n")
    else:
        f.write("No detailed information found.")

print("file1.txt created successfully")