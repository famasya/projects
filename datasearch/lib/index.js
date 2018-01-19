'use strict';

const request 	= require('request')
const cheerio	= require('cheerio')
let text, $, isFound
let page 		= 1

var crawler = (page, callback) => {
	let url 		= 'http://data.go.id/dataset?page='+page
	request(url, (error, response, body) => {
		if(!error && response.statusCode == 200) {
			$ = cheerio.load(body)
			$('h3.dataset-heading').each((index) => {
				let dataURL = $(this).find('a').attr('href')
				getDataID(dataURL, (returnedURL) => {
					return callback(returnedURL)
				})
			})
		}
	})
}

module.exports = {};
