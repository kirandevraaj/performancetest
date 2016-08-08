import requests
import urllib2
import urllib

def token():
    token_req=requests.get("https://10.76.155.49:8001/nccmws/api/v1/Token",verify = False,auth=('admin', 'Cisco123'))
    token = token_req.text.split()
    #print token
    str_token= str(token[1])
    print str_token
    return str_token
token()
