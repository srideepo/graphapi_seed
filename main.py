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

#method 1: authentication with authorization code
client_instance = msal.ConfidentialClientApplication(
    client_id=APPLICATION_ID,
    client_credential=CLIENT_SECRET,
    authority=authority_url
)
print(client_instance)

authorization_request_url = client_instance.get_authorization_request_url(SCOPES)
print(authorization_request_url)
webbrowser.open(authorization_request_url, new=True)

#below code obtained from Graph explorer -> signin -> Access token
authorization_code = '<ACCESS_TOKEN>'
access_token = client_instance.acquire_token_by_authorization_code(
    code=authorization_code,
    scopes=SCOPES
)
access_token_id = access_token['access_token']
headers = {'Authorization': 'Bearer ' + access_token_id}

endpoint = base_url + 'me'
response = requests.get(endpoint, headers=headers)
print(response)
print(response.json())

