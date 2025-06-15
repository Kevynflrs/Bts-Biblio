import tkinter as tk
from tkinter import messagebox
from controllers.emprunt_controller import EmpruntController
import re

class EmpruntView:
    def __init__(self, root, db_file, role):
        """
        Initialise la vue des emprunts.

        Arguments :
        root : La fenêtre principale de l'application.
        db_file (str) : Le chemin vers le fichier de la base de données.
        role (str) : Le rôle de l'utilisateur (admin ou agent).
        """
        self.root = root
        self.emprunt_controller = EmpruntController(db_file)
        self.role = role
        self.create_widgets()
        self.refresh_emprunt_list()

    def create_widgets(self):
        """Crée les widgets pour l'interface des emprunts."""
        # ID Livre
        self.label_id_livre = tk.Label(self.root, text="ID Livre")
        self.label_id_livre.grid(row=0, column=0)
        self.entry_id_livre = tk.Entry(self.root)
        self.entry_id_livre.grid(row=0, column=1)

        # ID Adhérent
        self.label_id_adherent = tk.Label(self.root, text="ID Adhérent")
        self.label_id_adherent.grid(row=1, column=0)
        self.entry_id_adherent = tk.Entry(self.root)
        self.entry_id_adherent.grid(row=1, column=1)

        # Boutons
        self.button_emprunter = tk.Button(self.root, text="Emprunter", command=self.emprunter_livre)
        self.button_emprunter.grid(row=2, column=0)

        self.button_retourner = tk.Button(self.root, text="Retourner", command=self.retourner_livre)
        self.button_retourner.grid(row=2, column=1)

        self.button_lister = tk.Button(self.root, text="Lister", command=self.refresh_emprunt_list)
        self.button_lister.grid(row=2, column=2)

        # Zone de texte pour afficher les résultats
        self.text_results = tk.Text(self.root, height=10, width=50)
        self.text_results.grid(row=3, column=0, columnspan=3)

    def emprunter_livre(self):
        """Enregistre un nouvel emprunt dans la base de données."""
        id_livre = self.entry_id_livre.get()
        id_adherent = self.entry_id_adherent.get()

        if not id_livre or not id_adherent:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        if not re.match(r'^\d+$', id_livre):
            messagebox.showerror("Erreur", "L'ID du livre doit être un nombre.")
            return

        if not re.match(r'^\d+$', id_adherent):
            messagebox.showerror("Erreur", "L'ID de l'adhérent doit être un nombre.")
            return

        self.emprunt_controller.emprunter_livre(int(id_livre), int(id_adherent))
        messagebox.showinfo("Succès", "Emprunt enregistré avec succès.")
        self.refresh_emprunt_list()

    def retourner_livre(self):
        """Met à jour la date de retour d'un emprunt dans la base de données."""
        id_emprunt = self.entry_id_livre.get()

        if not id_emprunt:
            messagebox.showerror("Erreur", "L'ID de l'emprunt doit être renseigné.")
            return

        if not re.match(r'^\d+$', id_emprunt):
            messagebox.showerror("Erreur", "L'ID de l'emprunt doit être un nombre.")
            return

        self.emprunt_controller.retourner_livre(int(id_emprunt))
        messagebox.showinfo("Succès", "Livre retourné avec succès.")
        self.refresh_emprunt_list()

    def refresh_emprunt_list(self, query=""):
        """Rafraîchit la liste des emprunts affichée."""
        emprunts = self.emprunt_controller.search_emprunts(query)
        self.text_results.delete(1.0, tk.END)
        for emprunt in emprunts:
            self.text_results.insert(tk.END, f"ID: {emprunt[0]}, ID Livre: {emprunt[1]}, ID Adhérent: {emprunt[2]}, Date Emprunt: {emprunt[3]}, Date Retour: {emprunt[4]}\n")