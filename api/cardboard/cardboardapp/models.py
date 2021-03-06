from django.db import models

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from PIL import Image
import sys
import io, base64

graph = tf.compat.v1.get_default_graph()  # 推論するセッションの初期化

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)


class Photo(models.Model):
    image = models.ImageField(upload_to='photos')

    IMAGE_SIZE = 224 # 画像サイズ
    MODEL_FILE_PATH = './cardboardapp/ml_models/vgg16_transfer.h5' # モデルファイル
    classes = ['normal_img', 'damage_img']
    num_classes = len(classes)

    def predict(self):
        model = None  # モデルを定義、初期化
        global graph  # 毎回同じモデルにデータを投入して推定できるようにする
        with graph.as_default():
            model = load_model(self.MODEL_FILE_PATH)

            img_data = self.image.read()  # 画像データを格納するための変数データ入れる
            img_bin = io.BytesIO(img_data)  # BytesIO:データをメモリ上に保持して、ファイルのようにアクセス

            image = Image.open(img_bin)
            image = image.convert('RGB')
            image = image.resize((self.IMAGE_SIZE, self.IMAGE_SIZE))
            data = np.asarray(image) / 255.0
            X = []
            X.append(data)
            X = np.array(X)

            result = model.predict([X])[0]  # 予測の一番目の値を表示
            predicted = result.argmax()  # 値の大きい方の番号(配列の添字)を返す
            percentage = int(result[predicted] * 100)  # パーセンテージ表記にする

            return self.classes[predicted], percentage
            # print(self.classes[predicted], percentage)

    def image_src(self):
        with self.image.open() as img:
            base64_img = base64.b64encode(img.read()).decode()

            return 'data:' + img.file.content_type + ';base64,' + base64_img