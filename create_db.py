import sqlite3

def create_table():
    connection = sqlite3.connect("user_database.db")
    cursor = connection.cursor()

    # Création de la table 'users'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

def register_user(username, password):
    connection = sqlite3.connect("user_database.db")
    cursor = connection.cursor()

    # Vérifier si l'utilisateur existe déjà
    cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    existing_user = cursor.fetchone()

    if existing_user is None:
        # Ajouter un nouvel utilisateur
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        connection.commit()
        print("Utilisateur enregistré avec succès.")
    else:
        print("L'utilisateur existe déjà.")

    connection.close()

if __name__ == "__main__":
    create_table()
