import psycopg2
import csv
conn = psycopg2.connect(host="localhost", port = "5432", database= "pp2", 
                        user= "postgres", password = "Nurban17."
)
cur = conn.cursor()
def inputData():
    name = input("Hello input your name: ")
    number = input("Input your phone number: ")
    cur.execute(' INSERT INTO deleter("PersonName", "PhoneNumber") VALUES( %s, %s); ' , (name, number))

def deleteData():
    print("Which name do ypu want to delete?\n")
    personName = input()
    cur.execute(f''' DELETE FROM deleter WHERE "PersonName"='{personName}' ''')

def deleteNum():
    print("Which num do ypu want to delete?\n")
    personNum = input()
    cur.execute(f''' DELETE FROM deleter WHERE "PhoneNumber"='{personNum}' ''')
done = False
while not done:
    print("What do you want to do?\n\
          1. Input data from console\n\
          2. Delete data from table by person name\n\
          3. Delete data from table by person num")
    x = int(input("Enter number 1-3\n"))
    if(x == 1):
        inputData()
   
    elif(x == 2):
        deleteData()

    elif(x == 3):
        deleteNum()
    conn.commit()
    
cur.close()
conn.close()
# cur.execute(' DELETE FROM postgres.public.phone_book ')