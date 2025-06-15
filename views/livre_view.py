import tkinter as tk
from tkinter import messagebox, simpledialog
from controllers.livre_controller import LivreController
import re

class LivreView:
    def __init__(self, root, db_file, role):
        """
        Initialise la vue des livres.

        Arguments :
        root : La fenêtre principale de l'application.
        db_file (str) : Le chemin vers le fichier de la base de données.
        role (str) : Le rôle de l'utilisateur (admin ou agent).
        """
        self.root = root
        self.livre_controller = LivreController(db_file)
        self.role = role
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

        self.button_modifier = tk.Button(self.root, text="Modifier", command=self.open_modify_dialog)
        self.button_modifier.grid(row=3, column=1)

        self.button_rechercher = tk.Button(self.root, text="Rechercher", command=self.rechercher_livre)
        self.button_rechercher.grid(row=4, column=0)

        self.button_lister = tk.Button(self.root, text="Lister", command=self.refresh_livre_list)
        self.button_lister.grid(row=4, column=1)

        # Désactiver les boutons pour les agents
        if self.role != "admin":
            self.button_ajouter.config(state=tk.DISABLED)
            self.button_modifier.config(state=tk.DISABLED)

        # Zone de texte pour afficher les résultats
        self.text_results = tk.Text(self.root, height=10, width=50)
        self.text_results.grid(row=5, column=0, columnspan=3)

    def validate_input(self, titre, auteur, annee):
        """Valide les entrées utilisateur avec des expressions régulières."""
        if not re.match(r'^[a-zA-Z0-9\s\-éèêëàâäçîïôöùûüÿœæÉÈÊËÀÂÄÇÎÏÔÖÙÛÜŸŒÆ]+$', titre):
            messagebox.showerror("Erreur", "Le titre contient des caractères invalides.")
            return False

        if not re.match(r'^[a-zA-Z0-9\s\-éèêëàâäçîïôöùûüÿœæÉÈÊËÀÂÄÇÎÏÔÖÙÛÜŸŒÆ]+$', auteur):
            messagebox.showerror("Erreur", "L'auteur contient des caractères invalides.")
            return False

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

    def open_modify_dialog(self):
        """Ouvre une boîte de dialogue pour modifier un livre."""
        selected_livre_id = simpledialog.askinteger("Modifier Livre", "Entrez l'ID du livre à modifier:")
        if selected_livre_id:
            self.show_modify_dialog(selected_livre_id)

    def show_modify_dialog(self, livre_id):
        """Affiche une boîte de dialogue pour modifier un livre."""
        modify_window = tk.Toplevel(self.root)
        modify_window.title("Modifier Livre")

        tk.Label(modify_window, text="Titre:").grid(row=0, column=0)
        entry_titre = tk.Entry(modify_window)
        entry_titre.grid(row=0, column=1)

        tk.Label(modify_window, text="Auteur:").grid(row=1, column=0)
        entry_auteur = tk.Entry(modify_window)
        entry_auteur.grid(row=1, column=1)

        tk.Label(modify_window, text="Année:").grid(row=2, column=0)
        entry_annee = tk.Entry(modify_window)
        entry_annee.grid(row=2, column=1)

        def save_changes():
            """Enregistre les modifications apportées à un livre."""
            new_titre = entry_titre.get()
            new_auteur = entry_auteur.get()
            new_annee = entry_annee.get()

            if not new_titre or not new_auteur or not new_annee:
                messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
                return

            try:
                new_annee = int(new_annee)
            except ValueError:
                messagebox.showerror("Erreur", "L'année doit être un nombre.")
                return

            if not self.validate_input(new_titre, new_auteur, new_annee):
                return

            self.livre_controller.update_livre(livre_id, new_titre, new_auteur, new_annee)
            messagebox.showinfo("Succès", "Livre modifié avec succès.")
            modify_window.destroy()
            self.refresh_livre_list()

        tk.Button(modify_window, text="Enregistrer", command=save_changes).grid(row=3, column=0, columnspan=2)

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
