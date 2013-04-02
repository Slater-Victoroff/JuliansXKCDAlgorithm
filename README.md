Steps for running:
1. check http://almamater.xkcd.com/best.csv for olin's current score.
2. go to some empty directory that you want this to run in and run the 
following command line commands:
	sudo apt-get update
	sudo apt-get install git
	git init
	git clone git@github.com:Slater-Victoroff/JuliansXKCDAlgorithm.git
	sudo apt-get install python3 python3-dev

3. Download pyskein from http://pythonhosted.org/pyskein/download.html (download the .tar file)
4. Go to your downloads directory and run:
	tar -xvzf pyskein-0.7.1.tar.gz
	cd pyskein-0.7.1
	python3 setup.py install
5. Go back to the directory that you used git clone in
6. Change the bestCnt value(line 19) in the algorithm.py file to the value
that olin is currently at. Save.
type:
python3 algorithm.py

7. If anything prints out after that upload it to http://almamater.xkcd.com/
Use the email olin.edu
then run it again on a lower number.