""""
Thisfile is run in every remote node that is listed in the server.txt
"""
import os
import subprocess
import getpass

dix = []
with open('server.txt', 'r') as infile:
    data = infile.readlines()
    for i in data:
        if i[0] != "#":
            dix.append([x.strip() for x in i.split(",")])

c_p = "/home/{}/.ssh".format(getpass.getuser())
if not os.path.exists(c_p):
    os.makedirs(c_p)

os.chdir(c_p)

pass_arg = ["ssh-keygen", "-P", ""]

p = subprocess.Popen(pass_arg, stdin=subprocess.PIPE, shell=False)
p.communicate(input='\ny'.encode())

p = subprocess.Popen('echo "StrictHostKeyChecking no" >> config', shell=True)
p.communicate(input='\n'.encode())
try:
    pass_arg = ["rm", "known_hosts"]
    p = subprocess.Popen(pass_arg, stdin=subprocess.PIPE, shell=False)
    p.communicate(input='\n'.encode())
except:
    pass

pass_arg = "chmod go-w ~"
p = subprocess.Popen(pass_arg, stdin=subprocess.PIPE, shell=True)
p.communicate(input='\n'.encode())

for x in dix:
    ipAddr = subprocess.check_output(["hostname", "-I"]).decode()
    print(ipAddr)
    # this is to avoid running sshpass and ssh-copy-id in the current node itself
    if x[0].split("@")[1] in ipAddr:
        print(x[0].split("@"), "xxxxxx")
        continue
    else:
        print("shamsham")
        print(x[0].split("@"), "@@@@@")
        p = subprocess.Popen(f"sshpass -p {x[1]} ssh-copy-id {x[0]}", shell=True)
        ts = os.waitpid(p.pid, 0)

        print(p, "hhhhh")
