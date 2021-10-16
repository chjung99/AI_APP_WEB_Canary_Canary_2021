const express= require('express')
const path = require('path')
const mysql = require('mysql')
const session = require('express-session')
const axios = require('axios')
const fs = require('fs') // fs for Buffer instance

//process.env에 dotenv 키:값들을 저장
// dotenv.config();
require('dotenv').config()

const app = express()

// PayloadtoolargeError -> 미들웨어들의 limit default 값 설정 변경하여 해결
app.use(express.json({
	limit:"50mb",
}))

app.use(express.urlencoded({
	limit:"50mb",
	extended:false
}))

app.use(session({
	HttpOnly:false, // 기존 true
	secret: process.env.SESSION_SECRET,
	resave:false,
	saveUninitialized:true,
}))

const IndexRouter =require('./routes/index')
const MsgRouter = require('./routes/message')

app.use('/',IndexRouter)
app.use('/message',MsgRouter)

var db = mysql.createConnection({
	host : 'localhost',
	user : 'root',
	password : process.env.db_password,
	database : 'node_db'
})

db.connect();

db.query('SELECT * FROM user_t',(err,result)=>{
	if(err) {
		throw err
	} else {
		console.log(result)
	}
})

// app.use((req, res, next) => {
// 	const err = new Error('Not Found');
// 	err.status = 404;
// 	next(err);
//   });
  
// app.use((err, req, res, next) => {
// 	res.locals.message = err.message;
// 	res.locals.error = req.app.get('env') === 'development' ? err : {};
// 	res.status(err.status || 500);
// 	res.render('error');
// });  

app.listen(5000,(err)=>{
	if (err){
		throw err	
	} else{
		console.log('running on 5000')
	}
})
