#!/usr/bin/env python
import os
import json
import logging
import time
import subprocess

# 1 Configurer la destination des logs, les niveaux, et le format
logging.basicConfig(filename='/var/log/watchdog.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

# 5 Verifier la presence du processus dans le retour de la commande ps -A
# Ajouter le resultat dans les logs et relancer si necessaire
def check(p):
    pname = p['NAME']
    ps = subprocess.check_output(['ps', '-A'])
    if pname in str(ps):
        logging.info(p['NAME'] + ' is up and running!')
    else:
        logging.warning(p['NAME'] + ' is dead! Restarting ...')
        subprocess.run([p['BIN'], p['ARGS']])

# 4 Lancer la verif du processus, puis attendre avant de relancer la fonction
def watchdog(p):
    check(p)
    time.sleep(p['WATCHTIME'])
    watchdog(p)

# 2 Ouvrir le fichier de configuration, puis parcourir les valeurs
with open('watchdog.json') as config_file:
    config = json.load(config_file)

# 3 Pour chaque processus, lancer un fork qui va le surveiller
for p in config['process']:
    pid = os.fork()
    if pid != 0:
        print('Lancement du watchdog pour : ' + p['NAME'])
        watchdog(p)
