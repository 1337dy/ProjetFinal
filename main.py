from datetime import *
from datetime import datetime
from pathlib import Path
import jsonpickle

#Edward Hajjar Dib #2071849


# La classe Personne
class Personne(object):

#la definition des methodes d'acces : nom et prenom
    def setnom(self, value: str):
                    #la contrainte
        if value.__len__() > 5 or value.__len__() < 21 and value[0].isupper():
            self.__nom = value
        else:
            raise ValueError('Le nom doit être entre 6 et 20 characteres')

    def getnom(self) -> str:
        return self.__nom

    def setprenom(self, value: str):
                    #la contrainte
        if value.__len__() > 5 or value.__len__() < 21 and value[0].isupper():
            self.__prenom = value
        else:
            raise ValueError('Le prenom doit être entre 6 et 20 characteres')

    def getprenom(self) -> str:
        return self.__prenom

    # le constructeur initialise le chemin avec le set
    def __init__(self, nom:str='xxxxxx', prenom:str='xxxxxx'):
        self.setnom(nom)
        self.setprenom(prenom)

    #la methode str
    def __str__(self) -> str :
            return f"Nom : {self.__nom}"\
            f"\nPrenom : {self.__prenom}"


# La classe Employe
class Employe(Personne):

#la definition des methodes d'acces : code et fonction
    def setcode(self, value: int):
        self.__code = value

    def getcode(self) -> int:
        return self.__code

    def setfonction(self, value: str):
        self.__fonction = value

    def getfonction(self) -> str:
        return self.__fonction

    # le constructeur initialise le chemin avec le set
    def __init__(self, nom:str, prenom:str, code:int, fonction:str):
        super().__init__(nom, prenom)
        self.setcode(code)
        self.setfonction(fonction)

    #la methode str
    def __str__(self) -> str :
            return f"Code : {self.__code}"\
            f"\nFonction : {self.__fonction}"


# La classe Client
class Client(Personne):

#la definition des methodes d'acces : telephone et courriel
    def settelephone(self, value: str):
        self.__telephone = value

    def gettelephone(self) -> str:
        return self.__telephone

    def setcourriel(self, value: str):
        self.__courriel = value

    def getcourriel(self) -> str:
        return self.__courriel

    # le constructeur initialise le chemin avec le set
    def __init__(self, nom:str, prenom:str, telephone:str, courriel:str):
        super().__init__(nom,prenom)
        self.settelephone(telephone)
        self.setcourriel(courriel)

    #la methode str
    def __str__(self) -> str :
            return f"Téléphone : {self.__telephone}"\
            f"\nCourriel : {self.__courriel}"


# La classe Reparation
class Reparation(object):

#la definition des methodes d'acces : code , description , montant , datereparation et codeemploye

    def setcode(self, value: int):
        self.__code = value

    def getcode(self) -> int:
        return self.__code

    def setdescription(self, value: str):
        self.__description = value

    def getdescription(self) -> str:
        return self.__description

    def setmontant(self, value: float):
        self.__montant = value

    def getmontant(self) -> float:
        return self.__montant

    def setdatereparation(self, value: datetime):
        self.__datereparation = value

    def getdatereparation(self) -> datetime:
        return self.__datereparation

    def setcodeemploye(self, value: int):
        self.__codeemploye = value

    def getcodeemploye(self) -> int:
        return self.__codeemploye

    # le constructeur initialise le chemin avec le set
    def __init__(self, code:int, description:str, montant:float,datereparation:datetime, codeemploye:int):
        self.setcode(code)
        self.setdescription(description)
        self.setmontant(montant)
        self.setdatereparation(datereparation)
        self.setcodeemploye(codeemploye)

# La classe Voiture
class Voiture(object):

