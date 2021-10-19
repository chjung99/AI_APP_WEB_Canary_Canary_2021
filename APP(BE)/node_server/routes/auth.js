// authentication Router
const express = require('express')
const router = express.Router()
const mysql = require('mysql');
const bcrypt = require('bcrypt')

const getDB = require('./database').getDB
const db = getDB()

const Authentication = (req,res,next)=>{
	if (req.session.d_num && req.session.isAuth == true){
		next()
	} else{
		res.redirect('/')
	}
}

// User 회원가입 Router
router.post('/create-user', async (req,res)=>{
	try{
		const {name} = req.body
		const d_num = parseInt(req.body.d_num) // str 형태의 d_num -> int로 파싱
		const password = req.body.password.replace(/ /g, "")
		
		// 보안성 위해 bcrypt 이용 PW 암호화
		const hashedPW = await bcrypt.hash(password,8) // 8은 salt를 의미
		const user = {name:name,d_num:d_num,password:hashedPW}
		console.log(user)
		// user add to DB code
		await db.query('INSERT INTO user_t(name,d_num,password) VALUES(?,?,?)',[name,d_num,hashedPW],(err,result)=>{
			if (err) {
				console.log('DB Insert ERROR : Failed To Insert')
				console.error(err.errno)
				if (err.errno == 1062) {
					res.json({status:405,msg:"User with Input D_num Already Exists"})	
				} else {
					res.json({status:500})
				}
			}
			else {
				console.log(result)
				// status code 201 = POST Request Handled and Created
				res.json({status:201,user_name:name,msg:'User Created Successful'})
			}
		})
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
				} else { // 즉 해당 d_num을 가진 User 존재 시 -> resolve로 db_result에 Pass
					resolve (result)
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


module.exports = router

