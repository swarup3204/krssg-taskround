# import socket programming library
import socket 
# import thread module
from _thread import *
import threading
#importing modules
import itertools,random
import pickle
import time
  
#print_lock = threading.Lock()
  
# thread function

def threaded2(c,indices):
    
    
        msg=pickle.dumps(indices)
        c.send(msg)

        time.sleep(1)

        # data received from client

        
              
            # lock released on exit
        #print_lock.release()
        #print(threading.get_ident())
        

        c.close()
  

def threaded(c,x,py_max):
    
        
        msg=pickle.dumps(x)

        c.send(msg)
        
        
        rmsg=[]

        # data received from client
        data = c.recv(1024)
        rmsg=pickle.loads(data)
        print('The value received from player ',len(py_max)+1,'is ',rmsg,' in this round')
        
        py_max.append(rmsg)

        if not data:
            print('Bye')
              
            # lock released on exit
           
           
        #print(threading.get_ident)
       
        
  
        # send back reversed string to client
        
  
    # connection closed
        c.close()
  
  
def Main():
    host = ""
  
    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
  
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    points=[0,0,0]  
    
    for i in range(1,5):

  
      # make a deck of cards
      deck = list(itertools.product(range(1,53)))
      # shuffle the cards
      random.shuffle(deck)

      j=0
      py_max=[]
      t=[]
        
    # a forever loop until client wants to exit
      for k in range(1,4):

        # establish connection with client
        
        c, addr = s.accept()
        

        x=[deck[j][0],deck[j+1][0],deck[j+2][0]]
        j+=3
        # lock acquired by client
        #print_lock.acquire()
        #print('Connected to :', addr[0], ':', addr[1])
  
        # Start a new thread and return its identifier
        time.sleep(4)

        to=threading.Thread(target=threaded,args=(c,x,py_max))
        to.start()
        t.append(to)
        
        
        
      for k in t:
            k.join()


      max_value=max(py_max)
      indices = [index for index, value in enumerate(py_max) if value == max_value]
      

      print('================Round ',i,'===============')
      print('Player ',end='')
      for k in range(len(indices)): 
            print(indices[k]+1,' ',end='')
            points[k]+=1

      print('win in this round')

      print('Points at the end of this round for each player')

      for m in range(0,3):
             print(points[i],' ',end='')
      print('')

    max_value=max(points)
    indices = [index for index, value in enumerate(points) if value == max_value]
    

    print('\n')

    print('Player ',end='')
    for k in range(len(indices)): 
            print(indices[k]+1,' ',end='')
            points[k]+=1

    print('won the game')

    for k in range(1,4):
      # establish connection with client
        c, addr = s.accept()
        # lock acquired by client
        #print_lock.acquire()
        #print('Connected to :', addr[0], ':', addr[1])
  
        # Start a new thread and return its identifier

    
        start_new_thread(threaded2,(c,indices))
        
     
           

          

    s.close()
if __name__ == '__main__':
    Main()

