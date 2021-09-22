pip install -r requirements.txt
python download_data.py
git clone https://github.com/ultralytics/yolov5 clone_code
mv dataset clone_code
cd clone_code
mv dataset/dataset.yaml data/dataset.yaml
pip install -r requirements.txt
python train.py --img 640 --batch 16 --epochs 3 --data dataset.yaml --weights yolov5s.pt