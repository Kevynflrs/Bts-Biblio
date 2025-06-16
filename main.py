import tkinter as tk
from tkinter import ttk
from views.auth_view import AuthView
from views.livre_view import LivreView
from views.adherent_view import AdherentView
from views.emprunt_view import EmpruntView
from views.statistiques_view import StatistiquesView
from database.database_manager import create_connection, create_tables

def initialize_database(db_file):
    """Initialize the database and create tables if they don't exist."""
    conn = create_connection(db_file)
    if conn is not None:
        create_tables(conn)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

def on_login_success(username, role):
    root = tk.Tk()
    app = Application(root, "bibliotheque.db", username, role)
    root.mainloop()

class Application(tk.Frame):
    def __init__(self, parent, db_file, username, role):
        super().__init__(parent)

        self.parent = parent
        self.db_file = db_file
        self.username = username
        self.role = role

        self.parent.title(f"Application de Gestion de Bibliothèque - {username} ({role})")
        self.parent.geometry("800x600")

        self.notebook = ttk.Notebook(self.parent)
        self.notebook.pack(pady=10, expand=True, fill='both')

        # Onglet pour la gestion des livres
        livre_frame = ttk.Frame(self.notebook)
        self.notebook.add(livre_frame, text="Gestion des Livres")
        LivreView(livre_frame, self.db_file, self.role)

        # Onglet pour la gestion des adhérents
        adherent_frame = ttk.Frame(self.notebook)
        self.notebook.add(adherent_frame, text="Gestion des Adhérents")
        AdherentView(adherent_frame, self.db_file, self.role)

        # Onglet pour la gestion des emprunts
        emprunt_frame = ttk.Frame(self.notebook)
        self.notebook.add(emprunt_frame, text="Gestion des Emprunts")
        EmpruntView(emprunt_frame, self.db_file, self.role)

        # Onglet pour les statistiques (uniquement pour les administrateurs)
        if self.role == "admin":
            statistiques_frame = ttk.Frame(self.notebook)
            self.notebook.add(statistiques_frame, text="Statistiques")
            StatistiquesView(statistiques_frame, self.db_file)

def main():
    root = tk.Tk()
    db_file = "bibliotheque.db"
    initialize_database(db_file)
    auth_view = AuthView(root, db_file, on_login_success)
    root.mainloop()

if __name__ == "__main__":
    main()
