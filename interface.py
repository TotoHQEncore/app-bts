import tkinter as tk
from tkinter import messagebox,font
from create_db import register_user, create_table
import sqlite3

def on_login_click():
    username = entry_username.get()
    password = entry_password.get()

    if password.lower() == 'admin':
        messagebox.showerror("Mot de passe interdit", "Le mot de passe 'admin' n'est pas autorisé. Veuillez choisir un autre mot de passe.")    
    if is_valid_user(username, password):
        welcome_window(username)
    else:
        messagebox.showerror("Erreur d'authentification", "Nom d'utilisateur ou mot de passe incorrect. Veuillez vérifier vos informations.")


def is_valid_user(username, password):
    connection = sqlite3.connect("user_database.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username=?', (username,))     #On regarde si l'utilisateur est dans la base de données
    existing_user = cursor.fetchone()

    if existing_user is None: #Ajouter l'utilisateur a la base de donnée s'il n'existe pas
        register_user(username, password)
        connection.close()
        return True
    else:
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))    # Si l'utilisateur est présent dans la DB, on vérifie le mot de passe
        user = cursor.fetchone()
        connection.close()
        return user is not None
def welcome_window(username):
    welcome_window = tk.Toplevel(app)
    welcome_window.title("Bienvenue")

    welcome_label = tk.Label(welcome_window, text=f"Bonjour {username}!")
    welcome_label.pack(pady=20)

app = tk.Tk()
app.title("Connexion à l'Application") # Création de la fenêtre principale
# Ajuster la taille de la fenêtre à 1920x1080
app.geometry("400x300")

# Centrer la fenêtre sur l'écran
app.update_idletasks()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - app.winfo_reqwidth()) //2
y = (screen_height - app.winfo_reqheight()) //2
app.geometry("+{}+{}".format(x, y))
app.configure(bg="#F5f5dc")

underline_font = tk.font.Font(family='Helvetica', size=10, underline=True)

label_username = tk.Label(app, text="Nom d'utilisateur:", bg="#F5f5dc",font=underline_font )
entry_username = tk.Entry(app)

label_password = tk.Label(app, text="Mot de passe:", bg="#F5f5dc",font=underline_font)
entry_password = tk.Entry(app, show="*") 

btn_login = tk.Button(app, text="Se connecter", command=on_login_click)

label_username.pack(pady=10)
entry_username.pack(pady=10)
label_password.pack(pady=10)
entry_password.pack(pady=10)
btn_login.pack(pady=20)

app.mainloop()