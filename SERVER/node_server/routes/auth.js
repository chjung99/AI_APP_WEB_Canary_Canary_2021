// authentication Router
const express = require('express')
const router = express.Router()
const mysql = require('mysql');
const bcrypt = require('bcrypt')

var db = mysql.createConnection({
	host : 'localhost',
	user : 'node_admin',
	password : process.env.db_password,
	database : 'node_db'
})

db.connect();

const Authentication = (req,res,next)=>{
	if (req.session.d_num && req.session.isAuth == true){
		next()
	} else{
		res.redirect('/')
	}
}


// 전체 user_t 조회 router
router.get('/get-test', async (req,res)=>{
    console.log('Postman Request Successful')
	var db_result
	await db.query('SELECT * FROM user_t', (err,result)=>{
		if (err) {
			throw err
			res.json({status:500,message:"DB 조회 실패..."})
		} else { // err가 나지 않으면
			console.log(result)
			res.json({status:200,message:'DB 조회 성공',result:result})
		}
	})
})

// 210927 post-req -> session 연결 성공
router.post('/post-test',(req,res)=>{
    const {name} = req.body
    const {d_num} = req.body
    // req.session.d_num = d_num
    console.log(name)
    console.log(d_num)
    res.json({status:200,name:name,d_num:d_num})
})

// User 회원가입 Router
router.post('/create-user', async (req,res)=>{
	try{
		const {name} = req.body
		const {d_num} = req.body
		const {password} = req.body
		
		// 보안성 위해 bcrypt 이용 PW 암호화
		const hashedPW = await bcrypt.hash(password,8) // 8은 salt를 의미
		console.log(hashedPW)
		const user = {name:name,d_num:d_num,password:hashedPW}
		// user add to DB code
		await db.query('INSERT INTO user_t(name,d_num,password) VALUES(?,?,?)',[name,d_num,hashedPW],(err,result)=>{
			if (err) {
				throw err
				res.json({status:500})
			}
			else {
				console.log(result)
				// status code 201 = POST Request Handled and Created
				res.json({status:201,user_name:name,msg:'User Created Successful'})
			}
		})
		 // status code 201 = POST Request Handled and Created
	} catch {
		res.json({status:500}) // fulfilled request failed
	}
    
})

router.post('/login',async (req,res)=>{
	const {d_num} = req.body
	const {password} = req.body
	const db_result = await new Promise((resolve,reject)=> 
		db.query('SELECT name,d_num,password FROM user_t WHERE d_num = ?',[d_num],(err,result)=>{
			if (err){
				reject (err)
			} else {
				console.log(result) // result 출력
				if(result.length == 0){
					resolve (false)
					res.json({status:404,msg:'User Not Found'})
				} else { // 즉 해당 d_num을 가진 User 존재 시 -> resolve로 Pass
					resolve (result)
					// res.json({status:200,msg:'User Found'})
				}
			}
		})
	)
	
	try {
		if( await bcrypt.compare(password,db_result[0].password)){
			res.json({status:200,msg:`User : ${db_result[0].name} => Login Successful`})
		}	else {
			console.log('Wrong PW')
			res.json({status:500,msg:'Wrong PassWord - Re Enter PW'})
		}
	} catch (err) {
		console.error(err)
	}
	
})


// 210918 request 받기 성공
router.post('/user_data',async (req,res)=>{
	const {name} = req.body
	const {d_num} = req.body
    console.log('User name request: ' + name)
    console.log('Dog Num request : ' + d_num)
    req.session.d_num = d_num //session에 d_num 저장
    req.session.isAuth = true
    // req.session.save()

    //db 연결 테스트
    await db.query('SELECT * FROM user_t',(err,result)=>{
        if(err) {
            throw err
        } else {
            console.log(result + 'from user auth page')
        }
    })

    res.json({status:200,d_num:d_num,isAuth:req.session.isAuth})
})

module.exports = router

