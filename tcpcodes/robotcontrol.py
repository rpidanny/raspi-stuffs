import socket
import smbus
import time


bus = smbus.SMBus(1)
address = 0x04

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

TCP_IP = '192.168.1.12'
TCP_PORT = 5010
BUFFER_SIZE = 1

while 1:
    print "Waiting For Client..."
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    conn, addr = s.accept()
    print 'Connection address:', addr

    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        #print "received data:", data
        print data
        if data == "R":
            print "right"
            writeNumber(3)
        if data == "L":
            print "left"
            writeNumber(2)
        if data == "F":
            print "Forward"
            writeNumber(1)
        if data == "B":
            print "Back"
            writeNumber(5)
        if data == "H":
            print "Stop"
            writeNumber(4)
        

    conn.close()