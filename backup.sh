#!/bin/bash

###################################################
### VARIABLES
###################################################

  date=$(date +"_%y-%m-%d")
  backup_path="/root/backups"
  res1=$(date +%s.%N)

#### Couleurs
  White='\e[1;37m'
  Blue='\e[0;34m'
  Green='\e[0;32m'
  Cyan='\e[0;36m'
  Red='\e[0;31m'
  Purple='\e[0;35m'
  Yellow='\e[1;33m'
  Grey='\e[0;30m'
  NC='\e[39m'

###################################################
### UTILITAIRES et DIVERS
###################################################

script_timings(){

  res2=$(date +%s.%N)
  dt=$(echo "$res2 - $res1" | bc)
  dd=$(echo "$dt/86400" | bc)
  dt2=$(echo "$dt-86400*$dd" | bc)
  dh=$(echo "$dt2/3600" | bc)
  dt3=$(echo "$dt2-3600*$dh" | bc)
  dm=$(echo "$dt3/60" | bc)
  ds=$(echo "$dt3-60*$dm" | bc)

  printf "Temps écoulé: %02.4f s \n" $ds

}

script_start(){

  echo -e "${Green}--------------------------------------------------------------------------------${NC}"
  echo -e "${Green}------------------------   DEBUT  DU  SCRIPT  ----------------------------------${NC}"
  echo -e "${Green}--------------------------------------------------------------------------------${NC}"

  script_timings

}

script_end(){

  script_timings

  echo -e "${Red}--------------------------------------------------------------------------------${NC}"
  echo -e "${Red}--------------------------   FIN   DU   SCRIPT  --------------------------------${NC}"
  echo -e "${Red}--------------------------------------------------------------------------------${NC}"

}

###################################################
###################################################
###           FONCTIONS DE SAUVEGARDE
###################################################
###################################################

##################################
### Test si noms de bases existent
##################################
sauvegarde_variables(){

  if test $# -lt 1
  then
    echo "Manque variables !"
    exit
  fi

script_timings
}

#######################
### Calcul espace libre
#######################
test_espace(){

  DISQUE=$(df --output=avail / | grep '[0-9]')
  DISQUE=$(echo "${DISQUE::-6}")
  echo -e " "
  echo -e " "
  echo -e "Espace libre : ${DISQUE}"
  echo -e " "
  echo -e " "

  if [ $DISQUE -lt 2 ]
  then
    echo -e "${Red} Espace disque insuffisant"
    exit 1
  fi

script_timings
}

###################################
### Export des bases avec mysqldump
###################################
sauvegarde_export(){

for i in $*
do
  echo -e "++++++++++++++++++++++++++++++++++++"
  echo -e "Sauvegarde de la base ${i}"
  echo -e "++++++++++++++++++++++++++++++++++++"
  mysqldump --verbose --databases $i > $backup_path/$i$date.sql
  script_timings

  sleep 1
done

}



# Compression
sauvegarde_zip(){
  cd $backup_path

  for filename in /backup_path/*.sql
  do
    echo -e "Compression de ${filename}"
    tar -czvf $backup_path/$filename$date.tar.gz $filename.sql
  done

}


####################################################################
################### SCRIPT PRINCIPAL ###############################
####################################################################

script_start >> /var/logs/backup.log

sauvegarde_variables >> /var/logs/backup.log
test_espace >> /var/logs/backup.log

sauvegarde_export >> /var/logs/backup.log

script_end >> /var/logs/backup.log
