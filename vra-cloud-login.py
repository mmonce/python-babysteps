# vRA Cloud REST API and JSON in Python

import requests
import json

# basline variables
# this script is designed for vRA Cloud; in the vRA API, you do not authenticate to vRA with Username and password
# You must first get an API key from the vRA Cloud Console
# simple string variables can be used
vracloudurlbase = "https://api.mgmt.cloud.vmware.com"
apikey = "7L5DrmFNID7fEuOy0txXJuY32rD7sYvyyxCbpmotknuoaezwSCRTdyKq260taj7j"

def get_token(apitoken):

    headers = {'Content-Type': 'application/json'}
   
    api_url = '{0}/iaas/api/login'.format(vracloudurlbase)
   
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



access_key = get_token(apikey)



if access_key:
    print ("\nSUCCESSFUL LOGIN WITH TOKEN IN SHORT VERSION")
else:
  print ("\nERROR NO ACCESS KEY IN SHORT VERSION")



headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(access_key)}

