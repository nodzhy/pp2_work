import psycopg2
import csv
conn = psycopg2.connect(host="localhost", port = "5432", database= "pp2", 
                        user= "postgres", password = "Nurban17."
)
cur = conn.cursor()
def inputData():
    name = input("Hello input your name: ")
    number = input("Input your phone number: ")
    cur.execute(' INSERT INTO phone_book("PersonName", "PhoneNumber") VALUES( %s, %s); ' , (name, number))

def deleteData():
    print("Which name do ypu want to delete?\n")
    personName = input()
    cur.execute(f''' DELETE FROM phone_book WHERE "PersonName"='{personName}' ''')
done = False
while not done:
    print("What do you want to do?\n\
          1. Input data from console\n\
          2. Delete data from table by person name")
    x = int(input("Enter number 1-5\n"))
    if(x == 1):
        inputData()
   
    elif(x == 2):
        deleteData()
    conn.commit()
    
cur.close()
conn.close()
# cur.execute(' DELETE FROM postgres.public.phone_book ')