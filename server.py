import mysql.connector
import hashlib
import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",9999))
server.listen()

def handle(c):
    c.send("username: ".encode())
    username=c.recv(1024).decode()
    c.send("password: ".encode())
    password=c.recv(1024)
    password=hashlib.sha256(password).hexdigest()


    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ahex",
        database="data"
    )
    cursor=connection.cursor()
    cursor.execute("select * from user6 where username=%s and password=%s", (username,password))
    
    if cursor.fetchall():
        c.send("Login Successful!!".encode())
    else:
        c.send("Login Failed!!".encode())

while True:
    client,addr=server.accept()
    threading.Thread(target=handle,args=(client,)).start()