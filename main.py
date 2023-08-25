from stravalib.client import Client
from stravalib import unithelper

scope = ['read', 'profile:read_all', 'activity:read']
access_token = 'f0f17736429d2893e3f49747cddcc36c00055ff5'

client = Client(access_token=access_token)

# I think redirect_uri will need to change to my web app name:
redirect_uri = 'https://www.strava.testapp.com'

client_id = 84165
print(client.authorization_url(client_id=client_id, redirect_uri=redirect_uri, scope=scope))

athlete = client.get_athlete()
runs_raw = list(client.get_activities(limit=10))
#
print(runs_raw)
