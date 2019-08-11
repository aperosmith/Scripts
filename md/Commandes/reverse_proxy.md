Redirection du port

    ssh -R 3389:targetIP:3389 root@XX.XX.XX.XX
 
Verification des connexions ouvertes sur le proxy :

    lsof -i -P -n | grep LISTEN

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg1MzM2Nzc0NV19
-->