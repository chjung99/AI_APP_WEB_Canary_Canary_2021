const express = require('express')
const router = express.Router()
const mysql = require('mysql')
const fs = require('fs')
// pytorch model import
const pytorch_model = require('../run_pytorch')
const bcrypt = require('bcrypt')

// var db = mysql.createConnection({
// 	host : 'localhost',
// 	user : 'root',
// 	password : process.env.db_password,
// 	database : 'node_db'
// })

// db.connect();

router.get('/main',(req,res)=>{
	// pytorch model child process testing
	pytorch_model('sample_upload') // sample 이미지 명
	req.session.name = 'main'
	res.send({status:200,session:req.session})
})

router.post('/upload',async (req,res)=>{
	console.log('img input router activated')
    console.log(req.session)
	const uploaded_img_binary = req.body.img_binary

	const decoded_img = Buffer.from(uploaded_img_binary,'base64')
	
	const img_id = 'decoded_' + Date.now()
	console.log('uploaded img_id : ', img_id)
	req.session.img_id = img_id

	await fs.writeFile(`org_images/${img_id}.jpg`, decoded_img ,(err)=>{
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

	res.json({status:200,imd_id:img_id,session:req.session})
	
})

router.get('/output', async (req,res)=>{

	// db.query('INSERT INTO user_upload_t ()',(err,result)=>{
	// 	if (err){
	// 		throw err
	// 	}
	// 	else {
	// 		console.log(result + 'from /img/upload')
	// 	}
	// })

	console.log('img output(session method) router activated')
	console.log(req.session)

	console.log('session input img_d :' ,req.session.img_id)
	if (req.session.img_id){
		await pytorch_model(req.session.img_id).then((prc_id) =>{
			console.log('process img : ' ,prc_id)
			const processed_img = fs.readFileSync(`prc_images/${prc_id}.jpg`)
			const processed_img_encoded = Buffer.from(processed_img).toString('base64')
			res.json({status:200,output:processed_img_encoded})
		}).catch((err)=>{
			console.error(err)
			res.json({status:404})
		})
	} else {
		console.error('no img_id in request.session')
		res.json({status:404,err_msg:'img_id for output undefined'})
	}


	// 아래 방법도 되지만 Error handling 위해 Promise를 활용
	// await pytorch_model(req.session.input)

})


// output using request parameters

router.get('/output-params/:img_id/:d_num', async (req,res)=>{
// router.get('/output-params/:img_id/:level', async (req,res)=>{ // -> output with levels
	
	// db.query('INSERT INTO user_upload_t ()',(err,result)=>{
	// 	if (err){
	// 		throw err
	// 	}
	// 	else {
	// 		console.log(result + 'from /img/upload')
	// 	}
	// })

	console.log('img output(params method) router activated')

	console.log('params input', req.params)
	console.log('User D_NUM ', req.params.d_num )
	const {d_num} = req.params
	
	if (req.params.img_id){
		const hashed_d_num = await bcrypt.hash(d_num,8)
		await pytorch_model(req.params.img_id).then((prc_id) =>{
			console.log(prc_id)
			const processed_img = fs.readFileSync(`prc_images/${prc_id}.jpg`)
			const processed_img_encoded = Buffer.from(processed_img).toString('base64')
			var warning_txt = fs.readFileSync(`warnings/${prc_id}_warning.txt`).toString('utf-8')
			if (warning_txt.length == 0) {
				warning_txt = '특이사항 없음'	
			}
			res.json({status:200,prc_img:processed_img_encoded,warning_text:warning_txt,hashed_d_num:hashed_d_num})
		}).catch((err)=>{
			console.error(err)
			res.json({status:404})
		})
	} else {
		console.error('no img_id in request parameter')
		res.json({status:404,err_msg:'img_id for output undefined'})
	}
	
	
})

module.exports = router