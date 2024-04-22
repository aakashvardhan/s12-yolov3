# Using YOLOv3 to detect images

## Table of Contents

- [Introduction](#introduction)
- [YOLOv3](#yolov3)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)


## Introduction

This project is a simple implementation of YOLOv3 to detect images. The project is based on the [YOLOv3 paper](https://arxiv.org/abs/1804.02767) and [YOLOv3 implementation](https://github.com/theschoolofai/YoloV3) by [theschoolofai](https://theschoolof.ai/).

## YOLOv3

YOLOv3 is a state-of-the-art, real-time object detection algorithm. The algorithm applies a single neural network to the full image, and then divides the image into regions and predicts bounding boxes and probabilities for each region. The algorithm is fast and accurate, making it ideal for real-time object detection.

"YoloV3 feature extractor contains skip connections (like ResNet) and 3 prediction heads (like Feature Pyramid Network) - each processing the image at a different spatial compression" - [theschoolofai](https://theschoolof.ai/).

