var request = require('request');
var cheerio = require('cheerio');
var text, $, found;
var page = 1;

runCrawler();

function runCrawler(){
    console.log("looking for data \"trenggalek\"");
    collection = [];
    crawl(page, function next(url){
        page++;
        crawl(page, next);
        console.log(url);
    });
}

function crawl(page, callback){
    var returnedUrl = [];
    var url = 'http://data.go.id/dataset?page='+page;
    request(url, function (error, response, body) {
      if (!error && response.statusCode == 200) {
        $ = cheerio.load(body);
        $('h3.dataset-heading').each(function(idx){
            url = $(this).find('a').attr('href');
            getID(url, function(returnedUrl){
                return callback(returnedUrl);
            });
        });
      }
    });
}

function getID(url, callback){
    var dataID;
    var url = 'http://data.go.id'+url;
    request(url, function (error, response, body) {
      if (!error && response.statusCode == 200) {
        $ = cheerio.load(body);
        dataID = $('li.resource-item').attr('data-id');
        getQuery(dataID, "trenggalek", function(res){
            if(res !== null){
                return callback("found in : "+url);
            }
            return callback("continue scanning");
        });
      }
    });
}

function getQuery(id, query, callback){
    var url = 'http://data.go.id/api/action/datastore_search?resource_id='+id+'&q='+query;
    request(url, function (error, response, body){
      if (!error) {
        try {
            var result = JSON.parse(body);
            if(result.success){
                var length = Object.keys(result.result.records).length;
                if(length > 0){
                    return callback(result.result.resource_id);
                } else {
                    return callback(null);
                }
            }
        } catch (e) {
            console.log(e,body);
        }
      } else {
        return callback(error);
      }
    });
}
