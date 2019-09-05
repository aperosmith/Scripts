Se connecter à l’ESX en SSH (mot de passe habituel)

Naviguer jusqu’au répertoire /etc/vmware

Copier le fichier de licence actuel (licence.cfg) afin d’avoir une sauvegarde.

Puis supprimer le fichier actuel :

    rm -r /etc/vmware/license.cfg

Copier le fichier de licence intégrée à l’ESX :

    cp /etc/vmware/.#license.cfg /etc/vmware/license.cfg

Redémarrer l’agent de management :

    /etc/init.d/vpxa restart


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMzM0NDEwMTRdfQ==
-->