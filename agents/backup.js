'use strict'

var yaml 		= require('js-yaml');
var fs 			= require('fs');
var conf 		= '';
var Tail 		= require('tail-forever');
var os			= require('os');
var https	 	= require('https'); 
var logSymbols 	= require('log-symbols');
var watch		= require('node-watch');

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

var checkBookmark = function(fn){
	if(fs.existsSync('.bookmark')){
		return fn(null, yaml.safeLoad(fs.readFileSync('.bookmark')));
	} else {
		fs.readdir('logs/', function(err, files){
			var bookmark = {};
			files.forEach(function(filename){
				bookmark[filename] = 0;
			})
			fs.writeFile('.bookmark',yaml.dump(bookmark),function(werror,wsuccess){
				if(werror) throw werror;
				return fn(null,bookmark);
			})
		});		
	}
}

function main(){
	console.log(logSymbols.info, ' agents started at', (new Date()));
	loadConfig(function(error,bookmark,conf){
		var logpath = "/Users/famasya/Dev/Nodejs/mg-agents/agents/logs/";
		console.log(bookmark);
		// watch('/Users/famasya/Dev/Nodejs/mg-agents/agents/logs/', function(filename){

		// })
	});
	process.on('SIGINT', function(){
		console.log(logSymbols.info, 'SIGINT catched. Bye!');
		process.exit();		
	});
}

main()
