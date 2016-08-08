import requests
import urllib2
import urllib
import xml.etree.ElementTree

token = requests.get("https://10.76.155.49:8001/nccmws/api/v1/Token",verify = False,auth=('admin', 'Cisco123'))
print token.text
token = token.text.split()
print token
str_token= str(token[1])
print "access token: ",str_token

xml_data = '<?xml version="1.0" encoding="UTF-8"?> <Request requestId="1342957791425">     <GetReport>         <ReportName>manage_cspc_instances</ReportName>     </GetReport> </Request>'
encoded_xml_data = urllib.quote_plus(xml_data)
print encoded_xml_data

url = "https://10.76.155.49:8001/nccmws/api/v1/Request"
headers = {
    'authorization': 'Bearer ' + str_token,
    'content-type': "application/x-www-form-urlencoded"
    }
response = requests.post(url,verify=False,headers = headers,data='request='+encoded_xml_data)
print response.text