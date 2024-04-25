import os
import time
from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt

os.environ["TFHUB_DOWNLOAD_PROGRESS"] = "True"

class train:
    def __init__(self, path):
        IMAGE_PATH = path
        SAVED_MODEL_PATH = "https://tfhub.dev/captain-pool/esrgan-tf2/1"
        def preprocess_image(self, image_path):
            hr_image = tf.image.decode_image(tf.io.read_file(image_path))
            if hr_image.shape[-1] == 4:
                hr_image = hr_image[..., :-1]
            hr_size = (tf.convert_to_tensor(hr_image.shape[:-1]) // 4) * 4
            hr_image = tf.image.crop_to_bounding_box(hr_image, 0, 0, hr_size[0], hr_size[1])
            hr_image = tf.cast(hr_image, tf.float32)
            return tf.expand_dims(hr_image, 0)
        def save_image(self, image, filename):
            if not isinstance(image, Image.Image):
                image = tf.clip_by_value(image, 0, 255)
                image = Image.fromarray(tf.cast(image, tf.uint8).numpy())
            image.save("%s.jpg" % filename)
            print("Saved as %s.jpg" % filename)
        hr_image = preprocess_image(IMAGE_PATH)
        save_image(tf.squeeze(hr_image), filename="Original Image")
        model = hub.load(SAVED_MODEL_PATH)
        start = time.time()
        fake_image = model(hr_image)
        fake_image = tf.squeeze(fake_image)
        print("Time: %f" % (time.time() - start))
        save_image(tf.squeeze(fake_image), filename="Super Resolution")
