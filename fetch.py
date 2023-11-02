import requests
import json
import pandas as pd

url_1 = "https://www.ubereats.com/gb/search?carid=eyJwbHVnaW4iOiJyZWNvbW1lbmRhdGlvbkZlZWRQbHVnaW4iLCJyZWNvbW1UeXBlIjoidG9wX3N0b3Jlc19ieV9jaXR5X3YyIiwidGl0bGUiOiJQb3B1bGFyIG5lYXIgeW91In0%3D&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMkJlbGZhc3QlMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKTzRyUTFfM19ZRWdSTWNYSDd5d1dWeTQlMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBNTQuNTk3Mjg1MDAwMDAwMDElMkMlMjJsb25naXR1ZGUlMjIlM0EtNS45MzAxMiU3RA%3D%3D&sc=HOME_FEED_ITEM&title=Popular%20near%20you"
url_2 = "https://www.ubereats.com/_p/api/getFeedV1"
local_url = "http://localhost:3000/api/data" 

# url = "https://webhook.site/781c6dd1-e8e7-4117-966c-37a8a1837461"

payload = ""
headers = {}
files={}

getCookies = requests.request("GET", url_1, headers=headers, data=payload)

payload = {}
headers = {
  'X-Csrf-Token': 'x',
  'Cookie': "; ".join([f"{key}={value}" for key, value in getCookies.cookies.items()])
}

getReview = requests.request("POST", url_2, headers=headers, data=payload, files=files)
# Check if the response contains JSON data
if getReview.status_code == 200 and 'application/json' in getReview.headers.get('content-type', 'application/json'):
    # Parse the JSON response and pretty-print it
    data = getReview.json()
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Data saved to 'data.json'")
    
else:
    print(getReview.text)   