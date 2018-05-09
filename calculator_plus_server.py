import socket
from ast import literal_eval as make_tuple
from thread import start_new_thread as th
s=socket.socket()
id=0
def create_socket():

    s.bind(("127.0.0.1",7575))
    s.listen(1)
    while True:
            conn,addr=s.accept()
            th(listener,(id,conn))


def Calculator_plus(a,b):
    return a+b

def Calculator_tafrigh(a,b):
    return a-b

def Calculator_zarb(a,b):
    return a*b

def Calculator_taghsim(a,b):
    return a/b



def listener(id,conn):
    while True:
        data=conn.recv(100)
        if data:
            print data
            if data[0:3]=="jam":
                data=make_tuple(data[3:])
                print data
                conn.send(str(Calculator_plus(data[0],data[1])))
            if data[0:3]=="taf":
                data=make_tuple(data[3:])
                conn.send(str(Calculator_tafrigh(data[0],data[1])))
            if data[0:3]=="zar":
                data=make_tuple(data[3:])
                conn.send(str(Calculator_zarb(data[0],data[1])))
            if data[0:3]=="tag":
                data=make_tuple(data[3:])
                conn.send(str(Calculator_taghsim(data[0],data[1])))
            else:
                print "vorodi ghalat ast"
                continue
create_socket()
