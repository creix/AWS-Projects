import requests
import json

response = requests.get('https://Counter.Social/api/v1/timelines/public')
if response.status_code != 200:
    print(response.status_code, response.text)

responses = json.loads(response.text)

for item in responses:
    print(json.dumps(item, indent=3))
