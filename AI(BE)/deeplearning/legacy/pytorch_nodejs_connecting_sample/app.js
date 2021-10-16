const spawn = require('child_process').spawn

const pythonProcess = spawn('python3',['./sample/pred.py','-p','./dogfromnode.jpg'])

console.log('pytorch testing')

pythonProcess.stdout.on('data', (data) =>{
    console.log('python-pytorch Process Done')
    console.log(data.toString())
})

// standard error handler
pythonProcess.stderr.on('data',(data)=>{
	console.log(`stderr:${data}`)
})

// error handler
pythonProcess.on('error',(err)=>{
	console.log(`error: ${err}`)
})

pythonProcess.on('exit',(code,signal)=>{
	if (code) {
		console.log(`Process Exit with Code :${code}`)
	}
	if (signal){
		console.log(`Process Killed with signal ${signal}`)
	}
	console.log(`Done !`)
})

console.log('pytorch testing done')