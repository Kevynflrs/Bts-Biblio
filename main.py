import tkinter as tk
from tkinter import ttk
from views.livre_view import LivreView
from views.adherent_view import AdherentView
from views.emprunt_view import EmpruntView

class Application(ttk.Frame):
    def __init__(self, parent, db_file):
        super().__init__(parent)

        self.parent = parent
        self.db_file = db_file

        self.parent.title("Application de Gestion de Bibliothèque")
        self.parent.geometry("800x600")

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
    app = Application(root, db_file)
    root.mainloop()

if __name__ == "__main__":
    main()
