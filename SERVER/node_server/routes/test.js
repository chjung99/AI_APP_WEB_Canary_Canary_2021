const express = require('express')
const router = express.Router()
const path = require('path')
const fs = require('fs')
const multer = require('multer')
const axios = require('axios')

//multer에 들어갈 storage 객체 생성
const storage = multer.diskStorage({
	// fs 속 위치를 지정해주는 destination
	destination: (req,file,callback) => {
		callback(null,'images/')
	},
	filename: async (req,file,callback)=>{
		console.log(file)
		// Date 와 file의 originalname을 extend 해줘 파일이름 생성
		filename = Date.now() + path.extname(file.originalname)
		await callback(null,filename)
		// db.query('INSERT INTO upload_t (user_id,timestamp,file_name) VALUES(123,NOW(),?)',[filename],(err)=>{
		// 	if (err) {
		// 		throw error
		// 	}
		// })
	}
})

const upload = multer({storage:storage})

// axios로 post request testing
router.get('/connection',async (req,res)=>{
	
	// sending User info POST request 
	// await axios.post('https://osamhack2021-ai-app-web-canary-canary-g4x9r75r6fq49-4000.githubpreview.dev/test/users', {
	// 	username : 'this is a Test User'
	//   })
	//   .then((res) => {
	// 	console.log('Sending User Info POST done')
	// 	// console.log(res);
	//   })
	//   .catch((error) =>{
	// 	console.log(error);
	//  });
	
	// sending IMG upload POST request
	
	// Converting img -> binary code
	const org_img = fs.readFileSync('images/sample.jpg')
	
	// org_img -> 'base64' 방식으로 Encoding
	const encoded_img = Buffer.from(org_img).toString('base64')
	
	// axios를 이용하여 /img_upload에 post request를 전송한다.
	await axios.post('https://osamhack2021-ai-app-web-canary-canary-g4x9r75r6fq49-4000.githubpreview.dev/test/img_upload',{
		username: 'User from axios post request ',
		img_binary : encoded_img
	}).then((res)=>{
		console.log('Converted Img Sending Success')
	}).catch((err)=>{
		console.error(err)
	})
	
	res.send('Connection Testing')
})


// 210918 request 받기 성공
router.post('/users',async (req,res)=>{
	
	const {username} = req.body
	
	console.log('User name request: ' + username)
		
	// console.log(req)
	// const {m_code} = req.body
	res.json({status:200})
})

// 210919 binary converted img POST request Router
router.post('/img_upload',(req,res)=>{
	console.log('img upload router activated')
	// const {username} = req.body
	// console.log(username)
	
	// 1st try -> flutter에서 binary로 Encoding된 img를 request로 보내주면 이를 활용해 저장하고 decoded_img로 recover 시키는 attempt
	const uploaded_img_binary = req.body.img_binary
	
	// Buffer.from 방식으로 decode 시행
	// uploaded_img가 base64 type으로 구성되어 있음을 선언 후 -> binary로 !! -> 한 후 fs.writeFile을 하면 이미지가 정상적으로 저장되지 않는다 -> base64로 encoding된 data를 이용해 fs.writefile 시행
	
	const decoded_img = Buffer.from(uploaded_img_binary,'base64')
	
	fs.writeFile('decoded_image.jpg', decoded_img ,(err)=>{
		if (err){
			throw err
		} else {
			res.json({status:200})
		}	
	});
	
	
})

/// ------------------------------------------------- ///
// local testing 

router.get('/local_upload',(req,res)=>{
	res.render('home.html')
})

// upload.single multi 등 다양한 방식 존재
// upload.single('form의 name 매개변수를 이용')
// post request에 upload 미들웨어를 거친 후 callback 되는 과정
router.post('/local_upload', upload.single("image_to_upload"),(req,res)=>{
	console.log('file uploaded')
	console.log(req.body)
	res.send('Img Uploaded')
})

//렌더링한 이미지 output.

router.get('/output', (req,res)=>{
	console.log('this page is for output')

	// sendFile 방식으로 이미지 제공... -> 현재 location인 __dirname + img 폴더의 위치를 찾아 sendFile
	res.sendFile(__dirname + '/images/sample.jpg')
	// res.send('hello this is a output page')
})
	
// request_params testing
router.get('/request_params',(req,res)=>{
	console.log(req.query)
	res.send('test done')
})

module.exports = router