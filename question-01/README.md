## Ansible playbook to install base servers for production environment

### Variables

Available variables are listed in `vars/main.yml`

```yaml
# 1 - Variables for Essentials role.
## SSH user variables.
users_create_homedirs: yes
users_default_shell: /bin/bash
```

### Roles

- Essentials Role: create ssh accounts, change hostname and `/etc/hosts` file.
- Docker Role: install docker daemon, docker logging + storage driver configuration.
- Tuning Role: some basic tuning configuration for high netowrk traffic workload.

### How to play

- Play all role:

```sh
ansible-playbook main.yml -v
```

- Play a specific role:

```sh
ansible-playbook main.yml -v --tags docker
```
