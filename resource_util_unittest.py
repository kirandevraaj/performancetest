import unittest
import requests
import urllib
import xml.dom.minidom
import os
import HTMLTestRunner
import spur
import paramiko
import subprocess
import csv
import time
import ConfigParser

class TestResourceUtil(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        Config = ConfigParser.ConfigParser()
        Config.read("nccm_config.ini")
        self.server_ip =  Config.get('NCCM Server Details','Server IP')
        self.user_name = Config.get('NCCM Server Details','username')
        self.passw = Config.get('NCCM Server Details','password')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server_ip, username=self.user_name, password=self.passw)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
        #print type(ssh_stdout)
        #print ssh_stdout.readlines()

    def test_pari_process_id(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server_ip, username=self.user_name, password=self.passw)
        #cmd = ["pgrep","pari_server"]
        #pid = subprocess.Popen([cmd[0],cmd[1]],stdout=subprocess.PIPE)
        #pid_output, err = pid.communicate()
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('pgrep pari_server')
        #cmd = ["pgrep","pari_server"]
        self.k= ssh_stdout.readlines()
        return self.k

    def test_res_cpu_mem(self):
        k = TestResourceUtil.test_pari_process_id(self)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server_ip, username=self.user_name, password=self.passw)
        new_k = k[0].replace("\n",'')
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ps -p '+ new_k + ' -o %mem,%cpu')
        list = ssh_stdout.readlines()
        print "Resource Utilisation=", list
        list1 = list[0]
        x= list1.split()
        list2 = list[1].replace('  ',' ')
        y= list2.split()
        for i in range(1):
            (q,w) = (x[i],y[i])
        prac = (q,w)
        d1= dict([prac])
        print d1
        for i in range(2):
            (q,w) = (x[i],y[i])
            prac = (q,w)
            d2= dict([prac])
        print d2
        d3 = dict(d1,**d2)
        print d3
        with open('performance.csv', 'a') as f:  # Just use 'w' mode in 3.x
            w = csv.DictWriter(f, d3.values())
            w.writeheader()

            #w.writerow(d3)

    def test_thread_count(self):
        k = TestResourceUtil.test_pari_process_id(self)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server_ip, username=self.user_name, password=self.passw)
        #ssh.connect("10.76.155.67", username="collectorlogin", password="Cisco@321")
        new_k = k[0].replace("\n",'')
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ps huH p " + new_k + " | wc -l")
        thread =  ssh_stdout.readlines()
        thread_count = thread[0].replace("\n",'')
        print "Thread Count = ",thread_count

suite = unittest.TestLoader().loadTestsFromTestCase(TestResourceUtil)


while True:
    unittest.TextTestRunner(verbosity=2).run(suite)
    time.sleep(10)


