import os

#DEFINITION OF PING FUNCTION
def check_ping():
    hostname = "localhost"
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    return pingstatus

#EXECUTE PING TEST
pingstatus = check_ping()
print (pingstatus)

