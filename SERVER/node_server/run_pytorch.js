const spawn = require('child_process').spawn

const yolov5_dir = '/workspace/AI_APP_WEB_Canary_Canary/AI/yolov5'
console.log(yolov5_dir)

function pytorch_model(upload_img,level) {
    // Promise return function
    return new Promise((res,rej)=>{
        console.log('pytorch model activated')
        console.log(upload_img)
<<<<<<< HEAD
        
        yolo_levels = [(1,'yolov5s6.py'),(2,'yolov5m6.py'),(3,'yolov5l6.py')]
        model_level = yolo_levels[level-1]
        const PytorchProcess = spawn('python3',[`${yolov5_dir}/detect.py`,'-w',`${yolov5_dir}/weight/${model_level}`,'-i', `./org_images/${upload_img}.jpg`,'-o',`./prc_images/prc_${upload_img}_lv${level}.jpg`])
=======
    
        // const PytorchProcess = spawn('python3',['./yolov5/detect.py','-w','./yolov5/weight/yolov5m6.pt','-i', `./org_images/${upload_img}.jpg`,'-o',`./prc_images/prc_${upload_img}.jpg`])
    
        const PytorchProcess = spawn('python3',[`${yolov5_dir}/detect.py`,'-w',`${yolov5_dir}/weight/yolov5s6.py`,'-i', `./org_images/${upload_img}.jpg`,'-o',`./prc_images/prc_${upload_img}.jpg`,'-o2',`./warnings/${upload_img}_warning.txt`])
>>>>>>> ea79169d4268bee6a81e24edd19cd4a15cc35566
    

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
            rej(`error: ${err}`)
        })
        
        // 명령어 실행문 'exit' emit ! close와 구분해야 된다.
        PytorchProcess.on('exit',(code,signal)=>{
            if (code) {
                console.log(`Process Exit with Code :${code}`)
            }
            if (signal){
                console.log(`Process Killed with signal ${signal}`)
            }
            console.log(`Done !`)
            // res(`prc_${upload_img}`) // prc_id
        })

        // spawn으로 생성한 python3 명령어가 실행이 종료되면 'close' emit -> 이후 processed img를 출력해주는 것이 가능하다
        PytorchProcess.on('close',(result)=>{
            console.log(result)
            console.log('Processed Closed')
            res(`prc_${upload_img}_lv${level}`) // prc_id
        })
        
        console.log('Running Yolov5 Pytorch Model')
    })
   
}

// pytorch model export
module.exports = pytorch_model