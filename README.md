Steps for running:

# Setup

Linux: 

```
sudo apt-get update
sudo apt-get install git
sudo apt-get install python3 python3-dev
```

OS X:

```
brew install python3
```

Then install the algorithm in your folder of choice:

```
git clone https://github.com/Slater-Victoroff/JuliansXKCDAlgorithm.git
cd JuliansXKCDAlgorithm

wget http://pypi.python.org/packages/source/p/pyskein/pyskein-0.7.1.tar.gz
tar -xvzf pyskein-0.7.1.tar.gz
cd pyskein-0.7.1
python3 setup.py install
cd ..

wget https://pypi.python.org/packages/source/r/requests/requests-1.2.0.tar.gz
tar -xvzf requests-1.2.0.tar.gz
cd requests-1.2.0.tar.gz
python3 setup.py install
cd ..
```

# Running

```
python3 algorithm.py
```

If there's a solution your computer finds it will automatically be uploaded to xkcd's site and you can just let it run. If it finds an answer and prints it out, rerun the script again!