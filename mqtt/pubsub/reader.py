import paho.mqtt.client as mqtt
import time
import nacl.secret
import nacl.utils
import json
import requests
from tinydb import TinyDB

key = 'W\x15g\xd6X\xfc\x19\x9e}F\xb7\xaa\xcf\xcf\xd8\x06\xdf\xc3\xa1\x9a\x7f\xa0,\xb9\x1e\x0cE\xc2=)\x85\x8a'
box = nacl.secret.SecretBox(key)

def on_connect(client, data, rc):
	channel = "electra"
	print "Connected with result",rc
	client.subscribe(channel)
	
def on_message(client, data, msg):
	nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)

	payload = msg.payload.split(';')
	ts = payload[0]
	isalive = payload[1]
	uuid = payload[2]
	power = payload[3]
	
	encrypted = box.encrypt("[{\"ts\": \""+ts+"\",\"isalive\": \""+isalive+"\",\"uuid\": \""+uuid+"\",\"power\": \""+power+"\"}]", nonce)
	
	val = ""
	for i in encrypted:
		o = ord(i)
		val += ","+str(o)
	send_request(val[1:])
	
def send_request(data):
	url = "http://localhost:5000/endpoint"
	headers = {"Cache-Control":"no-cache"}
	payload = {"token":"v6Y89Aa9OnSAGLCaMa0T","message":data}
	
	feedback = requests.post(url, headers=headers, data=payload)
	save_log(feedback.text)
	
def save_log(string):
	db = TinyDB('logs.json')
	log = decrypt(string)
	db.insert({'ts':time.time(),'uuid':log['uuid'],'message':log['message']})
	print "Command saved"
	
def decrypt(string):
	lst = string.split(',')
	s = ''
	for i in lst:
		s += chr(int(i))
	log = json.loads(box.decrypt(s))
	return log
	
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)

client.loop_forever()