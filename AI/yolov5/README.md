# Canary yolov5

## Train yolov5 in local
```
python clone_code/train.py --img 640 --batch 1 --epochs 3 --data data/dataset.yaml --weights yolov5m6.pt
```

## Train yolov5 in azure
```
python train_with_azure.py
```

## Mosaic image
```
pip install -qr https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt  # install dependencies
pip install opencv-python googledrivedownloader
python detect.py -w [WEIGHT PATH] -i [INPUT IMAGE PATH] -o [OUTPUT IMAGE PATH] -o2 [OUTPUT WARNING TXT PATH]
```
ex)
```
python detect.py -w ./weight/yolov5m6.pt -i ./image/soldier2.jpg -o ./image/out.jpg -o2 ./image/out_warning.txt -o3 ./out_log.txt
```

### Example
##### input_sample
![image](https://user-images.githubusercontent.com/62923434/136740119-e6c6a563-7725-4cd8-8322-1ebeb43a876c.png)

#### output_sample
![image](https://user-images.githubusercontent.com/62923434/136740097-e29265f5-933a-4cb8-b748-b8627754d7ab.png)


#### out_wart.txt
 노트북,군복 (이/가) 감지되었습니다.혹시 지금 군사 기밀을 노출하진 않으셨나요?
#### out_log.txt
 user_id:21-0124/object:노트북,군복/risk level:5 
### Strength option [on/off]

#### [On(default)]

![image](https://user-images.githubusercontent.com/62923434/136739652-2deb5aba-4652-471a-88c0-5bef4aec8ae8.png)

#### [Off]

![image](https://user-images.githubusercontent.com/62923434/136739773-5ba9e634-b5f9-4bce-bb87-f84fe9e80bd6.png)
