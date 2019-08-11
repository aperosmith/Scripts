Tester la connexion :

    mysql -h XX.XX.XX.XX -u root -p -e"show databases"

  

mysql -u root -p -e "  ; FLUSH PRIVILEGES;"

mysql -u root -p -e "GRANT ALL PRIVILEGES ON *.* TO 'haproxy_root’@‘XX.XX.XX.XX’ IDENTIFIED BY ‘******’ WITH GRANT OPTION; FLUSH PRIVILEGES"

  

  

  

create user 'replicator'@'%' identified by ‘******’;

grant replication slave on *.* to 'replicator'@'%';

create database example;

grant replication slave on *.* to 'replicator'@'%';

  

stop slave;

CHANGE MASTER TO MASTER_HOST = ’XX.XX.XX.XX’, MASTER_USER = 'replicator', MASTER_PASSWORD = ‘******’, MASTER_LOG_FILE = 'mysql-bin.XXXXXX’, MASTER_LOG_POS = XXXX;

start slave;

  

  

CHANGE MASTER TO MASTER_HOST = ’XX.XX.XX.XX’, MASTER_USER = 'replicator', MASTER_PASSWORD = ‘******’, MASTER_LOG_FILE = 'mysql-bin.XXXXXX, MASTER_LOG_POS = XXXX;

  

Use mysql;

UPDATE user SET authentication_string=PASSWORD('******') WHERE User='root';

UPDATE mysql.user SET plugin = 'mysql_native_password' WHERE User='root';

Flush privileges;

Exit

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTUxMzk3OTIxOSw3MzA5OTgxMTZdfQ==
-->