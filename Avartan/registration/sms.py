import http.client
from django.http import HttpResponse
import urllib
from urllib.request import urlopen

# import urllib2 # Python URL functions


def send_sms(contact, message):
    conn = http.client.HTTPSConnection("api.msg91.com")

    payload = '{ \"sender\": \"TCNITR\", \"route\": \"4\", \"country\": \"91\", \"sms\": [ { \"message\": \"'+message+'\", \"to\": [ \"'+str(contact)+'\" ] } ] }'

    headers = {
        'authkey': "286341AFU42bn6r5d35f6ab",
        'content-type': "application/json"
        }

    conn.request("POST", "/api/v2/sendsms?country=91", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    return HttpResponse('Registration successful!!!')


    # authkey = "238837A7MVgzyG6Svd5ba4def9" # Your authentication key.
    #
    # mobiles = "8720094989" # Multiple mobiles numbers separated by comma.
    #
    # message = "+message+" # Your message to send.
    #
    # sender = "TCNITR" # Sender ID,While using route4 sender id should be 6 characters long.
    #
    # route = "default" # Define route
    #
    # # Prepare you post parameters
    # values = {
    #           'authkey' : authkey,
    #           'mobiles' : mobiles,
    #           'message' : message,
    #           'sender' : sender,
    #           'route' : route
    #           }
    #
    #
    # url = "http://sms1.codenicely.in/api/sendhttp.php" # API URL
    #
    # postdata = urllib.parse.urlencode(values).encode("utf-8") # URL encoding the data here.
    #
    # req = urllib.request.Request(url, postdata)
    #
    # response = urlopen(req)
    #
    # output = response.read() # Get Response
    #
    # print (output) # Print Response
