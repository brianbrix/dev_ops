import os
import subprocess
import getpass

dix = []
with open('server.txt', 'r') as infile:
    data = infile.readlines()
    for i in data:
        # print(i.split(","))
        if i[0] != "#":
            dix.append([x.strip() for x in i.split(",")])

c_p = "/home/{}/.ssh".format(getpass.getuser())
if not os.path.exists(c_p):
    os.makedirs(c_p)
# if not os.path.exists("~/.ssh"):
#     os.makedirs("~/.ssh")

os.chdir(c_p)

# pass_arg = ["touch", f"{c_p}/authorized_keys"]
# subprocess.run(pass_arg, stdin=subprocess.PIPE, shell=False)
# pass_arg = ["touch", f"{c_p}/id_rsa.pub"]
# subprocess.run(pass_arg, stdin=subprocess.PIPE, shell=False)

# pass_arg = ["chmod", "600", f"{c_p}/authorized_keys"]
# subprocess.run(pass_arg, stdin=subprocess.PIPE, shell=False)
#
# pass_arg = ["chmod", "600", f"{c_p}/id_rsa"]
# subprocess.run(pass_arg, stdin=subprocess.PIPE, shell=False)

pass_arg = ["ssh-keygen", "-P", ""]

p = subprocess.Popen(pass_arg, stdin=subprocess.PIPE, shell=False)
p.communicate(input='\ny'.encode())

# pass_arg = ["cp", "id_rsa.pub", "authorized_keys"]
# p = subprocess.Popen(pass_arg, stdin=subprocess.PIPE, shell=False)
# p.communicate(input='\n'.encode())

# pass_arg = ["cp", "id_rsa.pub", "authorized_keys2"]
# p = subprocess.Popen(pass_arg, stdin=subprocess.PIPE, shell=False)
# p.communicate(input='\n'.encode())

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
    if x[0].split("@")[1] in ipAddr:
        print(x[0].split("@"), "xxxxxx")
        continue
    else:
        # pass_arg = ["sshpass", "-p", x[1], "ssh-copy-id", x[0]]
        # print(x[0] + ":~")
        print("shamsham")
        print(x[0].split("@"), "@@@@@")
        p = subprocess.Popen(f"sshpass -p {x[1]} ssh-copy-id {x[0]}", shell=True)
        ts = os.waitpid(p.pid, 0)

        print(p, "hhhhh")