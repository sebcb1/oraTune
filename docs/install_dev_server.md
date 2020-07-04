# Installation d'un serveur de developpement

## Installation de Centos

Sous centos:

- Centos 7.1 Installation
	- Language: English (United States)
	- Software selection: Gnome Desktop
	- KDUMP: disabled
	- Security policy: No profile selecte

Editer /etc/selinux/config:
`SELINUX=disabled`

De-activer le firewall:
```
systemctl stop firewalld.service
systemctl disable firewalld.service
```

Mise à jour du système:
`yum update -y`

Changement du runlevel par défaut:
`systemctl set-default multi-user.target`

Reboot du serveur...

## Installation de postgres

Installation des rpm:
```
yum install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
rpm -Uvh https://download.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum install centos-release-scl-rh
yum install postgresql11-server postgresql11 postgresql11-devel.x86_64
```

Activation du service:
```
systemctl enable postgresql-11
/usr/pgsql-11/bin/postgresql-11-setup initdb
systemctl start postgresql-11
```

Modification de /var/lib/pgsql/11/data/pg_hba.conf:
```
local   all             all                                     md5
host    all             all             127.0.0.1/32            md5
```

Changer le password du user posgres:
```
alter user postgres with password 'NEW_PASSWORD';
```

Resdémarrer postgres:
`systemctl restart postgresql-11`

Creation de la base de données oratune:
```
sudo su - postgres
psql
create database oratune;
create user oratune with encrypted password 'oratune';
grant all privileges on database oratune to oratune;
```

Tester la connexion: `psql  -U oratune -d oratune`

## Installation de rabitmq

Installation des rpm:
```
yum install erlang
yum install rabbitmq-server.noarch
```
Activation du service:
```
systemctl enable rabbitmq-server
systemctl start rabbitmq-server
```

## Installation du client Oracle

Installation des rpm:
```
yum install libaio
wget https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm
rpm -i oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm
```

Ajout dans le profile .bash_profile du user dev:
```
export LD_LIBRARY_PATH=/usr/lib/oracle/19.6/client64/lib:$LD_LIBRARY_PATH
```

## Installation de dcoker

Installation des rpm:
```
yum install docker docker-compose
```

## Installation de Git

Installation des rpm:
```
yum install git.x86_64 
```

## Installation de python 3 et pipenv

Installation des rpm:
```
yum install python3.x86_64 gcc.x86_64 python3-devel.x86_64 
```

Installation de pipenv:
```
pip3 install  pipenv
```




