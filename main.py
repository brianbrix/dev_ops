import os
import subprocess

dix = []
with open('server.txt', 'r') as infile:
    data = infile.readlines()
    for i in data:
        print(i.split(","))
        if i[0] != "#":
            dix.append([x.strip() for x in i.split(",")])
print(dix)
for x in dix:
    print(x)
    pass_arg = ["sshpass", "-p", x[1], "ssh-copy-id", x[0]]
    print(x[0] + ":~")

    subprocess.call(pass_arg)
    print("Free")
    subprocess.call(["chmod", "+x", x[2]])
    p = subprocess.Popen(["scp", "-r", x[2], x[0] + ":~"])
    sts = os.waitpid(p.pid, 0)
    # print(subprocess.run("ssh {} {}".format(x[0], 'bash -s {}'.format(x[2].split('/')[-1])), shell=True,
    #                  ).stdout)
    print('sudo -S bash {}'.format(x[2].split('/')[-1]))
    result = subprocess.run(['ssh', x[0], f"echo {x[1]} | sudo -S bash {x[2].split('/')[-1]}"]).stdout
    print(result)
    print(f"completed: {x[0]}")