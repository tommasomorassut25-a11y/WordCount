# Questo programma legge il contenuto di un file di testo
with open("input.txt", "r", encoding="utf-8") as f:
    contenuto = f.read()

# variabile di controllo per il ciclo
Flag = True

# variabile per contare le lettere, simboli e spazi nel file
count_letter = 0
count_symbol = 0
count_space = 0

# ciclo principale del programma
if __name__ == "__main__":

    print("Benvenuto nel programma di lettura del file!")
    print("Cosa vuoi fare?")

    while Flag:
        print("1. Leggi il contenuto del file")
        print("2. Analizza il contenuto del file")
        print("3. Esci")
        
        scelta = input("Inserisci la tua scelta: ")

        if scelta == "1":
            print("==================================")
            print("Il contenuto del file è:")
            print(contenuto)
            print("==================================")
        elif scelta == "2":
            print("==================================")
            print("Analisi del contenuto del file:")
            parole = contenuto.split() # split() divide il contenuto in parole e le memorizza in una lista
            print(f"Il numero di parole nel file è: {len(parole)}")
            for i in contenuto.lower():
                count_letter += 1
                if i in ".,;:!?": # se il carattere è un simbolo, incrementa il contatore dei simboli
                    count_symbol += 1
                elif i == " ": # se il carattere è uno spazio, incrementa il contatore degli spazi
                    count_space += 1
            print(f"Il numero di simboli nel file è: {count_symbol}")
            print(f"Il numero di spazi nel file è: {count_space}")
            print(f"Il numero di lettere nel file è: {count_letter}")
            print("==================================")
        elif scelta == "3":
            print("Uscita dal programma. Arrivederci!")
            Flag = False

# Chiusura file
f.close()