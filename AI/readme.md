# AI

## 코드 구조 설명
- Canary_model_zoo: 다양한 train model with weights(Easy tutorial ->SSD,Multi GPU ->EfficientDet)
- lagacy: 사용하지 않은 코드들 (ex: 데이터 전처리)
- yolov5: yolov5 + knowledge distillation 학습 및 모자이크 코드
- dataserver: MLOps server 코드(django)

## Train weight django

```
python train_starter_django.py -f [FILE PATH]
```
