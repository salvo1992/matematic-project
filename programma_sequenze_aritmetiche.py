# Importa la libreria PrettyTable per formattare le tabelle
from prettytable import PrettyTable

# Funzione per mostrare il menu principale
def menu():
    table = PrettyTable(["No", "Menu"])
    table.add_row(["1", "Calcolo del n-esimo termine di una sequenza aritmetica"])
    table.add_row(["2", "Calcolo di informazioni specifiche su due termini di una sequenza aritmetica"])
    table.add_row(["3", "Calcolo della somma dei primi n elementi di una sequenza aritmetica"])
    print("Menu:")
    print(table)

# Funzione per calcolare il n-esimo termine di una sequenza aritmetica
def aritmetica1():
    print("Calcolo del n-esimo termine di una sequenza aritmetica")
    print("-------------------------------------")
    Un = int(input("Inserisci il numero del termine (n): "))
    a = int(input("Inserisci il primo termine della sequenza (a): "))
    b = int(input("Inserisci la differenza tra i termini successivi (b): "))
    print("Formula: Un = a + (n-1) * b")
    print(f"U{Un} = {a} + ({Un}-1) * {b}")
    risultato = a + (Un - 1) * b
    print(f"U{Un} = {risultato}")
    print("")
    back = input("Digita 'y' per tornare al menu principale: ").lower()
    if back == 'y':
        return menu()
    else:
        return

# Funzione per calcolare informazioni specifiche su due termini della sequenza aritmetica
def aritmetica2():
    print("Calcolo di informazioni specifiche su due termini di una sequenza aritmetica")
    print("-------------------------------------")
    info1 = int(input("Inserisci il numero del primo termine (n1): "))
    info2 = int(input("Inserisci il numero del secondo termine (n2): "))
    valore1 = int(input(f"Inserisci il valore di U{info1}: "))
    valore2 = int(input(f"Inserisci il valore di U{info2}: "))
    
    nb = valore2 - valore1
    i21 = (info2 - 1) - (info1 - 1)
    valoreB = nb / i21
    valoreA = valore1 - (info1 - 1) * valoreB
    
    termineScelto = int(input("Inserisci il termine da calcolare: "))
    termineScelto1 = termineScelto - 1
    print(f"Il termine {termineScelto} è {valoreA + termineScelto1 * valoreB}")
    print("")
    back = input("Digita 'y' per tornare al menu principale: ").lower()
    if back == 'y':
        return menu()
    else:
        return

# Funzione per calcolare la somma dei primi n elementi di una sequenza aritmetica
def aritmetica3():
    print("Calcolo della somma dei primi n elementi di una sequenza aritmetica")
    print("-------------------------------------")
    Sn = int(input("Inserisci il numero totale di elementi (n): "))
    a = int(input("Inserisci il primo termine della sequenza (a): "))
    b = int(input("Inserisci la differenza tra i termini successivi (b): "))
    
    valoreFinale = (Sn / 2) * (2 * a + (Sn - 1) * b)
    print(f"La somma dei primi {Sn} elementi è {valoreFinale}")
    print("")
    back = input("Digita 'y' per tornare al menu principale: ").lower()
    if back == 'y':
        return menu()
    else:
        return

# Funzione principale per eseguire il programma
def main():
    menu()
    scelta = input("Scegli un'operazione (1/2/3): ")
    print("")

    while scelta in ('1', '2', '3'):
        if scelta == '1':
            aritmetica1()
        elif scelta == '2':
            aritmetica2()
        elif scelta == '3':
            aritmetica3()
        else:
            print("Scelta non valida. Scegli un'operazione corretta.")
        
        print("")
        scelta = input("Scegli un'operazione (1/2/3): ")
        print("")

    print("Uscita dal programma.")

# Esegui la funzione principale al lancio dello script
if __name__ == "__main__":
    main()
