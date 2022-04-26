from vehicule import *

class Train(Vehicule):
    """
    Classe Train
    """

    def __init__(self,  p_matricule = "",p_modele = "" ,p_annee_fab = 0, p_prix = 0 ):
        Vehicule.__init__(self,  p_matricule ,p_modele , p_annee_fab , p_prix  )


    def demarrer(self):

        print("le train fais sont départ")


    def accelerer(self):

        print("Le train prend de la vitesse")
