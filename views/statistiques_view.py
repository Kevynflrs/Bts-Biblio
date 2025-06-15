import tkinter as tk
from tkinter import messagebox
from controllers.statistiques_controller import StatistiquesController
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class StatistiquesView:
    def __init__(self, root, db_file):
        """
        Initialise la vue des statistiques.

        Arguments :
        root : La fenêtre principale de l'application.
        db_file (str) : Le chemin vers le fichier de la base de données.
        """
        self.root = root
        self.statistiques_controller = StatistiquesController(db_file)
        self.create_widgets()

    def create_widgets(self):
        """Crée les widgets pour l'interface des statistiques."""
        self.button_prets_par_mois = tk.Button(self.root, text="Prêts par Mois", command=self.show_prets_par_mois)
        self.button_prets_par_mois.pack(pady=5)

        self.button_livres_plus_empruntes = tk.Button(self.root, text="Livres les Plus Empruntés", command=self.show_livres_plus_empruntes)
        self.button_livres_plus_empruntes.pack(pady=5)

        self.button_export_pdf = tk.Button(self.root, text="Exporter en PDF", command=self.export_to_pdf)
        self.button_export_pdf.pack(pady=5)

        self.button_export_csv = tk.Button(self.root, text="Exporter en CSV", command=self.export_to_csv)
        self.button_export_csv.pack(pady=5)

        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def show_prets_par_mois(self):
        """Affiche les statistiques des prêts par mois."""
        data = self.statistiques_controller.get_prets_par_mois()
        if data:
            df = pd.DataFrame(data, columns=['Mois', 'Nombre de Prêts'])
            self.plot.clear()
            self.plot.bar(df['Mois'], df['Nombre de Prêts'])
            self.plot.set_title('Nombre de Prêts par Mois')
            self.plot.set_xlabel('Mois')
            self.plot.set_ylabel('Nombre de Prêts')
            self.canvas.draw()

    def show_livres_plus_empruntes(self):
        """Affiche les statistiques des livres les plus empruntés."""
        data = self.statistiques_controller.get_livres_plus_empruntes()
        if data:
            df = pd.DataFrame(data, columns=['Livre', 'Nombre d\'Emprunts'])
            self.plot.clear()
            self.plot.bar(df['Livre'], df['Nombre d\'Emprunts'])
            self.plot.set_title('Livres les Plus Empruntés')
            self.plot.set_xlabel('Livre')
            self.plot.set_ylabel('Nombre d\'Emprunts')
            self.canvas.draw()

    def export_to_pdf(self):
        """Exporte les statistiques en format PDF."""
        try:
            self.figure.savefig('statistiques.pdf')
            messagebox.showinfo("Succès", "Statistiques exportées en PDF avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'exportation en PDF: {e}")

    def export_to_csv(self):
        """Exporte les statistiques en format CSV."""
        try:
            data = self.statistiques_controller.get_prets_par_mois()
            df = pd.DataFrame(data, columns=['Mois', 'Nombre de Prêts'])
            df.to_csv('statistiques_prets_par_mois.csv', index=False)
            messagebox.showinfo("Succès", "Statistiques exportées en CSV avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'exportation en CSV: {e}")
