from vehicule import *

class Voiture(Vehicule):
    """
    Classe voiture
    """
    def __init__(self,p_matricule = "",p_modele = "" , p_annee_fab = 0, p_prix = 0 ):
        Vehicule.__init__(self, p_matricule ,  p_modele, p_annee_fab , p_prix  )


    def demarrer(self):

        print("La voiture démarre")

    def accelerer(self):

        print("La voiture pèse sur le gas")