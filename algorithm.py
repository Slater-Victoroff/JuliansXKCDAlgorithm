import re
import skein
import random
import requests

def diffHex(x,y):
	x = bin(int(x,16))[2:]
	y = bin(int(y,16))[2:]
	if len(y)<len(x):
		y = '0'*(len(x)-len(y))+y
	if len(x)<len(y):
		x = '0'*(len(y)-len(x))+x
	diffCnt = 0
	for i in range(len(x)):
		if x[i] != y[i]:
			diffCnt += 1
	return diffCnt

correct = b"5b4da95f5fa08280fc9879df44f418c8f9f12ba424b7757de02bbdfbae0d4c4fdf9317c80cc5fe04c6429073466cf29706b8c25999ddd2f6540d4475cc977b87f4757be023f19b8f4035d7722886b78869826de916a79cf9c94cc79cd4347d24b567aa3e2390a573a373a48a5e676640c79cc70197e1c5e7f902fb53ca1858b6"
bestCnt = int(re.search(r'olin\.edu","(\d+)"', requests.get("http://almamater.xkcd.com/best.csv").text).group(1))
log = open("log.txt", "w+")

print('Best count:', bestCnt)

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while True:
	a = ""
	for i in range(random.randint(2,1000)):
		curr = letters[random.randint(0,len(letters)-1)]
		a = a + curr
		theHash = str(skein.skein1024(a.encode(), digest_bits=1024).hexdigest())
		newCnt = diffHex(correct,theHash.encode())
		if newCnt < bestCnt:
			bestCnt = newCnt
			requests.post("http://almamater.xkcd.com/?edu=olin.edu", {'hashable': a})
                        log.write("NEW:\n|%s|\n%d\n\n" %(a, bestCnt))
			print("NEW:\n"+"|"+a+"|")
			print(bestCnt)
			print("\n")
