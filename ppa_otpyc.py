import os
import uuid
import magic
import shutil
from Crypto.Cipher import AES

f_cles = "cles.txt"
d_source = "Pachys"
d_temp   = "Temp"
d_sortie = "Sortie"

def popup(message):
    if os.name == 'nt':
        os.system('mshta vbscript:Execute("msgbox ""'+message+'"":close")')
        return True
    else:
        print()
        input(message)
        return False

def dechiffrement(f_source, f_sortie, cle, iv):
    try:
        cipher = AES.new(cle, AES.MODE_CBC, iv)
        chunk_size = 16
        with open(f_source, 'rb') as source:
            with open(f_sortie, 'wb') as sortie:
                while True:
                    chunk = source.read(chunk_size)
                    if not chunk:
                        break
                    decrypted_chunk = cipher.decrypt(chunk)
                    sortie.write(decrypted_chunk)
        return True
    except Exception as e:
        return False
        
def verification(fichier):
    try:
        f_mime = magic.Magic()
        f_type = f_mime.from_file(fichier)
        f_ext = fichier.rsplit('.', 1)[-1].lower()
        if f_ext != "txt":
            f_types = {}
            f_types['db'] = "composite"
            f_types['jpg'] = "jpeg"
            f_types['ini'] = "endian"
            f_types['xlsx'] = "excel"
                
            if f_ext in f_type.lower():
                return True
            elif f_types[f_ext] in f_type.lower():
                return True
            return False
        else:
            f_test = open(fichier, 'r')
            print(f_test.readlines()[0])
            return True
    except Exception as e:
        return False
        
def dechiffrer(fichier):
    ok = False
    f_source = fichier.replace("Pachys\\", "")
    f_temp   = d_temp+"\\"+str(uuid.uuid4())[:8]+"."+os.path.splitext(fichier)[0].rsplit('.', 1)[-1]
    f_sortie = d_sortie+"\\"+os.path.splitext(f_source)[0]
    for paires in cles:
        c = paires.split(" ")
        cle = bytes.fromhex(c[0])
        iv  = bytes.fromhex(c[1])
        if dechiffrement(fichier, f_temp, cle, iv):
            if verification(f_temp):
                ok = True
                break
    if ok:
        print("[OK] "+fichier)
        shutil.copy(f_temp, f_sortie)
        os.remove(fichier)
    else:
        print("[Erreur] "+fichier)

def parcourir(dossier):
    for element in os.listdir(dossier):
        chemin = os.path.join(dossier, element)
        chemin_copie = dossier.replace("Pachys\\", "Sortie\\")
        if not os.path.isdir(chemin_copie):
            os.mkdir(chemin_copie)  
        if os.path.isdir(chemin):
            parcourir(chemin)
        elif chemin.endswith(".pachy"):
            dechiffrer(chemin)

if __name__ == "__main__":
    if not os.path.isfile(f_cles):
        with open(f_cles, 'w') as file:
            file.write("0" * 64 + " " + "0" * 32)
        if popup("Merci d'insérer dans "+f_cles+" les clés de déchiffrement."):
            os.system("start notepad.exe "+os.path.abspath(f_cles))
        exit()
    if not os.path.isdir(d_source):
        os.mkdir(d_source)
        if popup("Merci d'insérer des fichiers à décrypter dans le dossier Pachys."):
            os.system("explorer.exe "+os.path.abspath(d_source))
    if not os.path.isdir(d_temp):
        os.mkdir(d_temp)   
    if not os.path.isdir(d_sortie):
        os.mkdir(d_sortie)
    f_cle = open(f_cles, 'r')
    cles = f_cle.readlines()
    parcourir(d_source)
    shutil.rmtree(d_temp)