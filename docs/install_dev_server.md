# Installation d'un serveur de developpement

# Installation de Centos

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



