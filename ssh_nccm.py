import spur
import paramiko

'''
shell = spur.SshShell(hostname="10.76.155.67", username="collectorlogin", password="Cisco@321")
result = shell.run(["echo", "-n", "hello"])
print result.output # prints c
'''


ssh = paramiko.SSHClient()
#ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.76.155.67", username="collectorlogin", password="Cisco@321")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
print type(ssh_stdin)
print ssh_stdout.readlines()

