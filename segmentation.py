import torch
from PIL import Image
import io
from torchvision import transforms
from ultralytics import YOLO


def get_yolov5():
    model = torch.hub.load('./yolov5', 'custom',
                           path='./model/best.pt', source='local')
    model.conf = 0.1
    return model

def get_yolov8():
    model = YOLO('./model/best_v8.pt')
    return model


# def get_image_from_bytes(binary_image, max_size=1024):
    
#     transform = transforms.Compose([
#             transforms.ToTensor(),
#             transforms.Resize((max_size, max_size)),
#         ])

#     input_image = Image.open(io.BytesIO(binary_image)).convert("RGB")
#     resized_image = transform(input_image)
#     return resized_image

def get_image_from_bytes(binary_image, max_size=1024):
    input_image = Image.open(io.BytesIO(binary_image)).convert("RGB")
    width, height = input_image.size
    resize_factor = min(max_size / width, max_size / height)
    resized_image = input_image.resize((
        int(input_image.width * resize_factor),
        int(input_image.height * resize_factor)
    ))
    return resized_image
