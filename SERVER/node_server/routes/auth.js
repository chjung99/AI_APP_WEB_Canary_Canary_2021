// authentication Router
const express = require('express')
const router = express.Router()
const mysql = require('mysql');

// var db = mysql.createConnection({
// 	host : 'localhost',
// 	user : 'root',
// 	password : process.env.db_password,
// 	database : 'node_db'
// })

// db.connect();

const Authentication = (req,res,next)=>{
	if (req.session.d_num && req.session.isAuth == true){
		next()
	} else{
		res.redirect('/')
	}
}

router.get('/get-test',(req,res)=>{
    console.log('Postman testing Successful')
    res.json({status:200,message:"PostMan Test Route"})
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

