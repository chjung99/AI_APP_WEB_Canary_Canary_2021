const express = require('express')
const router = express.Router()
const mysql = require('mysql')
const fs = require('fs')

// pytorch model import
const pytorch_model = require('../run_pytorch')
const bcrypt = require('bcrypt')

const getDB = require('./database').getDB
const db = getDB()

router.get('/main',(req,res)=>{
	// pytorch model child process testing
	pytorch_model('sample_upload') // sample 이미지 명
	req.session.name = 'main'
	res.send({status:200,session:req.session})
})

// Image Upload Router
router.post('/upload',async (req,res)=>{
	console.log('img input router activated')
    console.log(req.session)
	const uploaded_img_binary = req.body.img_binary
	const {d_num} = req.body // upload하는 user의 D_num

	const decoded_img = Buffer.from(uploaded_img_binary,'base64')
	
	const img_id = 'decoded_' + Date.now()
	console.log('uploaded img_id : ', img_id)
	req.session.img_id = img_id

	await fs.writeFile(`org_images/${img_id}.jpg`, decoded_img ,(err)=>{
		if (err){
			console.error(err)
			console.log('original img download Failure')
			res.json({status:500,msg:'Img Download Failure'})
		} else {
			console.log('original img save success')
		}	
	});
	
	// 사용자 업로드 Log 남기기
	db.query('INSERT INTO upload_t(uploader_d_num,img_id) VALUES(?,?)',[d_num,img_id],(err,result)=>{
		if (err){
			console.error(err)
			console.log('original img download Failure')
			res.json({status:500,msg:'User Upload Log Creating Failure'})
		}
		else {
			console.log(result + 'from /img/upload')
		}
		})
	// status code 204 or 205로 변경..?
	res.json({status:200,imd_id:img_id,user_d_num:d_num})

})


// Image Ouput Router : output using request parameters
router.get('/output-params/:img_id/:d_num', async (req,res)=>{

	console.log('img output(params method) router activated')
	console.log('Output Request User의 군번 ', req.params.d_num )
	
	const {img_id} = req.params
	const {d_num} = req.params
	
	if (img_id){
		const hashed_d_num = await bcrypt.hash(d_num,8)
		await pytorch_model(img_id).then((prc_id) =>{
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