console.log(logSymbols.info, ' setting loaded');
if(error){
	throw error
} else {
	var log 	= new Tail(conf['common']['bro_path']);
	var options = { 
	    hostname: conf['common']['host'], 
	    port: conf['common']['port'], 
	    path: conf['common']['host_path'], 
	    method: 'POST', 
	    key: fs.readFileSync(conf['tls']['key']), 
	    cert: fs.readFileSync(conf['tls']['crt']), 
	    ca: fs.readFileSync(conf['tls']['ca']),
	    headers: {
	    	'Content-Type': 'application/json'
	    }
	}; 

	log.on('line', function(data){
		var timestamp 	= Date.now();
		var hostname 	= os.hostname();
		var token		= conf['common']['token']
		data 			+= '\t'+timestamp+'\t'+hostname
		data			= {"token":token,"message":data}
		var postBody	= JSON.stringify(data);

		var req = https.request(options, function(res){
			res.on('data', function(data){
				console.log(logSymbols.success, "Chunk sent at", timestamp);
			})
		});
		req.write(postBody)
		req.end(); 
		req.on('error', function(e) {
		    console.error(logSymbols.error, e); 
		});
	});

	log.on('error', function(error){
		console.log(logSymbols.error, 'Error :', error)
	});

	log.watch();
}
