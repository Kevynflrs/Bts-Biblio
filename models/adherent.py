class Adherent:
    def __init__(self, id=None, nom=None, prenom=None, email=None):
        # Constructeur de la classe Adherent
        # Initialise un nouvel objet Adherent avec les attributs id, nom, prenom et email
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email

    def __str__(self):
        # Retourne une représentation sous forme de chaîne de caractères de l'objet Adherent
        # Utile pour l'affichage ou le débogage
        return f"Adherent(id={self.id}, nom={self.nom}, prenom={self.prenom}, email={self.email})"

    def to_tuple(self):
        # Convertit les attributs de l'objet Adherent en un tuple
        # Facilite l'insertion dans la base de données
        return (self.nom, self.prenom, self.email)

    def to_tuple_with_id(self):
        # Convertit tous les attributs de l'objet Adherent, y compris l'id, en un tuple
        # Utile pour les mises à jour dans la base de données
        return (self.id, self.nom, self.prenom, self.email)
