import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential, Model, load_model
from PIL import Image
import sys


# パラメーターの初期化
classes = ['normal_img', 'damage_img']
num_classes = len(classes)
image_size = 224

# 引数から画像ファイルを参照して読み込む
image = Image.open(sys.argv[1])
image = image.convert('RGB')
image = image.resize((image_size, image_size))
data = np.asarray(image) / 255.0
X = []
X.append(data)
X = np.array(X)


# モデルのロード
model = load_model('./vgg16_transfer.h5')

result = model.predict([X])[0]  # 予測の一番目の値を表示
predicted = result.argmax()  # 値の大きい方の番号(配列の添字)を返す
percentage = int(result[predicted] * 100)  # パーセンテージ表記にする

print(classes[predicted], percentage)