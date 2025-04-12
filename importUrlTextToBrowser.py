import webbrowser
import time
import os
import platform

# Chemins des navigateurs selon le système d'exploitation
chemins_navigateurs = {
    "windows": {
        "1": {
            "nom": "Chrome",
            "path": "C:/Program Files/Google/Chrome/Application/chrome.exe"
        },
        "2": {
            "nom": "Firefox",
            "path": "C:/Program Files/Mozilla Firefox/firefox.exe"
        },
        "3": {
            "nom": "Waterfox",
            "path": "C:/Program Files/Waterfox/waterfox.exe"
        },
        "4": {
            "nom": "Brave",
            "path": "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        },
        "5": {
            "nom": "Opera",
            "path": "C:/Users/VotreNomUtilisateur/AppData/Local/Programs/Opera/launcher.exe"
        }
    },
    "linux": {
        "1": {
            "nom": "Chrome",
            "path": "/usr/bin/google-chrome"
        },
        "2": {
            "nom": "Firefox",
            "path": "/usr/bin/firefox"
        },
        "3": {
            "nom": "Waterfox",
            "path": "/usr/bin/waterfox"
        },
        "4": {
            "nom": "Brave",
            "path": "/usr/bin/brave-browser"
        },
        "5": {
            "nom": "Opera",
            "path": "/usr/bin/opera"
        }
    },
    "darwin": {  # macOS
        "1": {
            "nom": "Chrome",
            "path": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        },
        "2": {
            "nom": "Firefox",
            "path": "/Applications/Firefox.app/Contents/MacOS/firefox"
        },
        "3": {
            "nom": "Waterfox",
            "path": "/Applications/Waterfox.app/Contents/MacOS/waterfox"
        },
        "4": {
            "nom": "Brave",
            "path": "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        },
        "5": {
            "nom": "Opera",
            "path": "/Applications/Opera.app/Contents/MacOS/Opera"
        }
    }
}

def detecter_systeme():
    systeme = platform.system().lower()
    if systeme == "darwin":
        return "darwin"  # macOS
    elif systeme == "linux":
        return "linux"
    elif systeme == "windows":
        return "windows"
    else:
        return None

def afficher_menu_systeme():
    print("\nChoisissez votre système d'exploitation :")
    print("1. Windows")
    print("2. Linux")
    print("3. macOS")
    print("0. Quitter")

def afficher_menu_navigateurs():
    print("\nChoisissez un navigateur pour ouvrir les URLs :")
    print("1. Chrome")
    print("2. Firefox")
    print("3. Waterfox")
    print("4. Brave")
    print("5. Opera")
    print("0. Retour")

def verifier_chemin(chemin):
    return os.path.exists(chemin)

def ouvrir_urls(navigateur_path, fichier_urls):
    try:
        # Vérifier si le navigateur existe
        if not verifier_chemin(navigateur_path):
            print(f"ERREUR: Le navigateur n'a pas été trouvé à l'emplacement : {navigateur_path}")
            print("Veuillez vérifier le chemin du navigateur ou l'installer.")
            return False

        # Enregistrer le navigateur
        webbrowser.register('custom_browser', None, webbrowser.BackgroundBrowser(navigateur_path))

        # Vérifier si le fichier d'URLs existe
        if not os.path.exists(fichier_urls):
            print(f"ERREUR: Le fichier {fichier_urls} n'a pas été trouvé.")
            return False

        # Lire et ouvrir les URLs
        with open(fichier_urls, 'r') as file:
            urls = file.readlines()
            if not urls:
                print("Le fichier est vide.")
                return False

            print(f"\nOuverture de {len(urls)} URL(s)...")
            for i, url in enumerate(urls, 1):
                url = url.strip()
                if url:
                    print(f"Ouverture de l'URL {i}/{len(urls)}")
                    webbrowser.get('custom_browser').open_new_tab(url)
                    time.sleep(1)  # Délai entre chaque URL

        print("Toutes les URLs ont été ouvertes avec succès!")
        return True

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return False

def main():
    # Détection automatique du système
    systeme_detecte = detecter_systeme()
    systeme_choisi = None

    while True:
        if systeme_choisi is None:
            print(f"\nSystème détecté automatiquement : {systeme_detecte}")
            afficher_menu_systeme()
            choix_systeme = input("Votre choix (Enter pour utiliser le système détecté) : ").strip()

            if choix_systeme == "":
                systeme_choisi = systeme_detecte
            elif choix_systeme == "0":
                print("Au revoir !")
                break
            elif choix_systeme == "1":
                systeme_choisi = "windows"
            elif choix_systeme == "2":
                systeme_choisi = "linux"
            elif choix_systeme == "3":
                systeme_choisi = "darwin"
            else:
                print("Choix invalide!")
                continue

        # Menu des navigateurs
        afficher_menu_navigateurs()
        choix_nav = input("Votre choix : ").strip()

        if choix_nav == "0":
            systeme_choisi = None  # Retour au menu des systèmes
            continue
        elif choix_nav in ["1", "2", "3", "4", "5"]:
            # Demander le chemin du fichier d'URLs
            fichier_urls = input("\nEntrez le chemin complet vers votre fichier d'URLs : ").strip()

            # Vérifier si le fichier existe
            if not os.path.exists(fichier_urls):
                print(f"ERREUR: Le fichier {fichier_urls} n'existe pas!")
                continue

            navigateur = chemins_navigateurs[systeme_choisi][choix_nav]
            print(f"\nUtilisation de {navigateur['nom']} sur {systeme_choisi}")

            # Permettre la modification du chemin du navigateur
            print(f"Chemin par défaut : {navigateur['path']}")
            modifier_chemin = input("Voulez-vous modifier ce chemin ? (o/N) : ").strip().lower()

            if modifier_chemin == 'o':
                nouveau_chemin = input("Entrez le nouveau chemin : ").strip()
                navigateur['path'] = nouveau_chemin

            # Ouvrir les URLs
            ouvrir_urls(navigateur['path'], fichier_urls)
        else:
            print("Choix invalide!")

if __name__ == "__main__":
    main()