import socket
s=socket.socket()
s.connect(("127.0.0.1",7575))


while True:

    f=int(input("braye jam adad 1 braye tafrigh 2 braye zarb 3 braye taghsim 4 ra vared konid:: "))
    if f == 1:
        a=int(input("adad aval ra vared konid::"))
        print type (a)
        b=int(input("adad dovom ra vared konid::"))
        data="jam(%d ,%d)" %(a,b)
        s.send(data)
    if f == 2:
        a=int(input("adad aval ra vared konid::"))

        b=int(input("adad dovom ra vared konid::"))

        data="taf(%d,%d)"%(a,b)
        s.send(data)
    if f == 3:
        a=int(input("adad aval ra vared konid::"))
        b=int(input("adad dovom ra vared konid::"))
        data="zar(%d,%d)"%(a,b)
        s.send(data)
    if f == 4:
        a=int(input("adad aval ra vared konid::"))
        b=int(input("adad dovom ra vared konid::"))
        data="tag(%d,%d)"%(a,b)
        s.send(data)
    else:
        pass
    #except:
        #pass
            #print "vorodi ghalat ast"
            #continue

    print s.recv(100)
