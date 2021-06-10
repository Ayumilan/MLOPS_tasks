import socket as so
import cv2
import pickle as p
import struct as st

print("Start video call without voice")
x = input("Enter the ip to which you want to connect: ")
print(x)

client_s = so.socket(so.AF_INET,so.SOCK_STREAM)
host_ip = x 
port = 2222
print("Socket Created")


client_s.connect((host_ip,port))
data = b""
payload_size = st.calcsize("Q")
print("Socket Accepted")


while True:
    while len(data) < payload_size:
        packet = client_s.recv(2160) 
        if not packet: break
        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = st.unpack("Q",packed_msg_size)[0]
    
    while len(data) < msg_size:
        data += client_s.recv(2160)
    frame_data = data[:msg_size]
    data  = data[msg_size:]
    frame = p.loads(frame_data)
    cv2.imshow("RECEIVING VIDEO",frame)
    key = cv2.waitKey(1) & 0xFF
    if key  == ord('q'):
        break
client_s.close()

print("THANK YOU ALL")
