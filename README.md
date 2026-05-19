# Candy Detection using YOLOv8m

## create conda environment
```bash
conda create -n pytorch_env python=3.13

conda activate pytorch_env

```

## install dependancies
```bash
pip install pytorch

pip install ultralytics

```

## train yolo model using custome dataset
```bash
yolo task=detect mode=train epochs=100 data=data_custom.yaml model=yolov8m.pt batch=16

```

## Get prediction using model
```bash
yolo task=detect mode=predict model=yolov8m_custom.pt show=True conf=0.5 source=1.jpg

yolo task=detect mode=predict model=yolov8m_custom.pt show=True conf=0.5 source=1.mp4

```