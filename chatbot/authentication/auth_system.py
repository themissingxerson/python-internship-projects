import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")
conn.commit()

while True:
    print("\n1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        cur.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        conn.commit()
        print("Signup successful")

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        if cur.fetchone():
            print("Login successful")
        else:
            print("Invalid username or password")

    elif choice == "3":
        print("Exiting")
        break

    else:
        print("Invalid choice")

conn.close()
