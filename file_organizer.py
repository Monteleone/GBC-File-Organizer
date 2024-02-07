import os
import shutil

def organizza_files_gba(path):
    # Cicla attraverso tutti i file nella directory specificata
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)

        # Verifica se il percorso corrente è un file con estensione .gba
        if os.path.isfile(filepath) and filename.endswith(".gbc"):
            # Crea una nuova cartella con il nome del file (senza estensione)
            folder_name = os.path.splitext(filename)[0]
            new_folder = os.path.join(path, folder_name)

            # Verifica se la cartella già esiste, altrimenti la crea
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            # Sposta il file nella nuova cartella
            new_filepath = os.path.join(new_folder, filename)
            shutil.move(filepath, new_filepath)

if __name__ == "__main__":
    # Specifica il percorso in cui cercare i file .gba
    path_da_esaminare = "C:\\Users\\plusg\\Downloads\\Roms\\gbc\\gbc"

    # Chiama la funzione per organizzare i file .gba
    organizza_files_gba(path_da_esaminare)
