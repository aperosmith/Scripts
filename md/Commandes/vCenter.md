Activer le shell en ssh

    shell.set --enabled true
    shell

Relancer le service vsphere

    service-control --stop vsphere-client
    service-control --start vsphere-client
    
Vérifier les services en cours d'éxecution

    service-control --status -all

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MzE2Nzk0ODFdfQ==
-->