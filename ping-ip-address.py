import os
import sys



#DEFINITION OF PING FUNCTION
def check_ping():
    ipAddress = str(sys.argv[1])
    print("Pinging Host at: " + ipAddress)

    hostname = ipAddress
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Active"
    else:
        pingstatus = "Error"
    return pingstatus

#EXECUTE PING TEST
pingstatus = check_ping()
 

print (pingstatus)

#WRITE PINGSTATUS TO A NEW FILE THAT CAN BE STORED AS AN ENV VARIABLE I THE LINUX SHELL AND BOUND TO OUTPUT
pythonoutputfile = open("ping_ip_results.txt","a+")
pythonoutputfile.write(pingstatus)
pythonoutputfile.close

