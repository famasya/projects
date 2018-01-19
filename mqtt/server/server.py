# This script is intended as API endpoints which provide command call to the RaspberryPi's box
# It requires GET/POST REST command to the server encrypted with NaCl secret key string to the box.

from flask import Flask, request, abort, Response
import nacl.secret
import nacl.utils
import json
import MySQLdb
import time

# Flask initialization
app = Flask(__name__)
# Secret key. WARNING: For Development ONLY. Use environment variable for more secure key storage.
key = 'W\x15g\xd6X\xfc\x19\x9e}F\xb7\xaa\xcf\xcf\xd8\x06\xdf\xc3\xa1\x9a\x7f\xa0,\xb9\x1e\x0cE\xc2=)\x85\x8a'
# NaCl instance initialization
box = nacl.secret.SecretBox(key)

# SQL connection
db = MySQLdb.connect("localhost","root","","electra")
cursor = db.cursor()

@app.route('/')
def index():
	abort(404)
	
# This is /endpoint URI which will be accessed by RaspberryPi to send node heartbeat every N seconds. It retrieves REST POST call which contains encrypted NaCl message, and return saved command sent by mobile API access.
@app.route('/endpoint', methods=['POST'])
# Endpoint main function
def retrieve():
	content = request.form['message']
	token = request.form['token']
	
	if(check_token(token)):
		content = json.loads(decrypt(content))[0]
		node_uuid = content['uuid']
		if(save_to_db(content)):
			msg = get_message(node_uuid)
			print msg
			return_string = encrypt(msg)
			return Response(return_string, mimetype="text/plain")
		else:
			return json.dumps({"msg":"Log saving failed"})
	else:
		return abort(401)
		
# Check the token function
def check_token(token):
	validate_token = 'SELECT count(1) FROM device WHERE token=\''+token+'\''
	cursor.execute(validate_token)
	query_result = cursor.fetchone()
	if(query_result != None):
		return True
	else:
		return False
	
# Save command to DB function
def save_to_db(data):
	save_query = "INSERT INTO records(node_uuid, isalive, node_ts, power) VALUES('"+data['uuid']+"','"+data['isalive']+"','"+data['ts']+"','"+data['power']+"')"
	try:
		cursor.execute(save_query)
		db.commit()
		return True
	except:
		print(cursor._last_executed)
		db.rollback()
		return False
		
def get_message(node_uuid):
	msg_query = "SELECT id,command,node_uuid FROM command WHERE node_uuid='"+node_uuid+"' AND executed='F'"
	cursor.execute(msg_query)
	result = cursor.fetchone()
	if(result != None):
		update_status = "UPDATE command SET executed='T' WHERE id='"+str(result[0])+"'"
		cursor.execute(update_status)
		db.commit()
		return "{\"message\":\""+result[1]+"\", \"uuid\":\""+result[2]+"\"}"
	else:
		return ""

# Decryption function. Message is stored by UNICODE number which each character is separated by comma. Return it to the UNICODE character in advance before decrypt it.
def decrypt(data):
	data = data.split(',')
	s = ''
	for i in data:
		s += chr(int(i))
	return box.decrypt(s)

# Encryption function is called to encrypt callback data returned to the RaspberryPi.
def encrypt(data):
	nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
	encrypted = box.encrypt(data, nonce)
	return_string = ''
    # Each character in encrypted message is resolved to its ordinal number to maintain message realibility.
	for i in encrypted:
		o = ord(i)
		return_string += ','+str(o)
	return return_string[1:]
	
# This endpoint provide mobile apps REST API to get current power node's status.
@app.route('/mobile')
# Main endpoint function
def api_index():
	client_token = request.headers['Client-Token']
	uuid,id = check_request_token(client_token)
	if(uuid != None):
		# return uuid
		return Response(get_node_data(uuid), mimetype="application/json")
	else:
		abort(401)

# Check mobile API's authentication
def check_request_token(token):
	validate_client_token = "SELECT device_uuid,id FROM clientdb WHERE token='"+token+"'"	
	cursor.execute(validate_client_token)
	query_result = cursor.fetchone()
	if(query_result != None):
		update_last_access = "UPDATE clientdb SET last_access='"+str(time.time())+"' WHERE device_uuid='"+str(query_result[0])+"'"
		cursor.execute(update_last_access)
		print update_last_access
		db.commit()
		return query_result
	else:
		return None
	
# Get all device latest status
def get_node_data(uuid):
	query = "SELECT CAST(MAX(ts) AS CHAR) ts,isalive,records.node_uuid FROM node RIGHT JOIN records ON node.node_uuid = records.node_uuid WHERE device_uuid = '"+uuid+"' group by isalive, node_uuid"
	cursor.execute(query)
	return json.dumps(cursor.fetchall())
	
@app.route('/mobile', methods=['POST'])
def get_command():
    client_token = request.headers['Client-Token']
    
    uuid,id = check_request_token(client_token)
    if(id != None):
        command = decrypt(request.headers['Client-Command'])
        load = json.loads(command)
        if(save_command(str(id), load)):
            return Response("{\"status\":200}", mimetype="application/json")
        else:
            abort(500)
    else:
        abort(401)
        
def save_command(id, command):
	query = "INSERT INTO command(client_id,command,node_uuid) VALUES("+id+",'"+command['message']+"','"+command['uuid']+"')"
	try:
		cursor.execute(query)
		db.commit()
		return True
	except:
		print(cursor._last_executed)
		db.rollback()
		return False

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)