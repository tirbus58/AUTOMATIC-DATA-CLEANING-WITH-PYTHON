import pandas as pd
import os

# Dossier contenant les fichiers CSV
input_folder = "data_input"  # Remplace par le chemin de ton dossier
output_file = "data_output/combined_cleaned_data.csv"  # Fichier de sortie

# Créer le dossier de sortie s'il n'existe pas
os.makedirs("data_output", exist_ok=True)

# Liste pour stocker les DataFrames
all_dataframes = []

# Parcourir tous les fichiers CSV dans le dossier
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_folder, filename)
        print(f"Traitement du fichier : {filename}")
        
        # Lire le fichier CSV
        df = pd.read_csv(file_path)
        
        # Nettoyer les données
        # 1. Supprimer les lignes avec des valeurs manquantes
        initial_rows = len(df)
        df = df.dropna()
        missing_rows = initial_rows - len(df)
        
        # 2. Supprimer les doublons
        initial_rows = len(df)
        df = df.drop_duplicates()
        duplicate_rows = initial_rows - len(df)
        
        # Ajouter le DataFrame nettoyé à la liste
        all_dataframes.append(df)
        
        # Rapport pour ce fichier
        print(f" - {missing_rows} lignes manquantes supprimées")
        print(f" - {duplicate_rows} doublons supprimés")
        print(f" - {len(df)} lignes conservées")

# Fusionner tous les DataFrames
if all_dataframes:
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    
    # Sauvegarder le fichier fusionné
    combined_df.to_csv(output_file, index=False)
    print(f"\nFusion terminée ! Fichier sauvegardé : {output_file}")
    print(f"Total de lignes dans le fichier final : {len(combined_df)}")
else:
    print("Aucun fichier CSV trouvé dans le dossier.")

# Générer un rapport simple (optionnel)
with open("data_output/rapport.txt", "w") as f:
    f.write(f"Rapport d'automatisation\n")
    f.write(f"Nombre de fichiers traités : {len(all_dataframes)}\n")
    f.write(f"Total de lignes dans le fichier final : {len(combined_df) if all_dataframes else 0}\n")
    f.write("Fichiers traités :\n")
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            f.write(f" - {filename}\n")
print("Rapport généré : data_output/rapport.txt")
