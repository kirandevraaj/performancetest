import subprocess
import os
import datetime

def my_func(cmd):
        pid = subprocess.Popen([cmd[0],cmd[1]],stdout=subprocess.PIPE)
        pid_output, err = pid.communicate()
        return pid_output

cmd = ["pgrep","pari_server"]
k = my_func(cmd)

def res(a):
        res_util = subprocess.Popen([a[0],a[1],a[2],a[3],a[4]],stdout=subprocess.PIPE)
        res_output, err = res_util.communicate()
        with open("resource_util.txt", "a")as f:
                f.write(datetime.datetime.now().ctime()+'\n')
        with open("resource_util.txt",'a') as f:
                f.writelines(res_output)
                f.close()


new_k = k.replace("\n",'')
a = ["ps", "-p" ,new_k ,"-o", "%cpu,%mem,cmd"]
res(a)


def thread_c():
        cmd = "ps huH p " + mod_k + " | wc -l"
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output = ps.communicate()[0]
        with open("resource_util.txt",'a') as f:
                f.writelines("current thread count: " + output+'\n')
                f.close()

mod_k = k.replace("\n",'')
thread_c()