"""
    http测试
"""


from socket import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8006))
s.listen(3)


c,addr = s.accept()
print("connect from",addr)

data = c.recv(1024)
print(data.decode())

msg = """HTTP/1.1 200 OK
Content-Type:text/html

<h1>hello world</h1>
"""
c.send(msg.encode())

c.close()
s.close()