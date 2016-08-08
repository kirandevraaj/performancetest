import unittest
import requests
import urllib
import xml.dom.minidom
import os
import HTMLTestRunner

class TestAudit(unittest.TestCase):
    def test_get_token(self):
        self.token_req=requests.get("https://10.76.155.49:8001/nccmws/api/v1/Token",verify = False,auth=('admin', 'Cisco123'))
        #print self.token_req.status_code
        self.token = self.token_req.text.split()
        self.str_token= str(self.token[1])
        self.assertEqual(self.token_req.status_code,200)
        return self.str_token


    def test_run_compliance(self):
            with open("compliance_req.xml") as myfile:
                self.xml_data ="".join(line.rstrip() for line in myfile)
            encoded_xml_data = urllib.quote_plus(self.xml_data)
            url = "https://10.76.155.49:8001/nccmws/api/v1/Request"
            headers = {'authorization': 'Bearer ' + self.test_get_token(),'content-type': "application/x-www-form-urlencoded"}
            response = requests.post(url,verify=False,headers = headers,data='request='+ encoded_xml_data)
            print response.status_code
            #print response.text
            #return response.text # getting xml response
            self.assertEqual(response.status_code,200)


suite = unittest.TestLoader().loadTestsFromTestCase(TestAudit)
#unittest.TextTestRunner(verbosity=2).run(suite)

outfile = open("Report2.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Test Report',
                description='This is to demonstrate rest api automation'
                )
runner.run(suite)