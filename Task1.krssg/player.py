# Import socket module
import socket,pickle
  



def Main():
    # local host IP '127.0.0.1'
    host = '127.0.0.1'
  
    # Define the port on which you want to connect
    port = 12345
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  
    # connect to server on local computer
    s.connect((host,port))
  
    
    while True:
  
        # message sent to server
        #s.send(message.encode('ascii'))
  
        # messaga received from server
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  
        # connect to server on local computer
        s.connect((host,port))
        data = s.recv(1024)
        msg=pickle.loads(data)

        y=list(msg)
        
        for i in range(0,3):
          
           if(13<msg[i]<27):
             y[i]-=13

           elif(26<msg[i]<40):
             y[i]-=26

           elif(39<msg[i]):
             y[i]-=39

        print('The cards that you got are of value ',end='')
        for i in range(0,3):
            print(y[i],' ',end='')
        print('')

        max_value=max(y)
        rmsg=[]

        rmsg=pickle.dumps(max_value)

        s.send(rmsg)
  
        
        ans = input('\nDo you want to continue(y/n) :')

        s.close()

        if ans == 'y':
            continue
        else:
            break

    

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  
    # connect to server on local computer
    s.connect((host,port))

    data = s.recv(1024)
    msg=pickle.loads(data)

    print('Player ',end='')

    for i in range(len(msg)):
        print(msg[i]+1,' ',end='')

    print('won the game')
        
    s.close()


if __name__ == '__main__':
    Main()

       