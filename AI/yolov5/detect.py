import torch
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--image_path', '-p')
parser.add_argument('--weight_path', '-p')

args = parser.parse_args()
# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=args.weight_path)
# Images
img = args.image_path  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
results.xyxy