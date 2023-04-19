# Requirements

1. Ansible installed:

```
sudo apt install python3
python3 -m ensurepip --upgrade
pip3 install ansible
```

# Why such a small role?

I found myself repeating this small piece of logic in several playbooks. I though it would be easier to do it once, and include it everywhere else.

## Required variables

Review the variables as shown in defaults.

The ansible playbook will validate whether the variables exist that you defined before running.

# Example playbook

```
hosts:
  - foo
roles:
  - pimvh.add_github_hostkeys

```

# TLDR - What will happen if I run this

- Add the hostkeys of GitHub fetch via the API to the systems known_host file (/etc/ssh/ssh_known_hosts) specified in the passed list.

TEST TEST TEST
