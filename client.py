import socket
import hashlib

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

while True:
    # Receive and print the menu options
    menu_options = client.recv(1024).decode()
    print(menu_options)

    # Choose an option (1 for login, 2 for register, 3 for exit)
    choice = input("Enter your choice: ")
    client.send(choice.encode())

    if choice == "1" or choice == "2":
        # Login or Register
        message = client.recv(1024).decode()
        username = input(message)
        client.send(username.encode())

        message = client.recv(1024).decode()
        password = hashlib.sha256(input(message).encode()).hexdigest()
        client.send(password.encode())

        result = client.recv(1024).decode()
        print(result)

    elif choice == "3":
        # Exit the loop
        break

    else:
        print("Invalid choice.")

client.close()
