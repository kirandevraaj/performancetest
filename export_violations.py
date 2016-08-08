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



class Export_Violations(unittest.TestCase):
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

    def test_read_policy_profile_response(self):
        #print self.str_token
        with open("execute_policy_profile_response.xml")as fr:
             file_read = fr.readlines()
            #print file_read
        import xml.etree.ElementTree as ET
        tree = ET.parse('execute_policy_profile_response.xml')
        root = tree.getroot()
        #print root
        self.audit_handle = root[0][0].text

        print "Audit handle of policy profile response",self.audit_handle
        return self.audit_handle
        #print "Total devices imported = ",total_nodes_imported
        #self.assertGreater(int(total_nodes_imported),60)

    def test_replace_audit_handle_in_export_violations(self):
        handle = self.test_read_policy_profile_response()
        with open("export_violations.xml")as fr:
             file_read = fr.readlines()
        import xml.etree.ElementTree as ET
        tree = ET.parse('export_violations.xml')
        root = tree.getroot()
        k= root.iter("Value")
        l = k.next()
        p= l.text
        print p

        tree = etree.parse('export_violations.xml')
        for j in tree.findall('.//Value'):
            print "JJJJJJJJJJJJJJ",j.text
            j.text = self.audit_handle
        with open('export_violations.xml', 'w') as file_handle:
            file_handle.write(etree.tostring(tree, pretty_print=True, encoding='utf8'))
            print "Input Request File Updated !!"

    def tearDown(self):
        time.sleep(20)
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)

