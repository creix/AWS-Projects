import requests
import json

# Obtain application credentials
response = requests.post('https://Counter.Social/api/v1/apps',
                         data={
                             'client_name': 'CCBDAApplication',
                             'redirect_uris': 'urn:ietf:wg:oauth:2.0:oob',
                             'scopes': 'read write follow push',
                             'website': 'http://localhost',
                         })

if response.status_code != 200:
    print(response.status_code, response.text)
    exit(-1)

app = json.loads(response.text)
print(json.dumps(app, indent=3))


# Obtain application access token
response = requests.post('https://Counter.Social/oauth/token',
                         data={
                             'client_id': app['client_id'],
                             'client_secret': app['client_secret'],
                             'redirect_uri': 'urn:ietf:wg:oauth:2.0:oob',
                             'grant_type': 'client_credentials'
                         })

if response.status_code != 200:
    print(response.status_code, response.text)
    exit(-1)

token = json.loads(response.text)
print(json.dumps(token, indent=3))


# Verify that the access token is working correctly
response = requests.get('https://Counter.Social/api/v1/apps/verify_credentials', headers={
    'Authorization': 'Bearer %s'%(token['access_token']),
})

if response.status_code != 200:
    print (response.status_code, response.text)
    exit(-1)

verification = json.loads(response.text)
print(json.dumps(verification, indent=3))


# Get the lists of the followers
response = requests.get('https://Counter.Social/api/v1/timelines/public')
responses = json.loads(response.text)

response = requests.get('https://Counter.Social/api/v1/accounts/%s/following' % responses[0]['account']['id'],
                        headers={'Authorization': 'Bearer %s' % token['access_token']})

if response.status_code != 200:
    print(response.status_code, response.text)
    exit(-1)

followers = json.loads(response.text)
for item in followers:
    print(json.dumps(item, indent=3))