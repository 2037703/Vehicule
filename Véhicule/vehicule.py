class Vehicule:
    """
    Classe véhicule
    """

    def __init__(self, p_matricule = "", p_annee_fab = 0, p_modele = "", p_prix = 0 ):

        """
        Méthode constructeur
        Attributs
        """

        self.matricule = p_matricule
        self.modele = p_modele
        self.annee_fab = p_annee_fab
        self.prix = p_prix


    def demarrer(self):

        print("Le véhicule démarre")


    def accelerer(self):

        print("Le véhicule accélère")