import json
import requests
#import urllib

apitoken="1lUWrQ0qY3MauPM6KAlXJkeXs5bZUsW2Ghw3zSQb7rAtDLv75SRal4Ft7MnvQfuI"
vraurlbase="https://api.mgmt.vmware.com/"
headers = {'Content-Type': 'application/json'}
api_url = "https://api.mgmt.cloud.vmware.com/iaas/api/login"

print (vraurlbase)

#
# DEFINE GET TOKEN FUNCTION
#


def get_token():
    #api_url = "https://api.mgmt.cloud.vmware.com/iaas/api/login"
    #api_url_plus = '{0}/iaas/api/login'.format(vraurlbase)
    #print ("URL with FORMAT COMMAND: " + api_url_plus)
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

#
#   END FUNCTION DEFINITION
#

#LOGIN TO VRA CLOUD
access_key = get_token()
headers1 = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(access_key)}

#DISPLAY LOGIN RESULTS

print ("\n\n####################################\n\n")
if access_key:
    print ("SUCCESSFUL LOGIN WITH TOKEN")
else:
    print ("ERROR NO ACCESS KEY")
print ("\n\n####################################\n\n")
#
# DEFINE EXTRACT VALUES FUNCTION
#

def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []
    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr
    results = extract(obj, arr, key)
    return results

#   END FUNCTION DEFINITION

#
#   DEFINE GET DEPLOYMENT IDS FUNCTION
#

def get_deployment_ids():
    #api_url = '{0}deployment/api/deployments'.format(vraurlbase)
    api_url = "https://api.mgmt.cloud.vmware.com/deployment/api/deployments"
 

    response = requests.get(api_url, headers=headers1, verify=False)
    if response.status_code == 200:
        json_data = json.loads(response.content.decode('utf-8'))
        ca_id = extract_values(json_data,'id')
        return ca_id
    else:
        print(response.status_code)

# END FUNCTION DEFINTION

#
#   GET ALL DEPLOYMENTS AND COUNT NUMBER
#

vraDeployments = get_deployment_ids()

print ("\n\n####################################\n\n")

if len(vraDeployments) == 0:
    print ("ERROR: No deployments returned")
else:
    print (str(len(vraDeployments)) + " deployments found")

print ("\n\n####################################\n\n")