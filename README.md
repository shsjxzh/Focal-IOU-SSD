## Focal IoU Loss into Faster-RCNN can be found [here](https://github.com/shsjxzh/Focal-IOU-Detectron). 


## SSD_FPN_Focal_IOU in PyTorch
The code references [Distance-IoU Loss: Faster and Better Learning for Bounding Box Regression](https://github.com/Zzh-tju/DIoU). Currently, some experiments are carried out on the VOC dataset, if you want to train your own dataset, more details can be refer to the links above.


### Losses
Losses can be chosen with the `losstype` option in the `config/config.py` file The valid options are currently: `[Iou|Giou|Diou|Ciou|Focal-iou|Focal-diou|Focal-ciou|SmoothL1]`.

```
VOC:
  'losstype': 'Focal-ciou'
```
### DIoU-NMS
NMS can be chosen with the `nms_kind` option in the `config/config.py` file. If set it to `greedynms`, it means using greedy-NMS.
Besides that, similar to DIoU-NMS in Faster R-CNN, we also introduce `beta1` for DIoU-NMS in SSD, that is DIoU = IoU - R_DIoU ^ {beta1}. With this operation, DIoU-NMS may perform better than default beta1=1.0. But for SSD `beta1=1.0` seems to be good enough. For more information, please refer to this [paper](https://arxiv.org/abs/1911.08287)
```
  'nms_kind': "diounms"
```

## Fold-Structure
The fold structure as follow:
- config/
	- config.py
	- __init__.py
- data/
	- __init__.py
 	- VOC.py
	- VOCdevkit/
- model/
	- build_ssd.py
	- __init__.py
	- backbone/
	- neck/
	- head/
	- utils/
- utils/
	- box/
	- detection/
	- loss/
	- __init__.py
- tools/
	- train.py
	- eval.py
	- test.py
- work_dir/
	

## Environment
- pytorch 1.4.0
- python3+
- visdom 
	- for real-time loss visualization during training!
	```Shell
	pip install visdom
	```
	- Start the server (probably in a screen or tmux)
	```Shell
	python visdom
	```
  * Then (during training) navigate to http://localhost:8097/ (see the Train section below for training details).


## Datasets
- PASCAL VOC:Download VOC2007, VOC2012 dataset, then put VOCdevkit in the data directory


## Training

### Training VOC
- The pretrained model refer [pretrained-models.pytorch](https://github.com/Cadene/pretrained-models.pytorch),you can download it.

- In the DIoU-SSD-pytorch fold:
```Shell
python tools/train.py
```

- Note:
  * For training, default NVIDIA GPU.
  * You can set the parameters in the train.py (see 'tools/train.py` for options) 
  * In the config,you can set the work_dir to save your training weight.(see 'configs/config.py`) 

## Evaluation
- To evaluate a trained network:

```Shell
python tools/ap.py --trained_model {your_weight_address}
```

## Test
- To test a trained network:

```Shell
python test.py -- trained_model {your_weight_address}
```
if you want to visual the box, you can add the command --visbox True(default False)

## Performance

#### VOC2007 Test mAP
- Backbone is ResNet50-FPN:

| Test |AP50|AP75|AP50-95|
|:-:|:-:|:-:|:-:|
|IoU|76.71|52.24|48.72|
|Focal-IoU|77.13|53.06|49.24|
|DIoU|76.62|51.89|48.67|
|Focal-DIoU|76.99|52.55|49.08|
|CIoU|76.76|52.58|48.84|
|Focal-CIoU|77.09|53.18|48.99|

## Pretrained weights

Here are the trained models using the configurations in this repository.

 - [IoU](https://pan.baidu.com/s/12IBhR5QMOr6EPTc_Po4M9g) pw: ulyn
 - [Focal-IoU](https://pan.baidu.com/s/1JO7d9ddssBesSw944ofoyw) pw: 2qes
 - [DIoU](https://pan.baidu.com/s/1HV6f86cFilhsFUWTyl-UfQ) pw: zb00
 - [Focal-DIoU](https://pan.baidu.com/s/1atGOmobYe-qv9JOJ9_OMsQ) pw: 5b1v
 - [CIoU](https://pan.baidu.com/s/1t3thhibAcmsw1AYeBgm-fg) pw: z11g
 - [Focal-CIoU](https://pan.baidu.com/s/1PJUCEGiVn2GzUmmgaq1yyg) pw: ucva
