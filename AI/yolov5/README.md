# Canary yolov5

## Prepare dataset
```
pip install -r requirements.txt
cd datasetup
python download_imagenet_data.py
python download_custom_data.py
```

## Train yolov5
```
cd ..
git clone https://github.com/ultralytics/yolov5 clone_code
mv datasetup/dataset clone_code
cd clone_code
mv dataset/dataset.yaml data/dataset.yaml
pip install -r requirements.txt
python train.py --img 640 --batch 16 --epochs 3 --data data/dataset.yaml --weights yolov5m6.pt
```

## Mosaic image
```
pip install -qr https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt  # install dependencies
pip install opencv-python googledrivedownloader
python detect.py -w [WEIGHT PATH] -i [INPUT IMAGE PATH] -o [OUTPUT IMAGE PATH]
```
ex)
```
python detect.py -w ./weight/yolov5m6.pt -i ./image/soldier2.jpg -o ./image/out.jpg
```
![in](image/soldier2.jpg)
![out](image/yolov5l6.jpg)
