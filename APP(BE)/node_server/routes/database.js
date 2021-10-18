const mysql = require('mysql')

// config -> .env 파일의 경로를 지정해서
require("dotenv").config({ path: "../.env" });

module.exports = {
	getDB,
}

function getDB() {
	var db = mysql.createConnection({
		host : 'localhost',
		user : 'node_admin',
		password : process.env.db_password,
		database : 'node_db'
	})
	
	db.connect();
	
	if (db){
		console.log('Database Connected')
		return db	
	} else {
		console.log('Database Login Failed')
		return false
	}
}

