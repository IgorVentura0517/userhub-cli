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
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )            
    """)

    connection.commit()
    connection.close()

### Função de inserir usuários ###
def create_user(nome, email):
    import sqlite3
    
    with sqlite3.connect("users.db") as connection:
        cursor = connection.cursor()
        
        cursor.execute(
            "INSERT INTO users (nome, email) VALUES (?, ?)",
            (nome, email)
        )


### Função de selecionar usuários ###

def get_users():

    with sqlite3.connect("users.db") as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        return users   