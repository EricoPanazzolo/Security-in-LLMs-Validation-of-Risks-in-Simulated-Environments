"""
Initialization script for SQLite database used in LLM06: Excessive Agency challenge.
Creates the 'client_data.db' file, the 'employees' table, and populates it with sample data.
"""
import sqlite3
import os

# Define path for the SQLite database
DB_PATH = 'client_data.db'

# Remove existing database file (start fresh each time)
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

# Connect to the new database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create the 'employees' table
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        role TEXT NOT NULL
    );
    '''
)

# Insert sample data into 'employees'
employees_data = [
    ('Érico', 'Security Consultant'),
    ('Daniel', 'Security Analyst'),
    ('Avelino', 'Cryptography Engineer'),
]

cursor.executemany(
    "INSERT INTO employees (name, role) VALUES (?, ?);",
    employees_data
)

# Commit changes and close connection
conn.commit()
conn.close()

print(f"Database initialized successfully at {DB_PATH}")