#la definition des methodes d'acces : numerpplaque , marque, modele , couleur , annee , proprietaire et reparations

    def setnumeroplaque(self, value: str):
        self.__numeroplaque = value

    def getnumeroplaque(self) -> str:
        return self.__numeroplaque

    def setmarque(self, value: str):
        self.__marque = value

    def getmarque(self) -> str:
        return self.__marque

    def setmodele(self, value: str):
        self.__modele = value

    def getmodele(self) -> str:
        return self.__modele

    def setcouleur(self, value: str):
        self.__couleur = value

    def getcouleur(self) -> str:
        return self.__couleur

    def setannee(self, value: int):
        self.__annee = value

    def getannee(self) -> int:
        return self.__annee


    def setproprietaire(self, value: Client):
        self.__proprietaire = value

    def getproprietaire(self) -> Client:
        return self.__proprietaire


    def setreparation(self, value: list[Reparation]):
        self.__reparation = value

    def getreparation(self) -> list[Reparation]:
        return self.__reparation

    # le constructeur initialise le chemin avec le set
    def __init__(self, numeroplaque:str, marque:str, modele:str ,couleur:str, annee:int, proprietaire:Client, reparations:list[Reparation]):
        self.setnumeroplaque(numeroplaque)
        self.setmarque(marque)
        self.setmodele(modele)
        self.setcouleur(couleur)
        self.setannee(annee)
        self.setproprietaire(proprietaire)
        self.setreparation(reparations)

    #methode ajouterreparation
    def ajouterreparation(self, element:Reparation)->None:
        pass


# La classe Garage
class Garage(object):

#la definition des methodes d'acces : nom, adresse, telephone , employes et voitures

    def setnom(self, value: str):
        self.__nom = value

    def getnom(self) -> str:
        return self.__nom

    def setadresse(self, value: str):
        self.__adresse = value

    def getadresse(self) -> str:
        return self.__adresse

    def settelephone(self, value: str):
        self.__telephone = value

    def gettelephone(self) -> str:
        return self.__telephone

    def setemployes(self, value: list[Employe]):
        self.__employe = value

    def getemployes(self) -> list[Employe]:
        return self.__employe

    def setvoitures(self, value: list[Voiture]):
        self.__voiture = value

    def getvoitures(self) -> list[Voiture]:
        return self.__voiture

    # le constructeur initialise le chemin avec le set
    def __init__(self, nom:str, adresse:str, telephone:str ,employes:list[Employe], voitures:list[Voiture]):
        self.setnom(nom)
        self.setadresse(adresse)
        self.settelephone(telephone)
        self.setemployes(employes)
        self.setvoitures(voitures)
        #initialisation des 2 listes vides
        self.__employe:list[Employe]=[]
        self.__voiture:list[Voiture]=[]

    ##Création d'employés
    #employe1: Employe = Employe("Dupont", "Pierre", 1, "Mécanicien")
    #employe2 = Employe("Tremblay", "Jean", 2, "Technicien")
    #print(employe1)

    #définition des méthodes utilitaires (employe)
    def isexistemploye(self, numero:int)-> bool:
        trouve:bool=False
        for employe in self.__employe:
            if employe.getcode()==code:
                break
        return trouve

    def ajouteremploye(self, value:Employe)->None:
        if not self.ajouteremploye(value.getcode()):
            self.__employe.append(value)
        else:
            raise ValueError("Le programme existe déjà")

    def supprimerprogramme(self, code:int)->None:
        #vérifier si le programme existe
        if self.isexistemploye(code):
        #trouver sil existe
            for employe in self.__employe:
                if employe.getcode()==code:
                    #supprimer le programme de la liste
                    self.__employe.remove(employe)
                    break
        else:
            raise ValueError("Employé inexistant")

    #la serialisation
    @classmethod
    def serialisergarage(cls, element:Garage, filename: str) -> None:
        # ouvrir le fichier (creer le stream)
        path: Path = Path(filename)
        stream = path.open('w')
        # serialiser la valeur vers un string sous le format json
        strjson: str = jsonpickle.encode(element, indent=4, separators=(',', ':'))
        # ecrire le string vers le fichier
        stream.write(strjson)
        # fermer le stream
        stream.flush()
        stream.close()

    #la deserialisation
    @classmethod
    def deserialisergarage(cls, filename: str) -> Garage:
        # ouvrir le fichier (creer le stream)
        path: Path = Path(filename)
        stream = path.open('r')
        # lire la chaine json a partir dun fichier
        strjson = stream.read()
        # deserialiser la chaine json vers un objet
        reponse: Garage = jsonpickle.decode(strjson)
        # fermer le stream
        stream.close()
        # retourner le resultat deserialisé
        return reponse

    #methode ajouter voiture
    def ajoutervoiture(self, element:Voiture)->None:
        pass

    #methode get voiture
    def getvoiture(self, numeroplaque:str)->Voiture:
        pass

    #methode ajouter reparation
    def ajouterreparation(self, numeroplaque:str, reparation:Reparation)->None:
        pass

    #methode get reparation
    def getreparation(self, numeroplaque:str)->list[Reparation]:
        pass
