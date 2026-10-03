import sqlite3

def init_db():
    """Ensures the table exists before any operations run."""
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL UNIQUE
    )
    """)
    conn.commit()
    conn.close()

def GetCommand():
    try:
        command = input("\n> ")
        return int(command)
    except ValueError:
        print("❌ Commands should be numbers only.")
        return None

def AddContact():
    name = input("🧑 Full Name> ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return

    phone_number = input("📞 Phone Number> ")
    if not phone_number.isdigit():
        print("❌ Phone Number should be numbers only.")
        return

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO contacts(name, phone_number) VALUES(?, ?)", (name, phone_number))
        conn.commit()
        print(f"✅ Contact '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print("❌ This phone number already exists.")
    finally:
        conn.close()

def viewContacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    conn.close()

    if contacts:
        print("\n--- Contact List ---")
        for contact in contacts:
            # contact[0] is ID, contact[1] is Name, contact[2] is Phone
            print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]}")
    else:
        print("ℹ️ No contacts to view yet.")

def UpdateContacts():
    try:
        contact_id = int(input("Id to edit> "))
        new_phone = input("New Phone Number> ")
        
        if not new_phone.isdigit():
            print("❌ Phone Number should be a number.")
            return

        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        
        # Check if ID exists
        cursor.execute("SELECT id FROM contacts WHERE id = ?", (contact_id,))
        if not cursor.fetchone():
            print("❌ Contact ID not found.")
            conn.close()
            return

        cursor.execute("UPDATE contacts SET phone_number = ? WHERE id = ?", (new_phone, contact_id))
        conn.commit()
        conn.close()
        print("✅ Contact updated successfully.")
    except ValueError:
        print("❌ ID must be a number.")

def DeleteContact():
    try:
        contact_id = int(input("Id to delete> "))
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        
        # Check if ID exists
        cursor.execute("SELECT id FROM contacts WHERE id = ?", (contact_id,))
        if not cursor.fetchone():
            print("❌ Contact ID not found.")
            conn.close()
            return

        cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        conn.commit()
        conn.close()
        print("🗑️ Contact deleted successfully.")
    except ValueError:
        print("❌ ID must be a number.")

