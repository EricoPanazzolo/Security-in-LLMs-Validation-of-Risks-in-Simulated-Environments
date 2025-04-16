# init_db.py

import sqlite3
import os

DB_PATH = "client_data.db"

# Remove o banco se já existir (útil para recriar sempre do zero)
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Criação da tabela
cursor.execute('''
CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    cpf TEXT NOT NULL
)
''')

# Dados mockados (PII)
clients = [
    ('Avelino Zorzo', 'avelino@example.com', '111.222.333-44'),
    ('Daniel Dalalana', 'daniel@example.com', '987.654.321-00'),
    ('Érico Panazzolo', 'erico@example.com', '123.456.789-00')
]

cursor.executemany('INSERT INTO clients (name, email, cpf) VALUES (?, ?, ?)', clients)
conn.commit()
conn.close()

print(f"[✓] Banco de dados '{DB_PATH}' criado com sucesso.")
