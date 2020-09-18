import json
import requests
#import urllib

apitoken="1lUWrQ0qY3MauPM6KAlXJkeXs5bZUsW2Ghw3zSQb7rAtDLv75SRal4Ft7MnvQfuI"
vraurlbase="https://api.mgmt.vmware.com"
headers = {'Content-Type': 'application/json'}


print (vraurlbase)

def get_token():
    api_url = "https://api.mgmt.cloud.vmware.com/iaas/api/login"
    api_url_plus = '{0}/iaas/api/login'.format(vraurlbase)
    print ("URL with FORMAT COMMAND: " + api_url_plus)
    data =  {
              "refreshToken" : apitoken
            }
    response = requests.post(api_url, headers=headers, data=json.dumps(data), verify=False)
    if response.status_code == 200:
        json_data = json.loads(response.content.decode('utf-8'))
        key = json_data['token']
        return key
    else:
        return None

access_key = get_token()
headers1 = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(access_key)}

if access_key:
    print ("SUCCESSFUL LOGIN WITH TOKEN")
else:
    print ("ERROR NO ACCESS KEY")

print (headers1)