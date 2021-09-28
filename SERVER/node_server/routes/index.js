const express = require('express')
const router = express.Router()

router.get('/',(req,res)=>{
	res.json({location:'Homepage',user_dnum:req.session.d_num,user_isAuth:req.session.isAuth})
})

module.exports = router