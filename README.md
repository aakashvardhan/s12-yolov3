# Using YOLOv3 to detect images

## Table of Contents

- [Introduction](#introduction)
- [YOLOv3](#yolov3)
- [Installation](#installation)
- [Results](#results)


## Introduction

This project is a simple implementation of YOLOv3 to detect images. The project is based on the [YOLOv3 paper](https://arxiv.org/abs/1804.02767) and [YOLOv3 implementation](https://github.com/theschoolofai/YoloV3) by [theschoolofai](https://theschoolof.ai/).

## YOLOv3

YOLOv3 is a state-of-the-art, real-time object detection algorithm. The algorithm applies a single neural network to the full image, and then divides the image into regions and predicts bounding boxes and probabilities for each region. The algorithm is fast and accurate, making it ideal for real-time object detection.

"YoloV3 feature extractor contains skip connections (like ResNet) and 3 prediction heads (like Feature Pyramid Network) - each processing the image at a different spatial compression" - [theschoolofai](https://theschoolof.ai/).

### Architecture

![YOLOv3 Architecture](https://github.com/aakashvardhan/s12-yolov3-demo/blob/main/asset/Screenshot%202024-04-22%20at%207.47.27%E2%80%AFPM.png)

## Installation

Refer to the [installation guide](https://github.com/aakashvardhan/YoloV3)

## Results

### Training Log 

```
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:04<00:00,  1.46it/s]
                 all       100       102  0.000179    0.0098  0.000231  0.000351

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      1/49     11.8G      7.14      7.56         0      14.7         7       512: 100% 7/7 [00:07<00:00,  1.04s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:01<00:00,  3.69it/s]
                 all       100       102         0         0         0         0

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      2/49     11.8G      7.07      2.79         0      9.86        10       512: 100% 7/7 [00:07<00:00,  1.04s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:01<00:00,  3.65it/s]
                 all       100       102         0         0         0         0

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      3/49     11.8G      5.55      2.63         0      8.18         7       512: 100% 7/7 [00:07<00:00,  1.04s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:01<00:00,  3.61it/s]
                 all       100       102         0         0         0         0

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      4/49     11.8G      4.79      3.48         0      8.27        12       512: 100% 7/7 [00:07<00:00,  1.04s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:01<00:00,  3.57it/s]
                 all       100       102         0         0         0         0

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      5/49     11.8G      4.24      3.56         0       7.8         8       512: 100% 7/7 [00:07<00:00,  1.04s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:01<00:00,  3.60it/s]
                 all       100       102         0         0         0         0

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      6/49     11.8G      4.76      3.61         0      8.37         8       512: 100% 7/7 [00:07<00:00,  1.04s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:01<00:00,  3.58it/s]
                 all       100       102         0         0         0         0

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      7/49     11.8G       4.4      3.64         0      8.03         6       512: 100% 7/7 [00:07<00:00,  1.06s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:01<00:00,  3.56it/s]
                 all       100       102         0         0         0         0

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      8/49     11.8G      4.35      3.21         0      7.56         8       512: 100% 7/7 [00:07<00:00,  1.07s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:01<00:00,  3.54it/s]
                 all       100       102         0         0         0         0

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
      9/49     11.8G      4.38      3.55         0      7.92         9       512: 100% 7/7 [00:07<00:00,  1.06s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.36it/s]
                 all       100       102      0.44   0.00862     0.138    0.0169

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     10/49     11.8G      5.45       3.3         0      8.74         8       512: 100% 7/7 [00:07<00:00,  1.06s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.13it/s]
                 all       100       102     0.503     0.608       0.5     0.551

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     11/49     11.8G      4.91      3.08         0      7.99         7       512: 100% 7/7 [00:07<00:00,  1.08s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.06it/s]
                 all       100       102     0.352     0.716     0.501     0.472

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     12/49     11.8G      3.88      2.13         0      6.01         5       512: 100% 7/7 [00:07<00:00,  1.08s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.07it/s]
                 all       100       102     0.141     0.804     0.489     0.241

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     13/49     11.8G      4.95      2.32         0      7.27         8       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.01it/s]
                 all       100       102     0.152     0.833     0.467     0.257

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     14/49     11.8G      3.96      1.87         0      5.83         7       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.04it/s]
                 all       100       102     0.209     0.765     0.548     0.328

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     15/49     11.8G      5.47      1.66         0      7.13         8       512: 100% 7/7 [00:07<00:00,  1.08s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.05it/s]
                 all       100       102     0.144     0.725     0.433      0.24

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     16/49     11.8G      4.37      1.62         0      5.99         9       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.07it/s]
                 all       100       102      0.26     0.676     0.456     0.376

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     17/49     11.8G      3.74      1.36         0       5.1        11       512: 100% 7/7 [00:07<00:00,  1.08s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.14it/s]
                 all       100       102     0.246     0.363     0.148     0.293

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     18/49     11.8G      4.02      1.21         0      5.23         5       512: 100% 7/7 [00:07<00:00,  1.10s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.13it/s]
                 all       100       102     0.594     0.539     0.481     0.565

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     19/49     11.8G      5.08      1.36         0      6.45        11       512: 100% 7/7 [00:07<00:00,  1.08s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.12it/s]
                 all       100       102     0.671     0.588     0.589     0.627

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     20/49     11.8G      4.44      1.23         0      5.67         7       512: 100% 7/7 [00:07<00:00,  1.10s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.07it/s]
                 all       100       102     0.701     0.782     0.729      0.74

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     21/49     11.8G      4.31     0.929         0      5.24         6       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.01it/s]
                 all       100       102     0.537     0.716     0.663     0.614

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     22/49     11.8G      3.18     0.923         0       4.1         6       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.02it/s]
                 all       100       102     0.656     0.692     0.696     0.673

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     23/49     11.8G      3.84      1.25         0      5.09        11       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.02it/s]
                 all       100       102     0.726     0.647     0.718     0.684

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     24/49     11.8G      4.46     0.876         0      5.34         7       512: 100% 7/7 [00:07<00:00,  1.10s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.02it/s]
                 all       100       102     0.719     0.753     0.733     0.736

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     25/49     11.8G      3.27      1.06         0      4.33         7       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.04it/s]
                 all       100       102     0.782     0.703     0.766      0.74

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     26/49     11.8G      3.12     0.919         0      4.04         6       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.06it/s]
                 all       100       102     0.721     0.765     0.741     0.742

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     27/49     11.8G      3.88      1.02         0       4.9        10       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.05it/s]
                 all       100       102     0.794      0.72      0.75     0.755

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     28/49     11.8G      3.69     0.852         0      4.55         5       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.06it/s]
                 all       100       102     0.821     0.814     0.864     0.817

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     29/49     11.8G         3     0.859         0      3.86         7       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  2.99it/s]
                 all       100       102     0.763     0.854      0.87     0.806

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     30/49     11.8G      3.44     0.887         0      4.32         8       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.00it/s]
                 all       100       102     0.822     0.817     0.859      0.82

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     31/49     11.8G      2.76     0.888         0      3.64         6       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.01it/s]
                 all       100       102     0.854     0.801      0.86     0.827

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     32/49     11.8G      3.18     0.852         0      4.03         9       512: 100% 7/7 [00:07<00:00,  1.10s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.04it/s]
                 all       100       102     0.898     0.773     0.866      0.83

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     33/49     11.8G       2.8     0.857         0      3.66         7       512: 100% 7/7 [00:07<00:00,  1.10s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.02it/s]
                 all       100       102     0.893     0.819     0.868     0.854

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     34/49     11.8G      2.69     0.859         0      3.55        10       512: 100% 7/7 [00:07<00:00,  1.11s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.03it/s]
                 all       100       102     0.896     0.849     0.888     0.872

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     35/49     11.8G      2.74     0.744         0      3.48         6       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.03it/s]
                 all       100       102     0.898     0.882     0.891      0.89

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     36/49     11.8G      3.22     0.743         0      3.96         7       512: 100% 7/7 [00:07<00:00,  1.10s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.00it/s]
                 all       100       102     0.905     0.845     0.882     0.874

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     37/49     11.8G      2.73     0.707         0      3.44         7       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.01it/s]
                 all       100       102     0.919     0.853     0.901     0.885

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     38/49     11.8G      2.84     0.777         0      3.62         7       512: 100% 7/7 [00:07<00:00,  1.10s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  2.97it/s]
                 all       100       102     0.916     0.855      0.91     0.884

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     39/49     11.8G       2.7     0.809         0      3.51         9       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.00it/s]
                 all       100       102     0.889     0.853     0.909     0.871

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     40/49     11.8G       2.9     0.789         0      3.69        11       512: 100% 7/7 [00:07<00:00,  1.10s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  2.99it/s]
                 all       100       102     0.908     0.868     0.909     0.887

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     41/49     11.8G      2.21     0.679         0      2.89         5       512: 100% 7/7 [00:07<00:00,  1.10s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.02it/s]
                 all       100       102     0.917     0.871     0.906     0.894

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     42/49     11.8G      2.31      0.78         0      3.09         7       512: 100% 7/7 [00:07<00:00,  1.10s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.04it/s]
                 all       100       102     0.898     0.865     0.908     0.881

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     43/49     11.8G      2.75     0.792         0      3.54         9       512: 100% 7/7 [00:07<00:00,  1.10s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.03it/s]
                 all       100       102     0.899     0.882     0.903     0.891

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     44/49     11.8G      2.45     0.742         0      3.19         7       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  2.99it/s]
                 all       100       102      0.89     0.892     0.911     0.891

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     45/49     11.8G      2.38     0.637         0      3.01         7       512: 100% 7/7 [00:07<00:00,  1.10s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.04it/s]
                 all       100       102     0.899     0.892     0.918     0.896

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     46/49     11.8G       2.2     0.692         0      2.89         8       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.01it/s]
                 all       100       102     0.894     0.906     0.917       0.9

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     47/49     11.8G      2.76      0.61         0      3.37         8       512: 100% 7/7 [00:07<00:00,  1.10s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.03it/s]
                 all       100       102     0.903     0.911     0.925     0.907

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     48/49     11.8G      2.41     0.619         0      3.02         5       512: 100% 7/7 [00:08<00:00,  1.17s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.01it/s]
                 all       100       102     0.915     0.922     0.928     0.918

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     49/49     11.8G      2.46     0.622         0      3.08         5       512: 100% 7/7 [00:07<00:00,  1.09s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 7/7 [00:02<00:00,  3.00it/s]
                 all       100       102     0.922     0.928     0.937     0.925
50 epochs completed in 0.171 hours.
```

### Result Plot

![result](https://github.com/aakashvardhan/YoloV3/blob/master/results.png)

### Inference

Here are some of the inference results:

| Image 1 | Image 2 | Image 3 | Image 4 | Image 5 |
|---------|---------|---------|---------|---------|
| ![Image 1](https://github.com/aakashvardhan/YoloV3/blob/master/output/image_11.jpg) | ![Image 2](https://github.com/aakashvardhan/YoloV3/blob/master/output/image_17.jpg) | ![Image 3](https://github.com/aakashvardhan/YoloV3/blob/master/output/image_22.jpg) | ![Image 4](https://github.com/aakashvardhan/YoloV3/blob/master/output/image_28.jpg) | ![Image 5](https://github.com/aakashvardhan/YoloV3/blob/master/output/image_3.jpg) |

| Image 6 | Image 7 | Image 8 | Image 9 | Image 10 |
|---------|---------|---------|---------|---------|
| ![Image 6](https://github.com/aakashvardhan/YoloV3/blob/master/output/image_30.jpg) | ![Image 7](https://github.com/aakashvardhan/YoloV3/blob/master/output/image_34.jpg) | ![Image 8](https://github.com/aakashvardhan/YoloV3/blob/master/output/image_60.jpg) | ![Image 9](https://github.com/aakashvardhan/YoloV3/blob/master/output/image_74.jpg) | ![Image 10](https://github.com/aakashvardhan/YoloV3/blob/master/output/image_84.jpg) |