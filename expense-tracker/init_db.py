import sqlite3

# Connect to database
connection = sqlite3.connect("database.db")

# Create cursor
cursor = connection.cursor()

# Create expenses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,

    amount REAL NOT NULL,

    category TEXT NOT NULL,

    date TEXT NOT NULL

)
""")

# Save changes
connection.commit()

# Close connection
connection.close()

print("✅ Database created successfully!")
