import unittest
import requests
import urllib
import xml.dom.minidom
import os
import HTMLTestRunner
import ConfigParser

class TestToken(unittest.TestCase):
    #token = ""
    def setUp(self):
        #print "Kiran ------------"
        Config = ConfigParser.ConfigParser()
        Config.read("nccm_config.ini")
        self.token_url =  Config.get('NCCM URL','token_url')
        self.request_url =  Config.get('NCCM URL','request_url')
        self.user = Config.get('Credentials','username')
        self.passw = Config.get('Credentials','password')
        pass

    def test_nccm_token(self):
        self.token_req=requests.get(self.token_url,verify = False,auth=(self.user, self.passw)) # credentials & host in a config file
        #print self.token_req.status_code
        self.token = self.token_req.text.split()
        str_token= str(self.token[1])
        self.assertEqual(self.token_req.status_code,200)
        #print str_token
        #print "Token--------------------",TestToken.token
        return str_token
        #print str_token
        #print type(self.str_token)

    def tearDown(self):
        pass