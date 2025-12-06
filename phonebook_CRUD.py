import sqlite3

def main():
    # Connect to the database
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    while True:
        # Display menu
        print("\nPhonebook Menu")
        print("1. Add a new entry")
        print("2. Look up a phone number")
        print("3. Update a phone number")
        print("4. Delete an entry")
        print("5. Display all entries")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_entry(cur)
        elif choice == '2':
            lookup_entry(cur)
        elif choice == '3':
            update_entry(cur)
        elif choice == '4':
            delete_entry(cur)
        elif choice == '5':
            display_entries(cur)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1-6.")

        conn.commit()

    conn.close()


def add_entry(cur):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    try:
        cur.execute("INSERT INTO Entries (Name, PhoneNumber) VALUES (?, ?)", (name, phone))
        print(f"Added entry: {name} - {phone}")
    except sqlite3.IntegrityError:
        print("Error: An entry with that name already exists.")


def lookup_entry(cur):
    name = input("Enter name to look up: ").strip()
    cur.execute("SELECT PhoneNumber FROM Entries WHERE Name = ?", (name,))
    result = cur.fetchone()
    if result:
        print(f"{name}'s phone number is {result[0]}")
    else:
        print("Entry not found.")


def update_entry(cur):
    name = input("Enter name to update: ").strip()
    cur.execute("SELECT PhoneNumber FROM Entries WHERE Name = ?", (name,))
    if cur.fetchone():
        new_phone = input("Enter new phone number: ").strip()
        cur.execute("UPDATE Entries SET PhoneNumber = ? WHERE Name = ?", (new_phone, name))
        print(f"Updated {name}'s phone number to {new_phone}")
    else:
        print("Entry not found.")


def delete_entry(cur):
    name = input("Enter name to delete: ").strip()
    cur.execute("SELECT * FROM Entries WHERE Name = ?", (name,))
    if cur.fetchone():
        cur.execute("DELETE FROM Entries WHERE Name = ?", (name,))
        print(f"Deleted entry for {name}")
    else:
        print("Entry not found.")


def display_entries(cur):
    cur.execute("SELECT Name, PhoneNumber FROM Entries ORDER BY Name")
    results = cur.fetchall()
    if results:
        print("\nPhonebook Entries:")
        for name, phone in results:
            print(f"{name:20} {phone}")
    else:
        print("Phonebook is empty.")


if __name__ == '__main__':
    main()
