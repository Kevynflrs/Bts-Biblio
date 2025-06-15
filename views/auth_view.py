import tkinter as tk
from tkinter import messagebox
from database.database_manager import create_connection, add_utilisateur, get_utilisateur

class AuthView:
    def __init__(self, root, db_file, on_login_success):
        """
        Initialise la vue d'authentification.

        Arguments :
        root : La fenêtre principale de l'application.
        db_file (str) : Le chemin vers le fichier de la base de données.
        on_login_success (function) : Fonction à appeler en cas de succès de la connexion.
        """
        self.root = root
        self.db_file = db_file
        self.on_login_success = on_login_success
        self.create_login_widgets()

    def create_login_widgets(self):
        """
        Crée les widgets pour l'interface de connexion.
        Configure les champs de saisie pour le nom d'utilisateur et le mot de passe,
        ainsi que les boutons pour se connecter et créer un compte.
        """
        self.root.title("Connexion")

        self.label_username = tk.Label(self.root, text="Nom d'utilisateur")
        self.label_username.grid(row=0, column=0)
        self.entry_username = tk.Entry(self.root)
        self.entry_username.grid(row=0, column=1)

        self.label_password = tk.Label(self.root, text="Mot de passe")
        self.label_password.grid(row=1, column=0)
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.grid(row=1, column=1)

        self.button_login = tk.Button(self.root, text="Se connecter", command=self.login)
        self.button_login.grid(row=2, column=0, columnspan=2)

        self.button_create_account = tk.Button(self.root, text="Créer un compte", command=self.create_account)
        self.button_create_account.grid(row=3, column=0, columnspan=2)

    def login(self):
        """
        Gère le processus de connexion.
        Récupère le nom d'utilisateur et le mot de passe, vérifie les informations d'identification,
        et appelle la fonction de succès de connexion si les informations sont correctes.
        """
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username or not password:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        conn = create_connection(self.db_file)
        user = get_utilisateur(conn, username)
        conn.close()

        if user and user[2] == password:  # Vérification basique du mot de passe
            self.on_login_success(username, user[3])  # user[3] est le rôle
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

    def create_account(self):
        """
        Ouvre une nouvelle fenêtre pour la création de compte.
        Masque la fenêtre de connexion actuelle et ouvre la fenêtre de création de compte.
        """
        self.root.withdraw()  # Masquer la fenêtre actuelle
        create_account_window = tk.Toplevel(self.root)
        CreateAccountView(create_account_window, self.db_file, lambda: self.show_login(self.root))

    def show_login(self, root):
        """
        Réaffiche la fenêtre de connexion après la création d'un compte.

        Arguments :
        root : La fenêtre principale de l'application.
        """
        root.deiconify()  # Réafficher la fenêtre de connexion

class CreateAccountView:
    def __init__(self, root, db_file, on_success):
        """
        Initialise la vue de création de compte.

        Arguments :
        root : La fenêtre principale de l'application.
        db_file (str) : Le chemin vers le fichier de la base de données.
        on_success (function) : Fonction à appeler après la création réussie d'un compte.
        """
        self.root = root
        self.db_file = db_file
        self.on_success = on_success
        self.create_account_widgets()

    def create_account_widgets(self):
        """
        Crée les widgets pour l'interface de création de compte.
        Configure les champs de saisie pour le nom d'utilisateur, le mot de passe et le rôle,
        ainsi que le bouton pour créer le compte.
        """
        self.root.title("Créer un compte")

        self.label_username = tk.Label(self.root, text="Nom d'utilisateur")
        self.label_username.grid(row=0, column=0)
        self.entry_username = tk.Entry(self.root)
        self.entry_username.grid(row=0, column=1)

        self.label_password = tk.Label(self.root, text="Mot de passe")
        self.label_password.grid(row=1, column=0)
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.grid(row=1, column=1)

        self.label_role = tk.Label(self.root, text="Rôle")
        self.label_role.grid(row=2, column=0)
        self.entry_role = tk.Entry(self.root)
        self.entry_role.grid(row=2, column=1)

        self.button_create = tk.Button(self.root, text="Créer", command=self.create_user)
        self.button_create.grid(row=3, column=0, columnspan=2)

    def create_user(self):
        """
        Gère le processus de création de compte.
        Récupère les informations du compte, les valide, et les ajoute à la base de données.
        Affiche un message de succès ou d'erreur en fonction du résultat.
        """
        username = self.entry_username.get()
        password = self.entry_password.get()
        role = self.entry_role.get()

        if not username or not password or not role:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        conn = create_connection(self.db_file)
        user = get_utilisateur(conn, username)
        if user:
            messagebox.showerror("Erreur", "Le nom d'utilisateur existe déjà.")
            conn.close()
            return

        utilisateur = (username, password, role)
        add_utilisateur(conn, utilisateur)
        conn.close()

        messagebox.showinfo("Succès", "Compte créé avec succès.")
        self.root.destroy()
        self.on_success()
