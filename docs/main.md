# Summary
> These are the commands that may help in future troubles that I have previously encountered or wrote down so I wouldn't forget when I need them.
# If need of pip installation not depending on std libraries
``curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python2.7``

# Basemap
``sudo apt-get install libgeos-3.5.0``

``sudo apt-get install libgeos-dev``

``sudo pip install https://github.com/matplotlib/basemap/archive/master.zip``

# pypy pip installation
``wget https://bootstrap.pypa.io/get-pip.py``

``pypy get-pip.py``

``pypy -m pip install package``

# Keyboard mapping
``sudo apt-get install git gcc make pkg-config libx11-dev libxtst-dev libxi-dev``

``git clone https://github.com/alols/xcape.git``

``cd xcape``

``Make``

``sudo make install``

Learn key code with xcape –d and put # infront of it to use it

``xcape -e '#66=Control_L'``
