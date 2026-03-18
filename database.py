import sqlite3

### Estabelecendo conexão com o banco de dados declaração do cursor ###
def create_connection():
    return sqlite3.connect("users.db")

### Função de criar a tabela de usuários ###
def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )            
    """)

    connection.commit()
    connection.close()


