# import os

# def Connect():
#     listok = []
#     listok.append(os.system('cmd /c "netsh wlan show networks"'))
#     name_of_router = 'Narkodispanse'
#     os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')

# try:

#     Connect()

# except print():
#     print("Не получилось!")
#     Connect()

#Connects the the desired WiFi network.    

from subprocess import Popen, PIPE, STDOUT
def connect_to_network(name):

    try:
        Network = Popen('netsh wlan connect ' + str(name), shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
        password = "password"
        Network.communicate(input=password.encode('utf-8'))
        print("Connected")
        Network.stdin.close()
        
    except:
        print("No connection")
    

    #Putty = Application(backend="uia").start('putty.exe -raw 192.168.1.1')

connect_to_network("Narkodispanser")