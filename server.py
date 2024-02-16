import mysql.connector
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

def handle(c):
    while True:
        # Receive choice (login, register, or exit)
        c.send("Choose an option:\n1. Login\n2. Register\n3. Exit\n".encode())
        choice = c.recv(1024).decode()

        if choice == "1":
            # Login
            c.send("Username: ".encode())
            username = c.recv(1024).decode()
            c.send("Password: ".encode())
            password = c.recv(1024).decode()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="ahex",
                database="data"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM user6 WHERE username=%s AND password=%s", (username, hashed_password))

            if cursor.fetchall():
                c.send("Login Successful!".encode())
            else:
                c.send("Login Failed!".encode())

        elif choice == "2":
            # Register
            c.send("Username: ".encode())
            username = c.recv(1024).decode()
            c.send("Password: ".encode())
            password = c.recv(1024).decode()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="ahex",
                database="data"
            )
            cursor = connection.cursor()

            try:
                cursor.execute("INSERT INTO user6 (username, password) VALUES (%s, %s)", (username, hashed_password))
                connection.commit()
                c.send("Registration Successful!".encode())
            except mysql.connector.Error as err:
                c.send(f"Registration Failed: {err}".encode())

        elif choice == "3":
            # Exit the loop
            break

        else:
            c.send("Invalid choice.".encode())

while True:
    client, addr = server.accept()
    threading.Thread(target=handle, args=(client,)).start()
