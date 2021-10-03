const spawn = require('child_process').spawn

function pytorch_model(upload_img) {
    console.log('pytorch model activated')
    console.log(upload_img)
    const PytorchProcess = spawn('python3',['./yolov5/detect.py','-w','./yolov5/weight/yolov5m6.pt','-i', `./org_images/${upload_img}.jpg`,'-o',`./prc_images/prc_${upload_img}.jpg`])

    PytorchProcess.stdout.on('data', (data) =>{
        console.log('python-pytorch Process Done')
        console.log(data.toString())
    })
    
    // standard error handler
    PytorchProcess.stderr.on('data',(data)=>{
        console.log(`stderr:${data}`)
    })
    
    // error handler
    PytorchProcess.on('error',(err)=>{
        console.log(`error: ${err}`)
    })
    
    PytorchProcess.on('exit',(code,signal)=>{
        if (code) {
            console.log(`Process Exit with Code :${code}`)
        }
        if (signal){
            console.log(`Process Killed with signal ${signal}`)
        }
        console.log(`Done !`)
    })
    
    console.log('Running Yolov5 Pytorch Model')
}

// pytorch model export
module.exports = pytorch_model