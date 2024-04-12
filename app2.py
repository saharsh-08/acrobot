# from config import AppConfig

# import msal

# # Enter the details of your AAD app registration
# client_id = "{", AppConfig.CLIENT_ID, "}"
# client_secret = "{", AppConfig.CLIENT_SECRET, "}"
# authority = "https://login.microsoftonline.com/", AppConfig.TENANT_ID
# scope = ['https://graph.microsoft.com/.default']

# # Create an MSAL instance providing the client_id, authority and client_credential parameters
# client = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)

# # First, try to lookup an access token in cache
# token_result = client.acquire_token_silent(scope, account=None)

# # If the token is available in cache, save it to a variable
# if token_result:
#   access_token = 'Bearer ' + token_result['access_token']
#   print('Access token was loaded from cache')

# # If the token is not available in cache, acquire a new one from Azure AD and save it to a variable
# if not token_result:
#   token_result = client.acquire_token_for_client(scopes=scope)
#   access_token = 'Bearer ' + token_result['access_token']
#   print('New access token was acquired from Azure AD')

# print(access_token)