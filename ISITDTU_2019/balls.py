import socket
import time
import io

HOST = '34.68.81.63'
PORT = 6666
DATA = '1,2,3,4 5,6,7,8'
init = '1,2,3,4 5,6,7,8'


#THIS IS FOR THE OPTION 1
one = '6,7,8 9,10,11'
oneBalance = '11 12'

oneHeavy = '9 10'
oneHLeft = '9'
oneHRight = '10'

oneLight = '9 10'
oneLLeft = '10'
oneLRight = '9'
########################



#THIS IS FOR OPTION 2
two = '1,2,5 3,6,12'
twoBalance = '7 8'
twoBBalance = '4'
twoBLeft = '7'
twoBRight = '8'



twoHeavy = '1 2'
twoHBalance = '4'
twoHLeft = '1'
twoHRight = '2'

twoLight = '3 12'
twoLBalance = '5'
twoLLeft = '3'
twoLRight = '3'



#######################

#THIS IS FOR OPTION 3
three = '5,6,1 7,2,12'
threeBalance = '3 4'
threeBBalance = '8'
threeBLeft = '3'
threeBRight = '4'


threeHeavy = '5 6'
threeHBalanced = '2'
threeHLeft = '5'
threeHRight = '6'

threeLight = '7 12'



def runProg(inny, level):
    #BASED ON THE RESULTS OF THE THIRD WEIGH, CHOOSE BALL
    if(int(str(level)[-1]) > 0.0):
        if(level == 1.1):
            return('12', 0.0)
        elif(level == 1.2):
            if('equally' in inny or 'balanced' in inny):
                return('11', 0.0)
            elif('heavier' in inny):
                return('9', 0.0)
            else:
                return('10', 0.0)
        elif(level == 1.3):
            if('equally' in inny or 'balanced' in inny):
                return('11', 0.0)
            if('lighter' in inny):
                return('9', 0.0)
            else:
                return('10', 0.0)
        elif(level == 2.1):
            if('equally' in inny or 'balanced' in inny):
                return('4', 0.0)
            if('heavier' in inny):
                return('7', 0.0)
            else:
                return('8', 0.0)
        elif(level == 2.2):
            if('equally' in inny or 'balanced' in inny):
                return('6', 0.0)
            if('lighter' in inny):
                return('1', 0.0)
            else:
                return('2', 0.0)
        elif(level == 2.3):
            if('equally' in inny or 'balanced' in inny):
                return('5', 0.0)
            else:
                return('3', 0.0)
        elif(level == 3.1):
            if('equally' in inny or 'balanced' in inny):
                return('8', 0.0)
            if('heavier' in inny):
                return('3', 0.0)
            else:
                return('4', 0.0)
        elif(level == 3.2):
            if('equally' in inny or 'balanced' in inny):
                return('2', 0.0)
            if('lighter' in inny):
                return('5', 0.0)
            else:
                return('6', 0.0)
        elif(level == 3.3):
            if('equally' in inny or 'balanced' in inny):
                return('1', 0.0)
            else:
                return('7', 0.0)
    else:
        #FIRST WEIGH
        if('1' in inny[-13:]):
            return(init, 10.0)
        #BASED ON RESULT OF FIRST WEIGH, CHOOSE SECOND
        #'2' in inny[-13:]
        elif(level == 10.0):
            if('equally' in inny or 'balanced' in inny):
                return(one, 1.0)
            elif('lighter' in inny):
                return(two, 2.0)
            else:
                return(three, 3.0)
        #BASED ON RESULTS OF SECOND WEIGH, CHOOSE THIRD
        #'3' in inny[-13:]
        elif(level > 0.0):
            if(level == 1.0):
                if('equally' in inny or 'balanced' in inny):
                    return(oneBalance, 1.1)
                elif('lighter' in inny):
                    return(oneHeavy, 1.2)
                else:
                    return(oneLight, 1.3)
            if(level == 2.0):
                if('equally' in inny or 'balanced' in inny):
                    return(twoBalance, 2.1)
                elif('lighter' in inny):
                    return(twoHeavy, 2.2)
                else:
                    return(twoLight, 2.3)
            else:
                if('equally' in inny or 'balanced' in inny):
                    return(threeBalance, 3.1)
                elif('lighter' in inny):
                    return(threeHeavy, 3.2)
                else:
                    return(threeLight, 3.3)


listOuut = []
def tcp_client():
    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    client.connect(( HOST, PORT ))
    response = client.recv(4096)
    #print(response + '\n\n\n')
    level = 10.0
    with open('testThisShit.txt', 'a') as loggg:
        while 1:
            time.sleep(.5)
            response = client.recv(4096)
            if(len(response) > 1):
                loggg.write('BEFORE RESPONSE############\n'+ response + "\nLevel: "+ str(level) +"\nEND BEFORE RESPONSE######\n\n\n")
                outt, level = runProg(response, level)
                loggg.write("The program's choice: "+ outt + '\n\n\n\n\n\n')
                client.send(outt)
                #client.send()
                
                print(response)

if __name__ == '__main__':
    tcp_client()


