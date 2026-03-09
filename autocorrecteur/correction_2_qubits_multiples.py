from autocorrecteur.correction import corriger_une_reponse
import numpy as np

def correction_exercice1(reponse):
    """
    Correction de l'exercice 1 : Registre de plusieurs qubits.
    """
    # Réponse attendue
    attendu = np.array([1, 0, 0, 0, 0, 0, 0, 0])

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 1", tol=0, max_essais=3, info="Révisez la fonction à 3 qubits.")

def correction_exercice2(reponse):
    """
    Correction de l'exercice 2 : Opérations sur plusieurs qubits.
    """
    # Réponse attendue
    attendu = np.array([
        [0.70710678, 0., 0., 0., 0., 0., 0., 0., 0.70710678, 0., 0., 0., 0., 0., 0., 0.],
        [0., 0.70710678, 0., 0., 0., 0., 0., 0., 0., 0.70710678, 0., 0., 0., 0., 0., 0.],
        [0., 0., 0.70710678, 0., 0., 0., 0., 0., 0., 0., 0.70710678, 0., 0., 0., 0., 0.],
        [0., 0., 0., 0.70710678, 0., 0., 0., 0., 0., 0., 0., 0.70710678, 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.70710678, 0., 0., 0., 0., 0., 0., 0., 0.70710678, 0., 0., 0.],
        [0., 0., 0., 0., 0., 0.70710678, 0., 0., 0., 0., 0., 0., 0., 0.70710678, 0., 0.],
        [0., 0., 0., 0., 0., 0., 0.70710678, 0., 0., 0., 0., 0., 0., 0., 0.70710678, 0.],
        [0., 0., 0., 0., 0., 0., 0., 0.70710678, 0., 0., 0., 0., 0., 0., 0., 0.70710678],
        [0.70710678, 0., 0., 0., 0., 0., 0., 0., -0.70710678, -0., -0., -0., -0., -0., -0., -0.],
        [0., 0.70710678, 0., 0., 0., 0., 0., 0., -0., -0.70710678, -0., -0., -0., -0., -0., -0.],
        [0., 0., 0.70710678, 0., 0., 0., 0., 0., -0., -0., -0.70710678, -0., -0., -0., -0., -0.],
        [0., 0., 0., 0.70710678, 0., 0., 0., 0., -0., -0., -0., -0.70710678, -0., -0., -0., -0.],
        [0., 0., 0., 0., 0.70710678, 0., 0., 0., -0., -0., -0., -0., -0.70710678, -0., -0., -0.],
        [0., 0., 0., 0., 0., 0.70710678, 0., 0., -0., -0., -0., -0., -0., -0.70710678, -0., -0.],
        [0., 0., 0., 0., 0., 0., 0.70710678, 0., -0., -0., -0., -0., -0., -0., -0.70710678, -0.],
        [0., 0., 0., 0., 0., 0., 0., 0.70710678, -0., -0., -0., -0., -0., -0., -0., -0.70710678]
    ])

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 2", tol=0, max_essais=3, info="Révisez l'opération sur plusieurs qubits.")

def correction_exercice3(reponse):
    """
    Correction de l'exercice 3 : Superposition égale de plusieurs qubits.
    """
    # Réponse attendue
    attendu = np.array([0.35355339, 0.35355339, 0.35355339, 0.35355339, 0.35355339, 0.35355339,
 0.35355339, 0.35355339])

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 3", tol=0, max_essais=3, info="Révisez la fonction pour créer une superposition égale.")

def correction_exercice4(reponse):
    """
    Correction de l'exercice 4 : État de Bell.
    """
    # Réponse attendue
    attendu = np.array([0.70710678, 0., 0., 0.70710678])

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 4", tol=1e-8, max_essais=3, info="Révisez la fonction pour créer un état de Bell.")

