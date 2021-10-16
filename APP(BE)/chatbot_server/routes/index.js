const express = require('express')
const router = express.Router()

router.get('/',(req,res)=>{
    res.send('This is a Kakao Chatbot Router')
})

module.exports = router