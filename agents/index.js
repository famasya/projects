'use strict'

// Initializing glboal variables
var yaml 		= require('js-yaml');
var fs 			= require('fs');
var conf 		= '';
var Tail 		= require('tail-forever');
var os			= require('os');
var https	 	= require('http'); 
var logSymbols 	= require('log-symbols');
var watch		= require('node-watch');
var LReader		= require('line-by-line');

// Function to load configuration. Returning bookmark and common configurations
var loadConfig = function(fn){
	checkBookmark(function(error, bookmark){
		try {
			conf = yaml.safeLoad(fs.readFileSync('config.yml', 'utf8'));
			return fn(null,bookmark,conf)	
		} catch(e) {
			return fn(e,null,null)
		}		
	})
}

// Function to load line bookmark
var checkBookmark = function(fn){
	if(fs.existsSync('bookmark.yml')){
		return fn(null, yaml.safeLoad(fs.readFileSync('bookmark.yml')));
	} else {
		return fn(".bookmark file not found",null);
	}
}

// Main function
function main(){
	console.log(logSymbols.info, ' agents started at', (new Date()));
	loadConfig(function(error,bookmark,conf){
		var logpath = conf['common']['bro_path'];

		// Define TLS/SSL request configuration
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
		// Agent token
		var token = conf['common']['token'];

		// Start watch log folder
		watch(logpath, function(filename){
			var lr = new LReader(filename);
			filename = filename.split('/');
			filename = filename[filename.length-1];
			var lastline = bookmark['bro'][filename];
			var linecounter = 0;
			var data = '';
			var timestamp 	= Date.now();
			var hostname 	= os.hostname();

			// When change detected, read it line-by-line in stream to avoid memory leakage
			lr.on('line', function(line){
				if(linecounter < lastline){
					linecounter++;					
				} else {
					linecounter++;
					bookmark['bro'][filename] = linecounter;
					var token		= conf['common']['token'];
					data 			+= line+'\t'+timestamp+'\t'+hostname+'\n';
				}
			});

			// on end file reading
			lr.on('end', function(){
				data			= {"token":token, "message":data, "log_name":filename}
				var postBody	= JSON.stringify(data);

				// make HTTPS request
				var req = https.request(options, function(res){
					res.on('data', function(data){
						console.log(logSymbols.success, "Chunk sent at", timestamp);
						// Update bookmark
						fs.writeFile('bookmark.yml',yaml.dump(bookmark),function(werror,wsuccess){
							if(werror) throw werror;
							console.log(logSymbols.info, 'writing index',bookmark['bro'][filename],'on',filename);
						})
					})
				});
				req.write(postBody)
				req.end(); 
				req.on('error', function(e) {
				    console.error(logSymbols.error, e); 
				});
			})
		})
	});

	// Catch SIGINT signal
	process.on('SIGINT', function(){
		console.log(logSymbols.info, 'SIGINT catched. Bye!');
		process.exit();		
	});
}

main()
