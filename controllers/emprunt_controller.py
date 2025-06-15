from models.emprunt import Emprunt
from database.database_manager import create_connection
from datetime import datetime

class EmpruntController:
    def __init__(self, db_file):
        """
        Initialise le contrôleur d'emprunt avec le fichier de la base de données.
        """
        self.db_file = db_file

    def emprunter_livre(self, id_livre, id_adherent):
        """
        Enregistre un nouvel emprunt dans la base de données.

        Arguments :
        id_livre (int) : L'ID du livre emprunté.
        id_adherent (int) : L'ID de l'adhérent qui emprunte le livre.

        Retourne :
        int : L'ID de l'emprunt ajouté.
        """
        date_emprunt = datetime.now().strftime("%Y-%m-%d")
        emprunt = Emprunt(id_livre=id_livre, id_adherent=id_adherent, date_emprunt=date_emprunt)
        conn = create_connection(self.db_file)
        # Supposons que nous ayons une fonction add_emprunt dans database_manager
        emprunt_id = self._add_emprunt_to_db(conn, emprunt.to_tuple())
        conn.close()
        return emprunt_id

    def _add_emprunt_to_db(self, conn, emprunt):
        """
        Ajoute un nouvel emprunt à la base de données.

        Arguments :
        conn : L'objet de connexion à la base de données.
        emprunt (tuple) : Un tuple contenant les informations de l'emprunt.

        Retourne :
        int : L'ID de l'emprunt ajouté.
        """
        sql = ''' INSERT INTO Emprunts(id_livre, id_adherent, date_emprunt) VALUES(?,?,?) '''
        cursor = conn.cursor()
        cursor.execute(sql, emprunt)
        conn.commit()
        return cursor.lastrowid

    def retourner_livre(self, id_emprunt):
        """
        Met à jour la date de retour d'un emprunt dans la base de données.

        Arguments :
        id_emprunt (int) : L'ID de l'emprunt à mettre à jour.
        """
        date_retour = datetime.now().strftime("%Y-%m-%d")
        conn = create_connection(self.db_file)
        # Supposons que nous ayons une fonction update_emprunt dans database_manager
        self._update_emprunt_in_db(conn, id_emprunt, date_retour)
        conn.close()

    def _update_emprunt_in_db(self, conn, id_emprunt, date_retour):
        """
        Met à jour la date de retour d'un emprunt dans la base de données.

        Arguments :
        conn : L'objet de connexion à la base de données.
        id_emprunt (int) : L'ID de l'emprunt à mettre à jour.
        date_retour (str) : La date de retour de l'emprunt.
        """
        sql = ''' UPDATE Emprunts SET date_retour = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (date_retour, id_emprunt))
        conn.commit()

    def search_emprunts(self, query):
        """
        Recherche des emprunts dans la base de données par ID de livre ou ID d'adhérent.

        Arguments :
        query (str) : La chaîne de recherche pour l'ID de livre ou l'ID d'adhérent.

        Retourne :
        list : Une liste de tuples représentant les emprunts trouvés.
        """
        conn = create_connection(self.db_file)
        # Supposons que nous ayons une fonction search_emprunts dans database_manager
        emprunts = self._search_emprunts_in_db(conn, query)
        conn.close()
        return emprunts

    def _search_emprunts_in_db(self, conn, query):
        """
        Recherche des emprunts dans la base de données par ID de livre ou ID d'adhérent.

        Arguments :
        conn : L'objet de connexion à la base de données.
        query (str) : La chaîne de recherche pour l'ID de livre ou l'ID d'adhérent.

        Retourne :
        list : Une liste de tuples représentant les emprunts trouvés.
        """
        sql = ''' SELECT * FROM Emprunts WHERE id_livre LIKE ? OR id_adherent LIKE ? '''
        cursor = conn.cursor()
        cursor.execute(sql, (f'%{query}%', f'%{query}%'))
        rows = cursor.fetchall()
        return rows
