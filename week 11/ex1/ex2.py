import psycopg2
import csv

conn = psycopg2.connect(host="localhost", port = "5432", database= "pp2", 
                        user= "postgres", password = "Nurban17."
)

cur = conn.cursor()

def inputData():
    name = input("Hello input your name: ")
    number = input("Input your phone number: ")
    cur.execute(' INSERT INTO insert("PersonName", "PhoneNumber") VALUES( %s, %s); ' , (name, number))

def update_contact(PersonName, PhoneNumber):
    cur.execute('UPDATE insert SET "PhoneNumber" = %s WHERE "PersonName" = %s;', (PhoneNumber, PersonName))
    conn.commit()

done = False
while not done:
    print("What do you want to do?\n\
          1. Input data from console\n\
          2. Update existing contact\n\
          3. End")
    x = int(input("Enter number 1-5\n"))
    if(x == 1):
        inputData()
    elif(x == 2):
        print("Which number do you want to update? Enter name and new number: ")
        name = input()
        newNumber = input()
        update_contact(name, newNumber)
    elif(x == 3):
        done = True
    conn.commit()
    
cur.close()
conn.close()