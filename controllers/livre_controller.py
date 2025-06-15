from models.livre import Livre
from database.database_manager import create_connection, add_livre, update_livre, delete_livre, search_livres

class LivreController:
    def __init__(self, db_file):
        """
        Initialise le contrôleur de livre avec le fichier de la base de données.
        """
        self.db_file = db_file

    def add_livre(self, titre, auteur, annee):
        """
        Ajoute un nouveau livre à la base de données.

        Arguments :
        titre (str) : Le titre du livre.
        auteur (str) : L'auteur du livre.
        annee (int) : L'année de publication du livre.

        Retourne :
        int : L'ID du livre ajouté.
        """
        livre = Livre(titre=titre, auteur=auteur, annee=annee)
        conn = create_connection(self.db_file)
        livre_id = add_livre(conn, livre.to_tuple())
        conn.close()
        return livre_id

    def update_livre(self, id, titre, auteur, annee):
        """
        Met à jour un livre existant dans la base de données.

        Arguments :
        id (int) : L'ID du livre à mettre à jour.
        titre (str) : Le nouveau titre du livre.
        auteur (str) : Le nouvel auteur du livre.
        annee (int) : La nouvelle année de publication du livre.
        """
        livre = Livre(id=id, titre=titre, auteur=auteur, annee=annee)
        conn = create_connection(self.db_file)
        update_livre(conn, livre.to_tuple_with_id())
        conn.close()

    def delete_livre(self, id):
        """
        Supprime un livre de la base de données.

        Arguments :
        id (int) : L'ID du livre à supprimer.
        """
        conn = create_connection(self.db_file)
        delete_livre(conn, id)
        conn.close()

    def search_livres(self, query):
        """
        Recherche des livres dans la base de données par titre ou auteur.

        Arguments :
        query (str) : La chaîne de recherche pour le titre ou l'auteur.

        Retourne :
        list : Une liste de tuples représentant les livres trouvés.
        """
        conn = create_connection(self.db_file)
        livres = search_livres(conn, query)
        conn.close()
        return livres
