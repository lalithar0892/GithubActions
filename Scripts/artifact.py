import sys
import requests
import urllib.parse

name = sys.argv[1] if len(sys.argv) > 1 else "cat"

# Fix: Capitalize properly for Wikipedia API
topic = name.strip().capitalize()

api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(topic)}"

response = requests.get(api_url)

with open("file1.txt", "w", encoding="utf-8") as f:

    f.write(f"Search Query: {name}\n")
    f.write(f"Search URL: https://en.wikipedia.org/wiki/{urllib.parse.quote(name)}\n\n")

    if response.status_code == 200:
        data = response.json()

        title = data.get("title", "No Title")
        extract = data.get("extract", "")

        if extract:
            f.write(f"Topic: {title}\n\n")
            f.write(f"Info: {extract}\n")
        else:
            f.write("No summary available for this topic.")
    else:
        f.write("No information found for this topic.")

print("file1.txt created successfully")