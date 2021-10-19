const express= require('express')
const path = require('path')
const mysql = require('mysql')
const session = require('express-session')
const axios = require('axios')
const fs = require('fs') // fs for Buffer instance
const cors = require('cors') // CORS Flutter -> XMLHttpRequest Error 해결 위해

//process.env에 dotenv 키:값들을 저장
// dotenv.config();
require('dotenv').config()

const app = express()

app.use(cors());	

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

const testRouter = require('./routes/test')
const indexRouter = require('./routes/index')
const authRouter = require('./routes/auth')
const imgRouter = require('./routes/img')
const databaseRouter = require('./routes/database')

app.use('/test',testRouter)
app.use('/',indexRouter)
app.use('/auth',authRouter)
app.use('/img',imgRouter)

//ejs로 html 파일 Rendering - Views 폴더
// app.set('views','./views')
// app.set('view engine', 'ejs');
// app.engine('html', require('ejs').renderFile);

app.use(express.static(path.join(__dirname, 'org_images')));
app.use(express.static(path.join(__dirname, 'prc_images'))); // 처리된 이미지 폴더 
app.use(express.static(path.join(__dirname, 'warnings'))); // 처리된 이미지 폴더 



app.listen(4000,(err)=>{
	if (err){
		throw err	
	} else{
		console.log('running on 4000')
	}
})