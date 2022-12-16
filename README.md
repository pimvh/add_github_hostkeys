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

Review the variables as shown in defaults:

```
E.g.
add_github_hostkeys_users:
- root
- johndoe
- plantpotter
```

The ansible playbook will validate whether the variables exist that you defined before running.

# Example playbook

```
hosts:
  - foo
roles:
  - pimvh.add_github_hostkeys

```

# TLDR - What will happen if I run this

- Add the hostkeys of GitHub fetch via the API to the users specified in the passed list.

# License

The GPLv3 License (GPLv3)

Copyright (c) 2022 Author

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
