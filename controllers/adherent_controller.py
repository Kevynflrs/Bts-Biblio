from models.adherent import Adherent
from database.database_manager import create_connection

class AdherentController:
    def __init__(self, db_file):
        """
        Initialise le contrôleur d'adhérent avec le fichier de la base de données.
        """
        self.db_file = db_file

    def add_adherent(self, nom, prenom, email):
        """
        Ajoute un nouvel adhérent à la base de données.

        Arguments :
        nom (str) : Le nom de l'adhérent.
        prenom (str) : Le prénom de l'adhérent.
        email (str) : L'email de l'adhérent.

        Retourne :
        int : L'ID de l'adhérent ajouté.
        """
        adherent = Adherent(nom=nom, prenom=prenom, email=email)
        conn = create_connection(self.db_file)
        # Supposons que nous ayons une fonction add_adherent dans database_manager
        adherent_id = self._add_adherent_to_db(conn, adherent.to_tuple())
        conn.close()
        return adherent_id

    def _add_adherent_to_db(self, conn, adherent):
        """
        Ajoute un nouvel adhérent à la base de données.

        Arguments :
        conn : L'objet de connexion à la base de données.
        adherent (tuple) : Un tuple contenant les informations de l'adhérent.

        Retourne :
        int : L'ID de l'adhérent ajouté.
        """
        sql = ''' INSERT INTO Adherents(nom, prenom, email) VALUES(?,?,?) '''
        cursor = conn.cursor()
        cursor.execute(sql, adherent)
        conn.commit()
        return cursor.lastrowid

    def update_adherent(self, id, nom, prenom, email):
        """
        Met à jour un adhérent existant dans la base de données.

        Arguments :
        id (int) : L'ID de l'adhérent à mettre à jour.
        nom (str) : Le nouveau nom de l'adhérent.
        prenom (str) : Le nouveau prénom de l'adhérent.
        email (str) : Le nouvel email de l'adhérent.
        """
        adherent = Adherent(id=id, nom=nom, prenom=prenom, email=email)
        conn = create_connection(self.db_file)
        # Supposons que nous ayons une fonction update_adherent dans database_manager
        self._update_adherent_in_db(conn, adherent.to_tuple_with_id())
        conn.close()

    def _update_adherent_in_db(self, conn, adherent):
        """
        Met à jour un adhérent dans la base de données.

        Arguments :
        conn : L'objet de connexion à la base de données.
        adherent (tuple) : Un tuple contenant les informations de l'adhérent.
        """
        sql = ''' UPDATE Adherents SET nom = ?, prenom = ?, email = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, adherent)
        conn.commit()

    def delete_adherent(self, id):
        """
        Supprime un adhérent de la base de données.

        Arguments :
        id (int) : L'ID de l'adhérent à supprimer.
        """
        conn = create_connection(self.db_file)
        # Supposons que nous ayons une fonction delete_adherent dans database_manager
        self._delete_adherent_from_db(conn, id)
        conn.close()

    def _delete_adherent_from_db(self, conn, id):
        """
        Supprime un adhérent de la base de données.

        Arguments :
        conn : L'objet de connexion à la base de données.
        id (int) : L'ID de l'adhérent à supprimer.
        """
        sql = 'DELETE FROM Adherents WHERE id=?'
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()

    def search_adherents(self, query):
        """
        Recherche des adhérents dans la base de données par nom ou prénom.

        Arguments :
        query (str) : La chaîne de recherche pour le nom ou le prénom.

        Retourne :
        list : Une liste de tuples représentant les adhérents trouvés.
        """
        conn = create_connection(self.db_file)
        # Supposons que nous ayons une fonction search_adherents dans database_manager
        adherents = self._search_adherents_in_db(conn, query)
        conn.close()
        return adherents

    def _search_adherents_in_db(self, conn, query):
        """
        Recherche des adhérents dans la base de données par nom ou prénom.

        Arguments :
        conn : L'objet de connexion à la base de données.
        query (str) : La chaîne de recherche pour le nom ou le prénom.

        Retourne :
        list : Une liste de tuples représentant les adhérents trouvés.
        """
        sql = ''' SELECT * FROM Adherents WHERE nom LIKE ? OR prenom LIKE ? '''
        cursor = conn.cursor()
        cursor.execute(sql, (f'%{query}%', f'%{query}%'))
        rows = cursor.fetchall()
        return rows
