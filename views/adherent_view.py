import tkinter as tk
from tkinter import messagebox
from controllers.adherent_controller import AdherentController

class AdherentView:
    def __init__(self, root, db_file):
        """
        Initialise la vue des adhérents.

        Arguments :
        root : La fenêtre principale de l'application.
        db_file (str) : Le chemin vers le fichier de la base de données.
        """
        self.root = root
        self.adherent_controller = AdherentController(db_file)
        self.create_widgets()

    def create_widgets(self):
        """Crée les widgets pour l'interface des adhérents."""
        ##self.root.title("Gestion des Adhérents")

        # Nom
        self.label_nom = tk.Label(self.root, text="Nom")
        self.label_nom.grid(row=0, column=0)
        self.entry_nom = tk.Entry(self.root)
        self.entry_nom.grid(row=0, column=1)

        # Prénom
        self.label_prenom = tk.Label(self.root, text="Prénom")
        self.label_prenom.grid(row=1, column=0)
        self.entry_prenom = tk.Entry(self.root)
        self.entry_prenom.grid(row=1, column=1)

        # Email
        self.label_email = tk.Label(self.root, text="Email")
        self.label_email.grid(row=2, column=0)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=2, column=1)

        # Boutons
        self.button_ajouter = tk.Button(self.root, text="Ajouter", command=self.ajouter_adherent)
        self.button_ajouter.grid(row=3, column=0)

        self.button_rechercher = tk.Button(self.root, text="Rechercher", command=self.rechercher_adherent)
        self.button_rechercher.grid(row=3, column=1)

        self.button_lister = tk.Button(self.root, text="Lister", command=self.lister_adherents)
        self.button_lister.grid(row=3, column=2)

        # Zone de texte pour afficher les résultats
        self.text_results = tk.Text(self.root, height=10, width=50)
        self.text_results.grid(row=4, column=0, columnspan=3)

    def ajouter_adherent(self):
        """Ajoute un adhérent à la base de données."""
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        email = self.entry_email.get()

        if not nom or not prenom or not email:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        adherent_id = self.adherent_controller.add_adherent(nom, prenom, email)
        messagebox.showinfo("Succès", f"Adhérent ajouté avec l'ID: {adherent_id}")

    def rechercher_adherent(self):
        """Recherche des adhérents dans la base de données."""
        query = self.entry_nom.get()
        adherents = self.adherent_controller.search_adherents(query)

        self.text_results.delete(1.0, tk.END)
        for adherent in adherents:
            self.text_results.insert(tk.END, f"ID: {adherent[0]}, Nom: {adherent[1]}, Prénom: {adherent[2]}, Email: {adherent[3]}\n")

    def lister_adherents(self):
        """Liste tous les adhérents de la base de données."""
        adherents = self.adherent_controller.search_adherents("")
        self.text_results.delete(1.0, tk.END)
        for adherent in adherents:
            self.text_results.insert(tk.END, f"ID: {adherent[0]}, Nom: {adherent[1]}, Prénom: {adherent[2]}, Email: {adherent[3]}\n")
