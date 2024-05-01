import psycopg2

conn = psycopg2.connect(host="localhost", port = "5432", database= "test2", 
                        user= "postgres", password = "Nurban17."
                        )

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person (
            id INT PRIMARY KEY, 
            name VARCHAR(255),
            age INT, 
            gender CHAR
);
""")

cur.execute("""INSERT INTO person (id, name, age, gender) VALUES 
            (1, 'Mike', 30, 'm'),
            (2, 'Lisa', 17, 'f'),
            (3, 'Alina', 18, 'f'),
            (4, 'nur', 18, 'm'),
            (5, 'Nana', 45, 'f');
            """)

conn.commit() 

cur.close() 
conn.close()
