# programma_sequenze_aritmetiche.py

"""
Modulo per il calcolo delle sequenze aritmetiche.
Contiene funzioni per:
- calcolo del termine n-esimo
- calcolo dei coefficienti a e b dati due termini noti
- calcolo della somma dei primi n termini
"""


def calcola_termine_n(n: int, a: int, b: int) -> int:
    """
    Calcola il n-esimo termine di una sequenza aritmetica.
    Formula: Un = a + (n - 1) * b

    :param n: posizione del termine da calcolare
    :param a: primo termine della sequenza
    :param b: differenza tra i termini
    :return: valore del termine n-esimo
    """
    return a + (n - 1) * b


def calcola_da_due_termini(n1: int, n2: int, u1: int, u2: int) -> dict:
    """
    Calcola a (termine iniziale) e b (differenza) dati due termini della sequenza.

    :param n1: posizione del primo termine noto
    :param n2: posizione del secondo termine noto
    :param u1: valore del primo termine
    :param u2: valore del secondo termine
    :return: dizionario con 'nilai-a' e 'nilai-b'
    """
    differenza_valori = u2 - u1
    differenza_posizioni = (n2 - 1) - (n1 - 1)

    if differenza_posizioni == 0:
        raise ValueError("Le posizioni n1 e n2 non possono essere uguali.")

    b = differenza_valori / differenza_posizioni
    a = u1 - (n1 - 1) * b

    return {
        'nilai-a': a,
        'nilai-b': b
    }


def calcola_somma_n(n: int, a: int, b: int) -> float:
    """
    Calcola la somma dei primi n termini di una sequenza aritmetica.
    Formula: Sn = n/2 * (2a + (n - 1) * b)

    :param n: numero dei termini da sommare
    :param a: primo termine
    :param b: differenza tra i termini
    :return: somma dei primi n termini
    """
    return (n / 2) * (2 * a + (n - 1) * b)
