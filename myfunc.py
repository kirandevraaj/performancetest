import unittest
import requests
import urllib
import xml.dom.minidom
import os
import HTMLTestRunner
import ConfigParser
import time

class TestCustomAudit(unittest.TestCase):
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

    def test_add_custom_policy(self):
        #print self.str_token
        with open("add_custom_policy.xml") as myfile:
            self.xml_data ="".join(line.rstrip() for line in myfile)
        encoded_xml_data = urllib.quote_plus(self.xml_data)
        Config = ConfigParser.ConfigParser()
        Config.read("nccm_config.ini")
        headers = {'authorization': 'Bearer ' + self.test_get_token(),'content-type': "application/x-www-form-urlencoded"}
        response = requests.post(self.request_url,verify=False,headers = headers,data='request='+ encoded_xml_data)
        #print response.status_code
        #print response.text
        return response.text # getting xml response
        self.assertEqual(self.response.status_code,200)

    def test_add_policy_group(self):
        #print self.str_token
        with open("add_policy_group.xml") as myfile:
            self.xml_data ="".join(line.rstrip() for line in myfile)
        encoded_xml_data = urllib.quote_plus(self.xml_data)
        Config = ConfigParser.ConfigParser()
        Config.read("nccm_config.ini")
        headers = {'authorization': 'Bearer ' + self.test_get_token(),'content-type': "application/x-www-form-urlencoded"}
        response = requests.post(self.request_url,verify=False,headers = headers,data='request='+ encoded_xml_data)
        #print response.status_code
        #print response.text
        return response.text # getting xml response
        self.assertEqual(self.response.status_code,200)

    def test_add_policy_profile(self):
        #print self.str_token
        with open("add_policy_profile.xml") as myfile:
            self.xml_data ="".join(line.rstrip() for line in myfile)
        encoded_xml_data = urllib.quote_plus(self.xml_data)
        Config = ConfigParser.ConfigParser()
        Config.read("nccm_config.ini")
        headers = {'authorization': 'Bearer ' + self.test_get_token(),'content-type': "application/x-www-form-urlencoded"}
        response = requests.post(self.request_url,verify=False,headers = headers,data='request='+ encoded_xml_data)
        #print response.status_code
        #print response.text
        return response.text # getting xml response
        self.assertEqual(self.response.status_code,200)

    def test_execute_policy_profile(self):
        #print self.str_token
        with open("execute_policy_profile.xml") as myfile:
            self.xml_data ="".join(line.rstrip() for line in myfile)
        encoded_xml_data = urllib.quote_plus(self.xml_data)
        Config = ConfigParser.ConfigParser()
        Config.read("nccm_config.ini")
        headers = {'authorization': 'Bearer ' + self.test_get_token(),'content-type': "application/x-www-form-urlencoded"}
        response = requests.post(self.request_url,verify=False,headers = headers,data='request='+ encoded_xml_data)
        #print response.status_code
        #print response.text
        return response.text # getting xml response
        self.assertEqual(self.response.status_code,200)

    def test_standard_compliance(self):
            with open("compliance_req.xml") as myfile:
                self.xml_data ="".join(line.rstrip() for line in myfile)
            encoded_xml_data = urllib.quote_plus(self.xml_data)
            Config = ConfigParser.ConfigParser()
            Config.read("nccm_config.ini")
            request_url =  Config.get('NCCM URL','request_url')
            headers = {'authorization': 'Bearer ' + self.test_get_token(),'content-type': "application/x-www-form-urlencoded"}
            response = requests.post(request_url,verify=False,headers = headers,data='request='+ encoded_xml_data)
            print response.status_code
            #print response.text
            #return response.text # getting xml response
            self.assertEqual(response.status_code,200)

    def tearDown(self):
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()