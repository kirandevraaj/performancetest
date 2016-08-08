import requests
import urllib2
import urllib
import xml.etree.ElementTree as ET
from nccm_token import token
import xml.dom.minidom
import filecmp
import os

def xml_req(): # Sending the xml request to the server
    with open("user_req.xml") as myfile:
        xml_data="".join(line.rstrip() for line in myfile)
    encoded_xml_data = urllib.quote_plus(xml_data)
    url = "https://10.76.155.49:8001/nccmws/api/v1/Request"
    headers = {'authorization': 'Bearer ' + token(),'content-type': "application/x-www-form-urlencoded"}
    response = requests.post(url,verify=False,headers = headers,data='request='+encoded_xml_data)
    return response.text # getting xml response
xml_req()
#print xml_req()

xml = xml.dom.minidom.parseString(xml_req()) # Formatting the xml response
pretty_xml_as_string = xml.toprettyxml()
with open("response.xml","w") as f:
        f.writelines(pretty_xml_as_string)
        f.close()

#print filecmp.cmp("golden_reference.xml","response.xml")
golden_ref_size = os.path.getsize("golden_reference.xml")
print "Expected response file size: ",(golden_ref_size/1000.0),"KB"

actual_response_size = os.path.getsize("response.xml")
print "Acutal response file size:   ",(actual_response_size/1000.0), "KB"
