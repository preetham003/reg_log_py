import mysql.connector
import hashlib

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ahex",
    database="data"
)
cursor = connection.cursor()
cursor.execute("""create table auto_inc(
               id int auto_increment primary key,
               username varchar(255) not null,
               password varchar(255) not null
)""")
username1,password1="john231",hashlib.sha256("john1234".encode()).hexdigest()
username2,password2="johnny231",hashlib.sha256("johnny1234".encode()).hexdigest()
username3,password3="ben23",hashlib.sha256("ben23".encode()).hexdigest()
username4,password4="maxx21",hashlib.sha256("maxx21".encode()).hexdigest()

try:
    cursor.execute("insert into user1(username,password) values(%s,%s)", (username1,password1))
    cursor.execute("insert into user1(username,password) values(%s,%s)",  (username2,password2))
    cursor.execute("insert into user1(username,password) values(%s,%s)",  (username3,password3))
    cursor.execute("insert into user1(username,password) values(%s,%s) ",(username4,password4))
    connection.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")


#connection.commit()