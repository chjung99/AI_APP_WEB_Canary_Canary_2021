const spawn = require('child_process').spawn

// 주최즉 권장 사항에 따라 yolov5_dir 변경
const yolov5_dir = '/workspace/AI_APP_WEB_Canary_Canary/APP(BE)/node_server'
// detect.py directory 최신화
// const yolov5_dir = '/workspace/AI_APP_WEB_Canary_Canary/AI(BE)/deeplearning/kwoledge_distillation_yolov5'
console.log(yolov5_dir)

function pytorch_model(upload_img) {
    // Promise return function
    return new Promise((res,rej)=>{
        console.log('pytorch model activated')
        console.log(upload_img)
    
    	
		// Node_DB의 upload_t로 별도로 log를 저장하기에 로그 저장 경로인 -o3는 별로도 지정해주지 않는다
        const PytorchProcess = spawn('python3',[`${yolov5_dir}/detect.py`,'-w',`${yolov5_dir}/weight/yolov5m6.py`,'-i', `./org_images/${upload_img}.jpg`,'-o',`./prc_images/prc_${upload_img}.jpg`,'-o2',`./warnings/prc_${upload_img}_warning.txt`])
    

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
            console.log(`Pytorch Model Processing Done !`)
        })

        // spawn으로 생성한 python3 명령어가 실행이 종료되면 'close' emit -> 이후 processed img를 출력해주는 것이 가능하다
        PytorchProcess.on('close',(result)=>{
            console.log(result)
            console.log('Processed Closed')
			console.log(`${upload_img} : Processed Closed`)
            res(`prc_${upload_img}`) // prc_id
        })
        
        console.log('Running Yolov5 Pytorch Model')
    })
   
}

// pytorch model export
module.exports = pytorch_model