# vRA Cloud REST API and JSON in Python

import requests
import json
import time
import os
import traceback
import argparse
import urllib3

# basline variables
# this script is designed for vRA Cloud; in the vRA API, you do not authenticate to vRA with Username and password
# You must first get an API key from the vRA Cloud Console
# simple string variables can be used
vracloudurlbase = "https://api.mgmt.cloud.vmware.com"
apikey = "7L5DrmFNID7fEuOy0txXJuY32rD7sYvyyxCbpmotknuoaezwSCRTdyKq260taj7j"
zoneID = "55bd885e-c436-4320-8659-aa54496f1384"

#---------------------------------------
# ALL PURPOSE JSON-PARSER FUNCTION
#----------------------------------------

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

#---------------------------------------
# GET BEARER TOKEN
#----------------------------------------

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

#---------------------------------------
# GET ALL CLOUD TEMPLATE (fka 'Blueprint') IDs
#----------------------------------------

# THIS FUNCTION USES ANOTHER FUNCTION "ALL PURPOSE JSON PARSER" TO PARSE THE JSON
# YOU can substitute the field you want by replacing "id" with another valid field


def create_project(vsphereczid):

    print ("ZONE ID: " + vsphereczid) #DELETE WHEN DONE

    api_url = '{0}/iaas/api/projects'.format(vracloudurlbase)

    print ("API URL : " + api_url) #DELETE WHEN DONE
    data =  {
                "administrators": [{ "email":"markmonce@yahoo.com" }],
                "members": [{ "email":"moncemark@gmail.com" }],
                "zoneAssignmentConfigurations": [
                    {
                    "zoneId": vsphereczid,
                    "priority": 0,
                    "maxNumberInstances": 0
                    }
                ],
                "operationTimeout": 0,
                "sharedResources": "true",
                "name": "Field Demo",
                "description": "Field Demo Project"
            }
    print ("Data: " + str(data))
    response = requests.post(api_url, headers=headers1, data=json.dumps(data), verify=False)
    if response.status_code == 201:
        json_data = json.loads(response.content.decode('utf-8'))
        print('Successfully Create Field Demo Project')
    else:
        print(response.status_code)
        return None

access_key = get_token(apikey)

headers1 = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(access_key)}

newProject = create_project(zoneID)

# i=11 #This is the array index of the ID to prind in line 96
# cloudTemplates = get_blueprint_ids()
# print ("ALL TEMPLATE IDS: \n")
# print (cloudTemplates)
# print ("\nTEMPLATE ID INDEX: " + str(i))
# print (cloudTemplates[i])

