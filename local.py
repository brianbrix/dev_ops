#!/usr/bin/env python3
import os, sys, getpass
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
import subprocess
#dir_path = os.path.dirname(os.path.realpath(file))
#parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
#sys.path.insert(0, parent_dir_path)

dix = []
with open('server.txt', 'r') as infile:
    data = infile.readlines()
    for i in data:
        if i[0] != "#":
            dix.append([x.strip() for x in i.split(",")])
for x in dix:
    pass_arg = ["sshpass", "-p", x[1], "ssh-copy-id", x[0]]

    p = subprocess.Popen(pass_arg, stdin=subprocess.PIPE, shell=False)
    p.communicate(input='\nyes\n{}\n'.format(x[1]).encode())
    #upload the pythpon and servers list to remote machine
    p = subprocess.Popen(["scp", "-r", "/home/brianbrix/PycharmProjects/devops/remote.py", x[0] + ":~"])
    sts = os.waitpid(p.pid, 0)
    p.communicate(input='\nyes\ny\n'.encode())

    p = subprocess.Popen(["scp", "-r", "/home/brianbrix/PycharmProjects/devops/server.txt", x[0] + ":~"])
    sts = os.waitpid(p.pid, 0)
    p.communicate(input='\nyes\ny\n'.encode())


    os_t = subprocess.check_output(["uname", "-a"]).decode()
#    print(os_t, "#################")
    result = subprocess.run(['ssh', x[0], f"echo {x[1]} | sudo -S apt install sshpass"]).stdout
    print("running python")
    #run python script in remote machine
    result = subprocess.run(['ssh', x[0], f"python3 remote.py"]).stdout
    result = subprocess.run(['pwd']).stdout
    print(x[0], "completed")

