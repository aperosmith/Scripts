#!/bin/sh

if test $# -lt 1
then
  echo "Manque fichier !"
  exit 99
fi


for i in `cat $1`
do
  a=`echo $i | cut -d \; -f1`
  b=`echo $i | cut -d \; -f2`
  c=`echo $i | cut -d \; -f3`
  d=`echo $i | cut -d \; -f4`
  echo "login = $b.$a  mot de passe = $c$d"
done
