import tkinter as tk
from tkinter import ttk
from database.database_manager import create_connection, create_tables
from views.livre_view import LivreView
from views.adherent_view import AdherentView
from views.emprunt_view import EmpruntView

def initialize_database(db_file):
    """Initialize the database and create tables if they don't exist."""
    conn = create_connection(db_file)
    if conn is not None:
        create_tables(conn)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

class Application(ttk.Frame):
    def __init__(self, parent, db_file):
        super().__init__(parent)

        self.parent = parent
        self.db_file = db_file

        self.notebook = ttk.Notebook(self.parent)
        self.notebook.pack(pady=10, expand=True, fill='both')

        # Onglet pour la gestion des livres
        livre_frame = ttk.Frame(self.notebook)
        self.notebook.add(livre_frame, text="Gestion des Livres")
        LivreView(livre_frame, self.db_file)

        # Onglet pour la gestion des adhérents
        adherent_frame = ttk.Frame(self.notebook)
        self.notebook.add(adherent_frame, text="Gestion des Adhérents")
        AdherentView(adherent_frame, self.db_file)

        # Onglet pour la gestion des emprunts
        emprunt_frame = ttk.Frame(self.notebook)
        self.notebook.add(emprunt_frame, text="Gestion des Emprunts")
        EmpruntView(emprunt_frame, self.db_file)

def main():
    root = tk.Tk()
    root.title("Application de Gestion de Bibliothèque")
    db_file = "bibliotheque.db"

    # Initialize the database
    initialize_database(db_file)

    app = Application(root, db_file)
    root.mainloop()

if __name__ == "__main__":
    main()
