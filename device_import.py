import unittest
import requests
import urllib
import xml.dom.minidom
import os
import HTMLTestRunner
import ConfigParser
import time
import xml.etree.ElementTree as ET
from xml.dom import minidom
from lxml import etree
from random import randint


class TestDeviceImport(unittest.TestCase):
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

    def test_import_virtual_devices(self):
        with open("import_virtualdevice_request.xml") as myfile:
            self.xml_data ="".join(line.rstrip() for line in myfile)
        encoded_xml_data = urllib.quote_plus(self.xml_data)
        Config = ConfigParser.ConfigParser()
        Config.read("nccm_config.ini")
        request_url =  Config.get('NCCM URL','request_url')
        headers = {'authorization': 'Bearer ' + self.test_get_token(),'content-type': "application/x-www-form-urlencoded"}
        response = requests.post(request_url,verify=False,headers = headers,data='request='+ encoded_xml_data)
        #print response.status_code
        print response.text
        return response.text # getting xml response
        self.assertEqual(self.response.status_code,200)

    def test_verify_nccm_devices_imported(self):
        tree = etree.parse('inventory_node_request.xml')
        for j in tree.findall('.//SessionId'):
            print "JJJJJJJJJJJJJJ", j.text
            j.text = str((randint(0,9000000)))
        with open('inventory_node_request.xml', 'w') as file_handle:
            file_handle.write(etree.tostring(tree, pretty_print=True, encoding='utf8'))
            print "Input Request File Updated !!"

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
        time.sleep(120)

