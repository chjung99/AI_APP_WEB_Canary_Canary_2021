const express = require('express')
const router = express.Router()
const mysql = require('mysql')

var db = mysql.createConnection({
	host : 'localhost',
	user : 'root',
	password : process.env.db_password,
	database : 'node_db'
})

db.connect()

router.get('/',(req,res)=>{
    const question = req.body.userRequest.utterance;
    const user_bot_id = req.body.userRequest.user.id;
    switch(question){
        case 'osam_test':
            answerdata = {
                'version': '2.0',
                'template': {
                'outputs': [{
                'simpleText': {
                'text': `테스트 성공! 사용자 봇ID는 ${user_bot_id}` + '\n' + 'https://jskakao.run.goorm.io/'
                }
                }],
                }
                }
                res.json(answerdata); 
                //userdata[0] = user_bot_id;
              break;

    }
})