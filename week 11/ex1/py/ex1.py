import psycopg2 as pgsql

connection = pgsql.connect(host="localhost", dbname="pp2", user="postgres", 
                           password="Nurban17.", port=5432)
cur = connection.cursor()

def createpattern():
    global query
    query = """SELECT * FROM PhoneBook
    WHERE """
    print(r"Do you want to search by surname(0)/name(1)/break(any num) enter the number:")
    mode = int(input())
    if mode == 0:
        query += "surname"
        print("Enter string")
        substr = input()
        print("""Select option:
        1-surname is equal to string
        2-surname starts with the string
        3-surname ends with the string
        4-surname contains the string""")
        mode1 = int(input())
        if mode1 == 1:
            query += "='{}'".format(substr)
        elif mode1 == 2:
            query += " iLIKE '{}%'".format(substr)
        elif mode1 == 3:
            query += " iLIKE '%{}'".format(substr)
        else:
            query += " iLIKE '%{}%'".format(substr)
    elif mode == 1:
        query += """name"""
        print("Enter string")
        substr = input()
        print("""Select option:
        1-name is equal to string
        2-name starts with the string
        3-name ends with the string
        4-name contains the string""")
        mode1 = int(input())
        if mode1 == 1:
            query += "='{}'".format(substr)
        elif mode1 == 2:
            query += " iLIKE '{}%'".format(substr)
        elif mode1 == 3:
            query += " iLIKE '%{}'".format(substr)
        else:
            query += " iLIKE '%{}%'".format(substr)
    else:
         return "error"
    return query

s1 = createpattern()
if s1 != "error":
    cur.execute(s1 + ";")
    print(cur.fetchall())

cur.close()
connection.close()
