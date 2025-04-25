import psycopg2
import csv

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="kot13",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

################################

def table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Breaking_bad (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            phone VARCHAR(20)
        );
    """)
    conn.commit()
    print("Table created!")


def csv_1():
    with open("C:/Users/brama/lab147/.vscode/labs/lab10/phonebook.csv", "r", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for a in reader:
            cur.execute(
                "INSERT INTO Breaking_bad (first_name, phone) VALUES (%s, %s)", (a['first_name'], a['phone'])
            )
    conn.commit()
    print("Inserted!")

def console(xw):
    while xw == "more":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        cur.execute("SELECT phone FROM Breaking_bad WHERE first_name = %s", (name,))
        l = cur.fetchone()
        if l:
            cur.execute(
                "UPDATE Breaking_bad SET phone = %s WHERE first_name = %s", (phone, name)
            )
        else:
            cur.execute(
                "INSERT INTO Breaking_bad (first_name, phone) VALUES (%s, %s)", (name, phone)
            )

        conn.commit()
        print("Ok, all right")
        while True:
            user = input("Do you want more? (yes or no): ")
            if user == "no":
                xw = 0
                break
            elif user == "yes":
                break
            else:
                print("Not valid (just yes or no)")

    print("Ok, all right")



def update():
    while True:
        i = input("Update name or phone ")
        if i == "name":
            old_name = input("old: ")
            new_name = input("new: ")
            cur.execute(
                "UPDATE Breaking_bad SET first_name = %s WHERE first_name = %s", (new_name, old_name)
            )
            conn.commit()
            break
        elif i == "phone":
            old_phone = input("old: ")
            new_phone = input("new: ")
            cur.execute(
                "UPDATE Breaking_bad SET phone = %s WHERE phone = %s", (new_phone, old_phone)
            )
            conn.commit()
            break
        else:
            print("Write (name) or (phone)")
    print("Updated!")

def search():
    while True:
        i = input("Search with using name or phone ")
        if i == "name":
            name = input("Enter name: ")
            cur.execute("SELECT * FROM Breaking_bad WHERE first_name = %s", (name,))
            break
        elif i == "phone":
            phone = input("Enter phone: ")
            cur.execute("SELECT * FROM Breaking_bad WHERE phone = %s", (phone,))
            break
        else:
            print("Write (name) or (phone)")
    all = cur.fetchall()
    for x in all:
        print(x)

def delete():
    while True:
        choice = input("Delete with using name or phone ")
        if choice == "name":
            name = input("Enter name to delete: ")
            cur.execute(
                "DELETE FROM Breaking_bad WHERE first_name = %s", (name,)
            )
            conn.commit()
            break
        elif choice == "phone":
            phone = input("Enter phone to delete: ")
            cur.execute(
                "DELETE FROM Breaking_bad WHERE phone = %s", (phone,)
            )
            conn.commit()
            break
        else:
            print("Write (name) or (phone)")
    print("Deleted!")

def clear():
    cur.execute(
        "TRUNCATE TABLE Breaking_bad RESTART IDENTITY;"
    )
    print('Cleared!')
    conn.commit()

def search_1():
    pattern = input("Enter part of name or phone to search: ")
    cur.execute("""
        SELECT * FROM Breaking_bad 
        WHERE first_name ILIKE %s OR phone ILIKE %s
    """, (f"%{pattern}%", f"%{pattern}%"))
    results = cur.fetchall()
    for r in results:
        print(r)

def output(long, begin):
    cur.execute("""
        SELECT * FROM Breaking_bad ORDER BY id LIMIT %s OFFSET %s
    """, (long, begin))
    results = cur.fetchall()
    for r in results:
        print(r)

def delete_1(value):
    cur.execute("""
        DO $$
        BEGIN
            IF EXISTS (SELECT 1 FROM Breaking_bad WHERE first_name = %s) THEN
                DELETE FROM Breaking_bad WHERE first_name = %s;
            ELSIF EXISTS (SELECT 1 FROM Breaking_bad WHERE phone = %s) THEN
                DELETE FROM Breaking_bad WHERE phone = %s;
            END IF;
        END
        $$;
    """, (value, value, value, value))
    conn.commit()
    print("Deleted by name or phone.")
while True:
        print("1.Create 2.CSV 3.Console 4.Update 5.Search 6.Delete 7.Clear 8.Search Pattern 9.Output 10.Delete by Name/Phone 11.Exit")
        option = input("Choose option: ")
        if option == "1":
            table()
        elif option == "2":
            csv_1()
        elif option == "3":
            xw = 'more'
            console(xw)
        elif option == "4":
            update()
        elif option == "5":
            search()
        elif option == "6":
            delete()
        elif option == "7":
            clear()
        elif option == "8":
            search_1()
        elif option == "9":
            long = int(input("Enter long: "))
            begin = int(input("Enter begin: "))
            output(long, begin)
        elif option == "10":
            value = input("Enter name or phone to delete: ")
            delete_1(value)
        elif option == "11":
            break
        else:
            print("Not valid")

cur.close()
conn.close()
