import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """
    Crée une connexion à une base de données SQLite spécifiée par db_file.

    Arguments :
    db_file (str) : Le chemin vers le fichier de la base de données SQLite.

    Retourne :
    conn : L'objet de connexion à la base de données ou None en cas d'erreur.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connecté à {db_file}, Version SQLite: {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    return conn

def create_tables(conn):
    """
    Crée les tables nécessaires dans la base de données si elles n'existent pas déjà.

    Arguments :
    conn : L'objet de connexion à la base de données.
    """
    try:
        cursor = conn.cursor()

        # Création de la table Livres pour stocker les informations sur les livres
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Livres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            auteur TEXT NOT NULL,
            annee INTEGER NOT NULL
        )
        ''')

        # Création de la table Adherents pour stocker les informations sur les adhérents
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Adherents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT NOT NULL
        )
        ''')

        # Création de la table Emprunts pour stocker les informations sur les emprunts
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Emprunts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_livre INTEGER NOT NULL,
            id_adherent INTEGER NOT NULL,
            date_emprunt TEXT NOT NULL,
            date_retour TEXT,
            FOREIGN KEY (id_livre) REFERENCES Livres (id),
            FOREIGN KEY (id_adherent) REFERENCES Adherents (id)
        )
        ''')
        
        # Create Utilisateurs table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
        ''')

        conn.commit()  # Valide les changements dans la base de données
    except Error as e:
        print(e)

def add_livre(conn, livre):
    """
    Ajoute un nouveau livre à la table Livres.

    Arguments :
    conn : L'objet de connexion à la base de données.
    livre (tuple) : Un tuple contenant les informations du livre (titre, auteur, annee).

    Retourne :
    int : L'ID du livre ajouté.
    """
    sql = ''' INSERT INTO Livres(titre, auteur, annee) VALUES(?,?,?) '''
    cursor = conn.cursor()
    cursor.execute(sql, livre)
    conn.commit()
    return cursor.lastrowid

def update_livre(conn, livre):
    """
    Met à jour les informations d'un livre dans la table Livres.

    Arguments :
    conn : L'objet de connexion à la base de données.
    livre (tuple) : Un tuple contenant les informations du livre (id, titre, auteur, annee).
    """
    sql = ''' UPDATE Livres SET titre = ?, auteur = ?, annee = ? WHERE id = ?'''
    cursor = conn.cursor()
    cursor.execute(sql, livre)
    conn.commit()

def delete_livre(conn, id):
    """
    Supprime un livre de la table Livres en fonction de son ID.

    Arguments :
    conn : L'objet de connexion à la base de données.
    id (int) : L'ID du livre à supprimer.
    """
    sql = 'DELETE FROM Livres WHERE id=?'
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()

def search_livres(conn, query):
    """
    Recherche des livres dans la table Livres par titre ou auteur.

    Arguments :
    conn : L'objet de connexion à la base de données.
    query (str) : La chaîne de recherche pour le titre ou l'auteur.

    Retourne :
    list : Une liste de tuples représentant les livres trouvés.
    """
    sql = ''' SELECT * FROM Livres WHERE titre LIKE ? OR auteur LIKE ? '''
    cursor = conn.cursor()
    cursor.execute(sql, (f'%{query}%', f'%{query}%'))
    rows = cursor.fetchall()
    return rows

def add_utilisateur(conn, utilisateur):
    """ Add a new user to the Utilisateurs table """
    sql = ''' INSERT INTO Utilisateurs(username, password, role)
              VALUES(?,?,?) '''
    cursor = conn.cursor()
    cursor.execute(sql, utilisateur)
    conn.commit()
    return cursor.lastrowid

def get_utilisateur(conn, username):
    """ Get a user by username """
    sql = ''' SELECT * FROM Utilisateurs WHERE username = ? '''
    cursor = conn.cursor()
    cursor.execute(sql, (username,))
    return cursor.fetchone()


def main():
    """
    Fonction principale pour créer la base de données et les tables.
    """
    database = 'bibliotheque.db'
    conn = create_connection(database)
    if conn is not None:
        create_tables(conn)
    else:
        print("Erreur ! Impossible de créer la connexion à la base de données.")

if __name__ == '__main__':
    main()