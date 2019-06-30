import socket
import time
import io
HOST = '104.154.120.223'
PORT = 8085


def Solver(serverIn, key):
    if('enter the key' in serverIn):
          return(key, key)
    else:
        temp = serverIn[(serverIn.find('cipher:')+ 8):serverIn.find('\n')]
        temp = temp.split(' ')
        outlist = ''
        for item in temp:
            if(len(item) == 8):
                outlist += item[1]
            elif(len(item) == 11):
                if(ord(item[-1]) > 64 and ord(item[-1]) < 91):
                    outlist += item[-4]
                else:
                    outlist += item[3]
            else:
                outlist += item[-1]
        print(outlist)
        return('2', outlist)



def tcp_client():
    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    client.connect(( HOST, PORT ))
    response = client.recv(4096)
    #print(response + '\n\n\n')
    key = ''
    temp = 0
    with open('chaosLog.txt', 'a') as loggg:
        while 1:
            #time.sleep(.5)
            response = client.recv(4096)
            texty, key = Solver(response, key)
            loggg.write('The:\n' + response+ '\n\n\n'+key+'\n\n\n')
            time.sleep(2)
            print('\nTHe length:\n'+ str(len(texty)) +'\n\n\n')
            client.send(texty)

#38

if __name__ == '__main__':
    tcp_client()