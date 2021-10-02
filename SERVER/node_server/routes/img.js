const express = require('express')
const router = express.Router()
const mysql = require('mysql')
const fs = require('fs')

var db = mysql.createConnection({
	host : 'localhost',
	user : 'root',
	password : process.env.db_password,
	database : 'node_db'
})

db.connect();

router.get('/main',(req,res)=>{
	req.session.name = 'main'
	res.send({status:200,session:req.session})
})

router.post('/upload',async (req,res)=>{
	console.log('img input router activated')
    console.log(req.session)
	const uploaded_img_binary = req.body.img_binary

	const decoded_img = Buffer.from(uploaded_img_binary,'base64')
	
	const img_name = 'decoded' + Date.now()

	req.session.input = img_name

	await fs.writeFile(`org_images/${img_name}.jpg`, decoded_img ,(err)=>{
		if (err){
			throw err
		} else {
			console.log('original img save success')
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

	res.json({status:200,session:req.session})
	
})

router.get('/output', (req,res)=>{

	// db.query('INSERT INTO user_upload_t ()',(err,result)=>{
	// 	if (err){
	// 		throw err
	// 	}
	// 	else {
	// 		console.log(result + 'from /img/upload')
	// 	}
	// })

	console.log('img output router activated')
	console.log(req.session)
	console.log('session input:' , req.session.input)

	// const processed_img =  fs.readFileSync(`org_images/${req.session.input}.jpg`)
	const processed_img =  fs.readFileSync(`org_images/decoded1633064533381.jpg`)

	const processed_img_encoded = Buffer.from(processed_img).toString('base64')
	
	res.json({status:200,output:processed_img_encoded})
})

module.exports = router