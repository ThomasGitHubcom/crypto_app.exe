<p align="center">
	<img src="https://i.ibb.co/5TZfnHm/580b57fbd9996e24bc43bbbf.png" width="200px" alt="Logo Ppa_otpyc"/>
</p>

Ppa_otpyc est un outil conçu pour décrypter les fichiers cryptés par le ransomware crypto_app.exe.<br>La cible était l'entreprise fictive [Dino-Secure](http://dino-secure.be/). Consultez le [DISCLAIMER.md](DISCLAIMER.md) avant toute utilisation.

## Installation
Pour obtenir les bibliothèques nécessaires, veuillez exécuter la commande suivante :
```bash
pip install -r requirements.txt
```


## Utilisation
 * Placez les clés de décryptage dans un fichier cles.txt.
 * Placez les fichiers cryptés dans un dossier *Pachy/* avec l'extension .pachy.
 * Exécutez le programme avec la commande suivante :
```bash
python ppa_otpyc.py
```


## Informations
MD5 de crypto_app.exe : eb650779a398dc08b72af5f0f876841e<br>
SHA1 de crypto_app.exe : 7fa13c0b373bbfa017c4faa7bfa514eff07912c6