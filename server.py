import socket as so
import cv2
import pickle as p
import struct as st


server_s = so.socket(so.AF_INET,so.SOCK_STREAM)
host_name  = so.gethostname()
host_ip = so.gethostbyname(host_name)
print('HOST IP:',host_ip)

port = 2222
s_address = (host_ip,port)
print("Socket Created Successfully")


server_s.bind(s_address)
print("Socket Bind Successfully")



server_s.listen(5)
print("LISTENING AT:",s_address)

print("Socket Accept")

while True:
    client_s,addr = server_s.accept()
    print('GOT CONNECTION FROM:',addr)
    if client_s:
        vid = cv2.VideoCapture(0)
        
        while(vid.isOpened()):
            img,frame = vid.read()
            a = p.dumps(frame)
            message = st.pack("Q",len(a))+a
            client_s.sendall(message)
            
		
            cv2.imshow('TRANSMITTING VIDEO',frame)
            key = cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                client_s.close()

print("THANK YOU ALL")
