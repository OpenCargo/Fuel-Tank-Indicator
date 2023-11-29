import socket

def udp_listener(update_function_args):
    update_function, *args = update_function_args
    UDP_IP = "192.168.1.17"
    UDP_PORT = 12345

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        decoded_data = data.decode()
        update_function(*args, decoded_data)



