import socket
import time

UDP_IP = "192.168.1.17"
UDP_PORT = 12346

def send_udp_packet(number):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = str(number).encode()
    sock.sendto(message, (UDP_IP, UDP_PORT))
    sock.close()

counter = 10

while True:
    send_udp_packet(counter)
    counter += 1
    time.sleep(10)
