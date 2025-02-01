#!/usr/bin/env python3

# 画像処理用ライブラリ OpenCV をインポート
import cv2

# 画像ファイルのパスを取得するモジュールをインポート
from ament_index_python.packages import get_package_share_directory
import os

# 画像ファイルがあるディレクトリのパスを指定
IMAGE_DIR_PATH = os.path.join(
    get_package_share_directory("introvision2"),
    "img"
)

# 表示させたい画像ファイル名
IMAGE_NAME = "lena.jpg"

# 表示させたい画像ファイルのフルパス
IMAGE_PATH = os.path.join(IMAGE_DIR_PATH, IMAGE_NAME)

# 画像の読み込み
image = cv2.imread(IMAGE_PATH)

# 画像表示
cv2.imshow("image view", image)
cv2.waitKey(0)