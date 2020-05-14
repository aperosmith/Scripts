#!/usr/bin/env python
import os
import json
import logging
import time
import subprocess

logging.basicConfig(filename='/var/log/watchdog.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

def check(p):
    pname = p['NAME']
    ps = subprocess.check_output(['ps', '-A'])
    if pname in str(ps):
        logging.info(p['NAME'] + ' is up and running!')
    else:
        logging.warning(p['NAME'] + ' is dead! Restarting ...')
        subprocess.run([p['BIN'], p['ARGS']])

def watchdog(p):
    check(p)
    time.sleep(p['WATCHTIME'])
    watchdog(p)

with open('watchdog.json') as config_file:
    config = json.load(config_file)
for p in config['process']:
    pid = os.fork()
    if pid != 0:
        print('Lancement du watchdog pour : ' + p['NAME'])
        watchdog(p)
