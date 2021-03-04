#!/usr/bin/python3
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
#    print(x[0] + ":~")

    p = subprocess.Popen(pass_arg, stdin=subprocess.PIPE, shell=False)
    p.communicate(input='\nyes\n{}\n'.format(x[1]).encode())

    p = subprocess.Popen(["scp", "-r", "/home/brianbrix/PycharmProjects/devops/test3.py", x[0] + ":~"])
    sts = os.waitpid(p.pid, 0)
    p.communicate(input='\nyes\ny\n'.encode())

    p = subprocess.Popen(["scp", "-r", "/home/brianbrix/PycharmProjects/devops/server.txt", x[0] + ":~"])
    sts = os.waitpid(p.pid, 0)
    p.communicate(input='\nyes\ny\n'.encode())

    # print(subprocess.run("ssh {} {}".format(x[0], 'bash -s {}'.format(x[2].split('/')[-1])), shell=True,
    #                  ).stdout)
#    print('sudo -S bash {}'.format(x[2].split('/')[-1]))
#    result = subprocess.run(['ssh', x[0], f"echo {x[1]} | sudo -S bash {x[2].split('/')[-1]}"]).stdout
    os_t = subprocess.check_output(["uname", "-a"]).decode()
#    print(os_t, "#################")
    result = subprocess.run(['ssh', x[0], f"echo {x[1]} | sudo -S apt install sshpass"]).stdout
    print("running python")
    result = subprocess.run(['ssh', x[0], f"python3 test3.py"]).stdout
    result = subprocess.run(['pwd']).stdout
    print(x[0], "completed")

