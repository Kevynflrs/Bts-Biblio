from database.database_manager import create_connection

class StatistiquesController:
    def __init__(self, db_file):
        self.db_file = db_file

    def get_prets_par_mois(self):
        """Récupère les statistiques des prêts par mois."""
        conn = create_connection(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT strftime('%m', date_emprunt) as Mois, COUNT(*) as "Nombre de Prêts"
            FROM Emprunts
            GROUP BY Mois
        ''')
        data = cursor.fetchall()
        conn.close()
        return data

    def get_livres_plus_empruntes(self):
        """Récupère les statistiques des livres les plus empruntés."""
        conn = create_connection(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT Livres.titre as Livre, COUNT(*) as "Nombre d'Emprunts"
            FROM Emprunts
            JOIN Livres ON Emprunts.id_livre = Livres.id
            GROUP BY Livre
            ORDER BY "Nombre d'Emprunts" DESC
            LIMIT 5
        ''')
        data = cursor.fetchall()
        conn.close()
        return data