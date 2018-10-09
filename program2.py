import mysql.connector
import sys 
import getopt
import datetime
global conn,cursor;

conn = mysql.connector.connect(host="localhost", user="root",password="root")



def connection():
    
    if conn.is_connected():
        return True
    else:
        return False

def create_database():
    if connection():
        mycursor = conn.cursor()
        try:
            mycursor.execute("CREATE DATABASE db_adarsh")
            print("\nDatabase 'db_adarsh' created \n")
        except:
            print("\nDatabase 'db_adarsh' already exists \n")
    else:
        print("\n Error in creating data base \n")


def create_table():
    conn_db = mysql.connector.connect(host="localhost", db="db_adarsh", user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()
        try:
            mycursor.execute("CREATE TABLE info(id INT(10) PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), dob DATE)")
            print("\n Table has been created\n")
        except:
            print("\n table already exists \n")
    else:
        print("\n Could not connect to mysql server \n")

    conn_db.close()


def insert_values():
    conn_db = mysql.connector.connect(host="localhost", db="db_adarsh", user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()

        sql = "INSERT INTO info (id, fname, lname, dob) VALUES (%s, %s, %s, %s)"

        id = input("Enter id\n")
        fname = input("Enter first name\n")
        lname = input("Enter lastname\n")
        dob = input("Enter dob ( yyyy-mm-dd )\n")

        if not valid_date(dob):
           exit();


        val = (id, fname, lname, dob)
        try:
            mycursor.execute(sql, val)
            conn_db.commit()
            print("\n Insertion Successful \n")

        except:
            print("\n Could not insert the values \n")
    else:
        print("\n Could not connect to mysql server \n")
    conn_db.close()



def alter_table():
    conn_db = mysql.connector.connect(host="localhost", db="db_adarsh", user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()

        col = input("Enter column name\n")
        sql = "ALTER TABLE reg_no add %s VARCHAR(255)" % (col)

        try:
            mycursor.execute(sql)
            conn_db.commit()
            print("\n column added to table Successful \n")

        except:
            print("\n column already present in the table \n")
    else:
        print("\n Could not connect to mysql server \n")
    conn_db.close()


def truncate_table():
    conn_db = mysql.connector.connect(host="localhost", db="db_adarsh", user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()

        sql = "DROP TABLE info"
        try:
            mycursor.execute(sql)
            conn_db.commit()

            print("\ntable deleted Successfully \n")

        except:
            print("\n err could not delete table \n")
    else:
        print("\n Error: Could not connect to mysql server \n")
    conn_db.close()


def display_values():
    conn_db = mysql.connector.connect(host="localhost", db="db_adarsh", user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()

        try:
            mycursor.execute("SELECT * FROM info")
            myresult = mycursor.fetchall()
            for x in myresult:
              print(x)

        except:
            print("\n No table is present \n")
    else:
        print("\n Could not connect to mysql server \n")
    conn_db.close()

def valid_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True;
    except ValueError:
        return False

def main():
    while True:


        print("\nEnter your choice::\n")
        print("Create database- 1:")
        print( "Create table- 2:")
        print("Insert values- 3:")
        print("Display table values- 4:")
        print("Alter table 5:")
        print("Trucate table- 6:")
        print("Quit- q:\n")

        choice = input("Enter the option:")


        if choice == '1':
            create_database()
        if choice == '2':
            create_table()
        if choice == '3':
            insert_values()
        if choice == '4':
            display_values()    
        if choice == '5':
            alter_table()
        if choice == '6':
            truncate_table()
        if choice == 'q':
            sys.exit()
        



if __name__ == "__main__":
    main();
