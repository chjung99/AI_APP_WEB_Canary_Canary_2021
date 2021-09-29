const express = require('express')
const router = express.Router()
const mysql = require('mysql')

var db = mysql.createConnection({
	host : 'localhost',
	user : 'root',
	password : process.env.db_password,
	database : 'node_db'
})

db.connect();

router.post('/upload',(req,res)=>{
	console.log('img upload router activated')
    
	// 1st try -> flutter에서 binary로 Encoding된 img를 request로 보내주면 이를 활용해 저장하고 decoded_img로 recover 시키는 attempt
	const uploaded_img_binary = req.body.img_binary
	
	// binary로 변환된 img를 디코딩해준다.
	const decoded_img = Buffer.from(uploaded_img_binary,'base64')
	
	fs.writeFile('decoded_image.jpg', decoded_img ,(err)=>{
		if (err){
			throw err
		} else {
			res.json({status:200})
		}	
	});
	
	// db.query('INSERT INTO user_upload_t ()',(err,result)=>{
	// 	if (err){
	// 		throw err
	// 	}
	// 	else {
	// 		console.log(result + 'from /img/upload')
	// 	}
	// })
	
	res.json({status:200})
	
})

router.get('/output',(req,res)=>{

})

module.exports = router