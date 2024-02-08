import webbrowser
import requests
import msal
from msal import PublicClientApplication

APPLICATION_ID = '<APPLICATION_ID>'
CLIENT_SECRET = '<CLIENT_SECRET>'
TENANT_ID = '<TENANT_ID>'
authority_url = f'https://login.microsoftonline.com/{TENANT_ID}/'
#authority_url = 'https://login.microsoftonline.com/common/oauth2/nativeclient/'

base_url = 'https://graph.microsoft.com/v1.0/'

SCOPES = ['User.Read', 'User.Read.All']

#method 2: Login to acquire access_token
#for below to work must enable "Allow public client flows" under App registration.
#else error thrown "request body must contain client_secret"
app = PublicClientApplication(
    client_id=APPLICATION_ID,
    authority=authority_url
)

flow = app.initiate_device_flow(scopes=SCOPES)
print(flow)
print(flow['message'])
webbrowser.open(flow['verification_uri'])

access_token = app.acquire_token_by_device_flow(flow)
print('>>>>', access_token)
access_token_id = access_token['access_token']
headers = {'Authorization': 'Bearer ' + access_token_id}

endpoint = base_url + 'me'
response = requests.get(endpoint, headers=headers)
print(response)
print(response.json())
