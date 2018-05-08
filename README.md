# PersonalLinuxFiles
This is my personal setup on fresh xubuntu install. ``setup.py`` will try to install all programs that I mostly use and will install configuration files to $HOME.

## How to run setup.py

``setup.py`` has the name of a conventional python package installer but it actually a basic script to do run bash commands. In order to run ``setup.py``, root privileges are necessary.

> **CAUTION**: Python 3 and newer, preferably 3.6 and up is necessary.

``sudo python3 setup.py``

## Aim
This is not a repository for anybody. It is solely personal. It will install softwares and dependencies for the packages I commonly use. One of them is ``pymssql`` package which I use for Azure SQL Database. For details, consult ``pymssql.md`` file in the repository.

tmux, zsh and oh-my-zsh will be configured.

Following $HOME libraries will be moved to ``$HOME/Libraries`` folder:
1. Desktop
2. Templates
3. Public
4. Music
5. Pictures
6. Videos

> In order to change this setting ``user-dirs.dirs`` file can be configured under ``$HOME/.config/``

