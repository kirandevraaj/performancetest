import unittest
import requests
import urllib
import xml.dom.minidom
import os
import HTMLTestRunner
import ConfigParser
import BeautifulSoup


class TestZCompliance(unittest.TestCase):
    def setUp(self):
        Config = ConfigParser.ConfigParser()
        Config.read("nccm_config.ini")
        self.token_url =  Config.get('NCCM URL','token_url')
        self.request_url =  Config.get('NCCM URL','request_url')
        self.user = Config.get('Credentials','username')
        self.passw = Config.get('Credentials','password')
        pass

    def test_get_token(self):
        self.token_req=requests.get(self.token_url,verify = False,auth=(self.user, self.passw)) # credentials & host in a config file
        #print self.token_req.status_code
        self.token = self.token_req.text.split()
        self.str_token= str(self.token[1])
        self.assertEqual(self.token_req.status_code,200)
        return self.str_token


    def test_devices_imported(self):
        with open("inventory_node_request.xml") as myfile:
            self.xml_data ="".join(line.rstrip() for line in myfile)
        encoded_xml_data = urllib.quote_plus(self.xml_data)
        Config = ConfigParser.ConfigParser()
        Config.read("nccm_config.ini")
        request_url =  Config.get('NCCM URL','request_url')
        headers = {'authorization': 'Bearer ' + self.test_get_token(),'content-type': "application/x-www-form-urlencoded"}
        response = requests.post(request_url,verify=False,headers = headers,data='request='+ encoded_xml_data)
        print response.status_code
        with open ("inventory_nodes_response.xml",'w')as fw:
            fw.writelines(response.text)

        self.assertEqual(response.status_code,200)

        with open("inventory_nodes_response.xml")as fr:
            nodes = fr.readlines()

        import xml.etree.ElementTree as ET
        tree = ET.parse('inventory_nodes_response.xml')
        root = tree.getroot()
        total_nodes_imported = root[0][1].text
        print "Total devices imported = ",total_nodes_imported

        self.assertGreater(int(total_nodes_imported),60)

    def tearDown(self):
        import time
        #time.sleep(30)

if __name__ == "__main__":
    unittest.main()