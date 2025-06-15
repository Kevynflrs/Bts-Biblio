class Livre:
    def __init__(self, id=None, titre=None, auteur=None, annee=None):
        # Constructeur de la classe Livre
        # Initialise un nouvel objet Livre avec les attributs id, titre, auteur et annee
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    def __str__(self):
        # Retourne une représentation sous forme de chaîne de caractères de l'objet Livre
        # Utile pour l'affichage ou le débogage
        return f"Livre(id={self.id}, titre={self.titre}, auteur={self.auteur}, annee={self.annee})"

    def to_tuple(self):
        # Convertit les attributs de l'objet Livre en un tuple
        # Facilite l'insertion dans la base de données
        return (self.titre, self.auteur, self.annee)

    def to_tuple_with_id(self):
        # Convertit tous les attributs de l'objet Livre, y compris l'id, en un tuple
        # Utile pour les mises à jour dans la base de données
        return (self.id, self.titre, self.auteur, self.annee)
