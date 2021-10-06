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
// app.use(cors({
//     origin: ["https://osamhack2021-ai-app-web-canary-canary-g4x9r75r6fq49-4000.githubpreview.dev"],
//     credentials: true,
// }));

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

const testRouter = require('./routes/test')
const indexRouter = require('./routes/index')
const authRouter = require('./routes/auth')
const imgRouter = require('./routes/img')

app.use('/test',testRouter)
app.use('/',indexRouter)
app.use('/auth',authRouter)
app.use('/img',imgRouter)

app.use('/local_upload',express.static(path.join(__dirname,'images'))) // /local_upload/abc.png

//ejs로 html 파일 Rendering - Views 폴더
app.set('views','./views')
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);

//images폴더에 관하여 정적인 접근을 가능하게 해줌 ex: https://osam-project-testing-tkqtg.run.goorm.io/sample.jpg 는 images 폴더 안의 sample.jpg를 출력해준다.
app.use(express.static(path.join(__dirname, 'org_images')));
app.use(express.static(path.join(__dirname, 'prc_images'))); // 처리된 이미지 폴더 

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

app.listen(4000,(err)=>{
	if (err){
		throw err	
	} else{
		console.log('running on 4000')
	}
})
