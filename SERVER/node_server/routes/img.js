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

router.get('/main',(req,res)=>{
	res.send('this is a img route main page')
})

router.post('/upload',async (req,res)=>{
	console.log('img upload router activated')
    
	const uploaded_img_binary = req.body.img_binary

	const decoded_img = Buffer.from(uploaded_img_binary,'base64')
	
	const img_name = 'decoded' + Date.now()

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
	
	const processed_img = await fs.readFile(`org_images/${img_name}.jpg`)

	const processed_img_encoded = Buffer.from(org_img).toString('base64')
	
	res.json({status:200,output:processed_img_encoded})
	
})

router.get('/output', async(req,res)=>{
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
	
	const processed_img = await fs.readFile(`org_images/${img_name}.jpg`)

	const processed_img_encoded = Buffer.from(org_img).toString('base64')
	
	res.json({status:200,output:processed_img_encoded})
})

module.exports = router