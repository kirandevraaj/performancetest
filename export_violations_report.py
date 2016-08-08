import unittest
import requests
import urllib
import xml.dom.minidom
import os
import HTMLTestRunner
import ConfigParser
import time
import BeautifulSoup
import lxml
import xml.etree.ElementTree as ET
from xml.dom import minidom
from lxml import etree



class Export_Violations_Report(unittest.TestCase):
    def setUp(self):
        Config = ConfigParser.ConfigParser()
        Config.read("nccm_config.ini")
        self.token_url =  Config.get('NCCM URL','token_url')
        self.request_url =  Config.get('NCCM URL','request_url')
        self.user = Config.get('Credentials','username')
        self.passw = Config.get('Credentials','password')


    def test_get_token(self):
        self.token_req=requests.get(self.token_url,verify = False,auth=(self.user, self.passw)) # credentials & host in a config file
        #print self.token_req.status_code
        self.token = self.token_req.text.split()
        self.str_token= str(self.token[1])
        self.assertEqual(self.token_req.status_code,200)
        return self.str_token

    def test_export_audit_job(self):
        #print self.str_token
        with open("export_violations.xml") as myfile:
            self.xml_data ="".join(line.rstrip() for line in myfile)
        encoded_xml_data = urllib.quote_plus(self.xml_data)
        Config = ConfigParser.ConfigParser()
        Config.read("nccm_config.ini")
        headers = {'authorization': 'Bearer ' + self.test_get_token(),'content-type': "application/x-www-form-urlencoded"}
        response = requests.post(self.request_url,verify=False,headers = headers,data='request='+ encoded_xml_data)
        #print response.status_code
        print response.text
        return response.text # getting xml response
        self.assertEqual(self.response.status_code,200)

        def tearDown(self):
            time.sleep(300)
            pass

    if __name__ == '__main__':
        unittest.main(verbosity=2)