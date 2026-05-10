# Seat Occupancy Detector using YOLOv8

## Project Overview

This project presents an AI-based seat occupancy detection system developed for smart campus environments such as libraries, cafeterias, classrooms, and study areas. The system detects whether seats are **Available** or **Occupied** using computer vision and object detection techniques based on the YOLOv8 framework.

The project was developed as an improved version of the baseline model from Project 1. Multiple experiments were conducted to improve model accuracy, robustness, and generalization performance.

---

# Project Versions

## Seat_Occupancy_Detector_Version3

Version 3 contains the upgraded YOLOv8l model with:
- improved architecture
- dataset augmentation
- training optimization
- evaluation metrics
- confusion matrices
- validation prediction analysis

This folder includes:
- training scripts
- testing scripts
- curves
- confusion matrices
- labels
- validation batches
- prediction examples
- result visualizations

---

## Seat_Occupancy_Detector_Version4 (Final)

Version 4 represents the final optimized version of the project and includes:
- final trained YOLOv8l model
- improved dataset split
- optimized training configuration
- final evaluation metrics
- final prediction outputs
- updated experiment results

This folder includes:
- final training script
- final testing script
- final confusion matrix
- final result curves
- validation prediction images
- test prediction images
- labels
- trained model weights

---

# Classes

The model detects two classes:
- Available
- Occupied

---

# Technologies Used

- Python
- Ultralytics YOLOv8
- PyTorch
- OpenCV
- Roboflow
- CUDA GPU Acceleration

---

# Hardware Environment

Training was performed using:
- NVIDIA RTX 3070 Ti GPU
- CUDA 12.1
- Python 3.10
- VS Code on Windows

---

# Training Configuration

Final model configuration:
- Model: YOLOv8l
- Epochs: 100
- Batch Size: 4
- Image Size: 832

---

# Repository Structure

```text
Seat_Occupancy_Detector_Version3/
│
├── curves/
├── confusion_matrix/
├── results/
├── labels/
├── test_pics/
├── val_batch/
├── train_script/
└── test_script/

Seat_Occupancy_Detector_Version4 (Final)/
│
├── curves/
├── confusion_matrix/
├── results/
├── labels/
├── test_pics/
├── val_batch/
├── train_script/
└── test_script/
