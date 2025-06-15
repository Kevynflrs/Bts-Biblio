import tkinter as tk
from tkinter import messagebox
from controllers.livre_controller import LivreController
import re

class LivreView:
    def __init__(self, root, db_file):
        """
        Initialise la vue des livres.

        Arguments :
        root : La fenêtre principale de l'application.
        db_file (str) : Le chemin vers le fichier de la base de données.
        """
        self.root = root
        self.livre_controller = LivreController(db_file)
        self.create_widgets()
        self.refresh_livre_list()

    def create_widgets(self):
        """Crée les widgets pour l'interface des livres."""
        # Titre
        self.label_titre = tk.Label(self.root, text="Titre")
        self.label_titre.grid(row=0, column=0)
        self.entry_titre = tk.Entry(self.root)
        self.entry_titre.grid(row=0, column=1)

        # Auteur
        self.label_auteur = tk.Label(self.root, text="Auteur")
        self.label_auteur.grid(row=1, column=0)
        self.entry_auteur = tk.Entry(self.root)
        self.entry_auteur.grid(row=1, column=1)

        # Année
        self.label_annee = tk.Label(self.root, text="Année")
        self.label_annee.grid(row=2, column=0)
        self.entry_annee = tk.Entry(self.root)
        self.entry_annee.grid(row=2, column=1)

        # Boutons
        self.button_ajouter = tk.Button(self.root, text="Ajouter", command=self.ajouter_livre)
        self.button_ajouter.grid(row=3, column=0)

        self.button_rechercher = tk.Button(self.root, text="Rechercher", command=self.rechercher_livre)
        self.button_rechercher.grid(row=3, column=1)

        self.button_lister = tk.Button(self.root, text="Lister", command=self.refresh_livre_list)
        self.button_lister.grid(row=3, column=2)

        # Champ pour l'ID du livre à modifier/supprimer
        self.label_id = tk.Label(self.root, text="ID du livre")
        self.label_id.grid(row=5, column=0)
        self.entry_id = tk.Entry(self.root)
        self.entry_id.grid(row=5, column=1)

        # Bouton Modifier
        self.button_modifier = tk.Button(self.root, text="Modifier", command=self.modifier_livre)
        self.button_modifier.grid(row=5, column=2)

        # Bouton Supprimer
        self.button_supprimer = tk.Button(self.root, text="Supprimer", command=self.supprimer_livre)
        self.button_supprimer.grid(row=5, column=3)

        # Zone de texte pour afficher les résultats
        self.text_results = tk.Text(self.root, height=10, width=50)
        self.text_results.grid(row=4, column=0, columnspan=3)

    def validate_input(self, titre, auteur, annee):
        """Valide les entrées utilisateur avec des expressions régulières."""
        # Vérifie que le titre et l'auteur ne contiennent que des lettres, des chiffres et des espaces
        if not re.match(r'^[a-zA-Z0-9\s\-éèêëàâäçîïôöùûüÿœæÉÈÊËÀÂÄÇÎÏÔÖÙÛÜŸŒÆ]+$', titre):
            messagebox.showerror("Erreur", "Le titre contient des caractères invalides.")
            return False

        if not re.match(r'^[a-zA-Z0-9\s\-éèêëàâäçîïôöùûüÿœæÉÈÊËÀÂÄÇÎÏÔÖÙÛÜŸŒÆ]+$', auteur):
            messagebox.showerror("Erreur", "L'auteur contient des caractères invalides.")
            return False

        # Vérifie que l'année est un nombre valide
        if not re.match(r'^\d{4}$', str(annee)):
            messagebox.showerror("Erreur", "L'année doit être un nombre à 4 chiffres.")
            return False

        return True

    def ajouter_livre(self):
        """Ajoute un livre à la base de données."""
        titre = self.entry_titre.get()
        auteur = self.entry_auteur.get()
        annee = self.entry_annee.get()

        if not titre or not auteur or not annee:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        try:
            annee = int(annee)
        except ValueError:
            messagebox.showerror("Erreur", "L'année doit être un nombre.")
            return

        if not self.validate_input(titre, auteur, annee):
            return

        self.livre_controller.add_livre(titre, auteur, annee)
        messagebox.showinfo("Succès", "Livre ajouté avec succès.")
        self.refresh_livre_list()

    def modifier_livre(self):
        """Ouvre une fenêtre popup pour modifier un livre existant."""
        id_livre = self.entry_id.get()
        if not id_livre:
            messagebox.showerror("Erreur", "Veuillez saisir l'ID du livre à modifier.")
            return

        try:
            id_livre = int(id_livre)
        except ValueError:
            messagebox.showerror("Erreur", "L'ID doit être un nombre.")
            return

        # Recherche du livre pour pré-remplir les champs
        livres = self.livre_controller.search_livres("")
        livre_cible = None
        for livre in livres:
            if livre[0] == id_livre:
                livre_cible = livre
                break

        if not livre_cible:
            messagebox.showerror("Erreur", f"Aucun livre trouvé avec l'ID {id_livre}.")
            return

        # Créer une popup
        popup = tk.Toplevel(self.root)
        popup.title("Modifier le livre")

        # Champs pré-remplis
        tk.Label(popup, text="Titre").grid(row=0, column=0)
        entry_titre = tk.Entry(popup)
        entry_titre.insert(0, livre_cible[1])
        entry_titre.grid(row=0, column=1)

        tk.Label(popup, text="Auteur").grid(row=1, column=0)
        entry_auteur = tk.Entry(popup)
        entry_auteur.insert(0, livre_cible[2])
        entry_auteur.grid(row=1, column=1)

        tk.Label(popup, text="Année").grid(row=2, column=0)
        entry_annee = tk.Entry(popup)
        entry_annee.insert(0, str(livre_cible[3]))
        entry_annee.grid(row=2, column=1)

        def confirmer_modification():
            titre = entry_titre.get()
            auteur = entry_auteur.get()
            annee = entry_annee.get()

            if not titre or not auteur or not annee:
                messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
                return

            try:
                annee = int(annee)
            except ValueError:
                messagebox.showerror("Erreur", "L'année doit être un nombre.")
                return

            if not self.validate_input(titre, auteur, annee):
                return

            self.livre_controller.update_livre(id_livre, titre, auteur, annee)
            messagebox.showinfo("Succès", "Livre modifié avec succès.")
            self.refresh_livre_list()
            popup.destroy()

        # Bouton de confirmation
        tk.Button(popup, text="Enregistrer", command=confirmer_modification).grid(row=3, column=0, columnspan=2)


    def supprimer_livre(self):
        """Supprime un livre de la base de données par son ID."""
        id_livre = self.entry_id.get()
        if not id_livre:
            messagebox.showerror("Erreur", "Veuillez saisir l'ID du livre à supprimer.")
            return
        try:
            id_livre = int(id_livre)
        except ValueError:
            messagebox.showerror("Erreur", "L'ID doit être un nombre.")
            return

        confirmation = messagebox.askyesno("Confirmation", f"Supprimer le livre avec ID {id_livre} ?")
        if confirmation:
            self.livre_controller.delete_livre(id_livre)
            messagebox.showinfo("Succès", "Livre supprimé avec succès.")
            self.refresh_livre_list()

    def rechercher_livre(self):
        """Recherche des livres dans la base de données."""
        query = self.entry_titre.get()
        self.refresh_livre_list(query)

    def refresh_livre_list(self, query=""):
        """Rafraîchit la liste des livres affichée."""
        livres = self.livre_controller.search_livres(query)
        self.text_results.delete(1.0, tk.END)
        for livre in livres:
            self.text_results.insert(tk.END, f"ID: {livre[0]}, Titre: {livre[1]}, Auteur: {livre[2]}, Année: {livre[3]}\n")