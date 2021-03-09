# vRA Cloud REST API and JSON in Python

import requests
import json

# basline variables
# this script is designed for vRA Cloud; in the vRA API, you do not authenticate to vRA with Username and password
# You must first get an API key from the vRA Cloud Console
# simple string variables can be used
vracloudurlbase = "https://api.mgmt.cloud.vmware.com"
apikey = ""


# vRA Authentication POST command to get Bearer Token
# The API key is not used in the REST commands itself, you must first get a Bearer token or 'Refresh Token'
# This token is used in the Authorization Header of all subsequent API Calls

#------------------------------------
#
# Python Function Definition - get_vra_bearer_token
#
#------------------------------------

def get_vra_bearer_token (apitoken): 
    # REST Headers are key-value pairs and the Python 'Dictionary' data structure is a perfect way to store them
    # For the API REQEUST METHOD 
    # For details on the Python Dictionary data structure see https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3#:~:text=Dictionaries%20map%20keys%20to%20values,braces%20on%20either%20side%20%7B%20%7D%20.
    headers = {'Content-Type': 'application/json'}

    #In this version, we will use simple concatenation to construct the full REST URL that will be used in the POST COMMAND
    #In a later versions of , we will use the "format" command that seems to be in favor by most python developers
    getTokenURL  = vracloudurlbase + "/iaas/api/login"

    #OPTIONAL Print the values of your variables to make sure they are properly set
    print("\nURL: " + getTokenURL)
    print ("\nAPI KEY: " + apitoken)

    #IN THIS EXAMPLE, we are doing things one step at a time. Before we can execute the REST POST command, we need for format the BODY of the POST request
    #We stored that in the "headers" dictionary. Here we will FIRST execute a JSON command "dumps" to format the headers into JSON format
    #The JSON BODY is defined in this DICTIONARY
    jsonBody = {
              "refreshToken" : apitoken
            }

    #We format this into JSON using the json.dumps command here
    # See this page for details on the json.dump and json.dumps commands https://www.geeksforgeeks.org/json-dump-in-python/#:~:text=The%20dump()%20method%20is,be%20stored%20as%20an%20argument
    data = json.dumps(jsonBody)

    

    #OPTIONAL: Let's print out the formatted JSON "body" of our POST COMMAND (need to convert the DICT to string first using "str")
    print ("\nJSON HEADER: " + str(jsonBody))
    print ("\nAfter json.dumps..... : " + str(data))
    
    print ("\nTIME TO EXECUTE THE REST POST COMMAND......")
    print ("\nThe command will be: response = requests.post(" + getTokenURL + ", headers=" + str(headers) +", data=" + str(data) + ", verify=False)")

    # Now, we authenticate to the vRA API to send the API key and the Headers to retrieve a Bearer token.
    # We will use the requests.post Method
    # For details on this python method see: https://www.geeksforgeeks.org/get-post-requests-using-python/
    #response = requests.post(api_url, headers=headers, data=json.dumps(data), verify=False)

    print ("\nEXECUTING POST COMMAND NOW.........................\n")

    response = requests.post(getTokenURL, headers=headers, data=data, verify=False)

    #Before we parse the results, lets check the REST response code. We expect to see a 200 code if the REST POST CALL WAS SUCCESSFUL
    print ("REST RESPONSE CODE IS: " + str(response.status_code))

    #Now that we know the API call was successful, we will parse the result to get the bearer token we wanted
    #We will still include logic to verify we actually did get a successful code, using an if-then clause

    if response.status_code == 200:
        # We will parse the results into proper jSON format using the json.loads commmand against the RESPONSE we just retrieved
        # json.loads is basically the opposite of the json.dumps command we executed earlier to format the BODY of the REST command
        # Where the json.dumps converted a python DICIONARY to JSON, the JSON loads converts a JSON string INTO a python DICTIONARY
        # For details on the json.loads command see: https://www.programiz.com/python-programming/json
        # Also check this: https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

            print ("\nRaw response: " + str(response.text))
            json_data = json.loads(response.content.decode('utf-8'))

        #Now that we have the JSON, we can parse it to find what we needed all along, the value of 'token'
            key = json_data['token']
            return key
    else:
            return None
    
   
## ALL DONE!!! THIS IS A VERY INEFFICIENT STYLE OF CODE, BUT IT WAS DONE THIS WAY TO DISSECT EVERYTHING THAT IS GOING ON WITHIN PYTHON
## The next function produces the exact same result, but does so in much more elegant code.



 ###### END FUNCTION DEFINITION #########################################################################

#------------------------------------
#
# Python Function Definition - get_token
#
#------------------------------------

# THIS FUCTION DOES EXACTLY what the previous function does without all of the individual steps broken out.
# It also uses a more preferred method of concatenation by using the Python format command instead of the 
# crude method of concatenation used above...

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

# MUCH MORE COMPACT THAN THE VERSION ABOVE

###### END FUNCTION DEFINITION #########################################################################


#Use his to get the Bearer Token the long hard way -- but easier to understand
bearerToken = get_vra_bearer_token(apikey)

print ("\nThe Return value of the get_vra_bearer_token() function is: " + str(bearerToken) + "\n")

#Use this to get the Bearer Token using fewer lines of code LONG VERSION
#access_key = get_token(apikey)

# Rather than PRINT the entire Bearer Token like we did before, we will simply test the value of the key

if access_key:
    print ("\nSUCCESSFUL LOGIN WITH TOKEN IN SHORT VERSION")
else:
  print ("\nERROR NO ACCESS KEY IN SHORT VERSION")

  #This is an extra line to format a header for all subsequent REST CALLS IN THIS SCRIPT

headers1 = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(access_key)}

#NOW...we can use the access_key to EXECUTE REST COMMANDS IN THE API

