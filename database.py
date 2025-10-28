import sqlite3

# Cria o banco de dados
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Cria a tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT
)
""")

conn.commit()
conn.close()
