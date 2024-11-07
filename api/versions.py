from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf


print("TensorFlow version:", tf.__version__)
print("Pillow (PIL) version:", Image.__version__)
print("NumPy version:", np.__version__)
print("Uvicorn version:", uvicorn.__version__)
