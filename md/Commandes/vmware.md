Activer le shell en ssh

    shell.set --enabled true
    shell

Relancer le service vsphere

    service-control --stop vsphere-client
    service-control --start vsphere-client

<!--stackedit_data:
eyJoaXN0b3J5IjpbNzU2OTY0NDkyXX0=
-->