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

def console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute(
        "INSERT INTO Breaking_bad (first_name, phone) VALUES (%s, %s)", (name, phone)
    )
    conn.commit()
    print("Inserted!")

def update():
    i = input("Update name or phone ")
    if i == "name":
        old_name = input("old: ")
        new_name = input("new: ")
        cur.execute(
            "UPDATE Breaking_bad SET first_name = %s WHERE first_name = %s", (new_name, old_name)
        )
    elif i == "phone":
        old_phone = input("old: ")
        new_phone = input("new: ")
        cur.execute(
            "UPDATE Breaking_bad SET phone = %s WHERE phone = %s", (new_phone, old_phone)
        )
    conn.commit()
    print("Updated!")

def search():
    i = input("Search with using name or phone ")
    if i == "name":
        name = input("Enter name: ")
        cur.execute("SELECT * FROM Breaking_bad WHERE first_name = %s", (name,))
    elif i == "phone":
        phone = input("Enter phone: ")
        cur.execute("SELECT * FROM Breaking_bad WHERE phone = %s", (phone,))
    all = cur.fetchall()
    for x in all:
        print(x)

def delete():
    choice = input("Delete with using name or phone ")
    if choice == "name":
        name = input("Enter name to delete: ")
        cur.execute(
            "DELETE FROM Breaking_bad WHERE first_name = %s", (name,)
        )
    elif choice == "phone":
        phone = input("Enter phone to delete: ")
        cur.execute(
            "DELETE FROM Breaking_bad WHERE phone = %s", (phone,)
        )
    conn.commit()
    print("Deleted!")

while True:
        print("1.Create 2.CSV 3.Console 4.Update 5.Search 6.Delete 7.Exit")
        option = input("Choose option: ")
        if option == "1":
            table()
        elif option == "2":
            csv_1()
        elif option == "3":
            console()
        elif option == "4":
            update()
        elif option == "5":
            search()
        elif option == "6":
            delete()
        elif option == "7":
            break
        else:
            print("NOT VALID")

cur.close()
conn.close()
