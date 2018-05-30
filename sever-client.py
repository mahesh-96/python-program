#server
# TCP Server Code
 
#host="127.0.0.1"               
host="127.168.2.75" 
port=4446               

from socket import *            
s=socket(AF_INET, SOCK_STREAM)
s.bind((host,port))             
                                        
s.listen(1)         
                                            
print ("Listening for connections.. ")
q,addr=s.accept()               
                                        
data=raw_input("Enter data to be send:  ")
                                            
q.send(data)                        
s.close()
# End of code

#Client
# TCP Client Code
 
#host="127.0.0.1"            

host = "127.168.2.75"
port=4446               
 
from socket import *        
 
s=socket(AF_INET, SOCK_STREAM)      
s.connect((host,port))          
 
msg=s.recv(1024)            
 
print ("Message from server : " + msg.strip().decode('ascii'))
 
s.close()                           
# End of code
