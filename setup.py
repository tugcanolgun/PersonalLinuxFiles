from pathlib import Path
import os
import sys

APT = """sudo apt-get install -y libqt4-test qt4-dev-tools tk-dev python-dev libsasl2-dev libqtgui4 tmux libncursesw5-dev papirus-icon-theme libldap2-dev vim-gtk3 python-pyrex libqtcore4 libc6-dev arc-theme libpq-dev qt4-designer touchpad-indicator gcc build-essential python-opengl libgdbm-dev filezilla libgle3 pkg-config python3-dev python3.6-dev python-pyside.qtopengl libsqlite3-dev libqt4-script libssl-dev libbz2-dev libtool libxml2-dev git idle-python2.7 libqt4-dbus libreadline-gplv2-dev python-qt4-gl python3-lxml libxslt1-dev zsh libqt4-network libffi-dev autoconf libqt4-xml python-qt4 htop ranger caca-utils highlight atool w3m poppler-utils mediainfo xbindkeys"""

def create_dirs():
    home = Path().home()
    vim = home / ".vim"
    if not vim.is_dir():
        print(".vim folder created")
        vim.mkdir()
    else:
        print(".vim folder already exists")
    swap = vim / "swap"
    undo = vim / "undo"
    backup = vim / "backup"
    if not swap.is_dir():
        print("swap folder created")
        swap.mkdir()
    else:
        print("swap folder already exists")
    if not undo.is_dir():
        print("undo folder created")
        undo.mkdir()
    else:
        print("backup folder already exists")
    if not backup.is_dir():
        print("backup folder created")
        backup.mkdir()
    else:
        print("backup folder already exists")

def vundle():
    vundle = Path().home() / ".vim" / "bundle" / "Vundle.vim"
    if vundle.is_dir():
        print("Vundle folder already exists")
        return
    command = "git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim"
    os.system(command)

def oh_my_zsh():
    vundle = Path().home() / ".oh-my-zsh"
    if vundle.is_dir():
        print("oh-my-zsh folder already exists")
        return
    command = 'sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"'
    os.system(command)

def ppas():
    command = "sudo add-apt-repository ppa:atareao/atareao -y"
    os.system(command)
    command = "sudo add-apt-repository ppa:papirus/papirus -y"
    os.system(command)

def spotify():
    os.system("xbindkeys --defaults > ~/.xbindkeysrc")
    settings = """"dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause"
    XF86AudioPlay
    "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop"
    XF86AudioStop
    "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next"
    XF86AudioNext
    "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous"
    XF86AudioPrev"""
    os.system(f"echo {settings} >> ~/.xbindkeysrc")
    os.system("xbindkeysrc")

def main():
    print("Welcome to easy installation")
    print("System will not be updated from the start, the necessary packages will be installed")
    input("To continue, press any key...")
    ppas()
    os.system(APT)

    input("Is the installation finished?")
    create_dirs()
    oh_my_zsh()
    vundle()
    spotify()


if __name__ == "__main__":
    if os.getuid() != 0:
        print("Sudo rights is necessary for this script. Program terminated.")
        sys.exit(0)
    main()
    print("Program terminated")


