class Emprunt:
    def __init__(self, id=None, id_livre=None, id_adherent=None, date_emprunt=None, date_retour=None):
        # Constructeur de la classe Emprunt
        # Initialise un nouvel objet Emprunt avec les attributs id, id_livre, id_adherent, date_emprunt et date_retour
        self.id = id
        self.id_livre = id_livre
        self.id_adherent = id_adherent
        self.date_emprunt = date_emprunt
        self.date_retour = date_retour

    def __str__(self):
        # Retourne une représentation sous forme de chaîne de caractères de l'objet Emprunt
        # Utile pour l'affichage ou le débogage
        return (f"Emprunt(id={self.id}, id_livre={self.id_livre}, "
                f"id_adherent={self.id_adherent}, date_emprunt={self.date_emprunt}, "
                f"date_retour={self.date_retour})")

    def to_tuple(self):
        # Convertit les attributs de l'objet Emprunt en un tuple
        # Facilite l'insertion dans la base de données
        return (self.id_livre, self.id_adherent, self.date_emprunt, self.date_retour)

    def to_tuple_with_id(self):
        # Convertit tous les attributs de l'objet Emprunt, y compris l'id, en un tuple
        # Utile pour les mises à jour dans la base de données
        return (self.id, self.id_livre, self.id_adherent, self.date_emprunt, self.date_retour)
